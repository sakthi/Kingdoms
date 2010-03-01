// Kingdoms Game
// AwesomeStanlyLabs. Stanislav Yudin
// All rights reserved.

//initial game data
var game_map_data = null;
var current_command = null;
var selected_object = null;
var move_directions = null;
//var ajax_load = "<img src='loading.gif' alt='loading...' />";

var ajax_load = "<div id='loading'><img src='/loading.gif' alt='loading...' />Loading...</div>";
function start_ajax()
{
	$("#progress").show();
	$("#progress").html(ajax_load);
}

function stop_ajax()
{
	$("#progress").hide();
}

function init_game(game_id)
{
	update_game_map(game_id);
	
	$("#wait-command").hide();
	$("#move-command").hide();
	$("#attack-command").hide();
	
	$("panel").corner();
}

function object_move(game_id)
{
	if (selected_object) {
		move_directions = {};
		current_command = 'move';
		//set arrows for move
		if (game_map_data.cells[selected_object.mapx + 1][selected_object.mapy] == null) {
			move_directions["rigth"] = [ selected_object.mapx + 1, selected_object.mapy ];
		}
		if (game_map_data.cells[selected_object.mapx - 1][selected_object.mapy] == null) {
			move_directions["left"] = [ selected_object.mapx - 1, selected_object.mapy ];
		}
		if (game_map_data.cells[selected_object.mapx][selected_object.mapy - 1] == null) {
			move_directions["up"] = [ selected_object.mapx, selected_object.mapy - 1 ];
		}
		if (game_map_data.cells[selected_object.mapx][selected_object.mapy + 1] == null) {
			move_directions["down"] = [ selected_object.mapx, selected_object.mapy + 1];
		}
		if (game_map_data.cells[selected_object.mapx + 1][selected_object.mapy - 1] == null) {
			move_directions["ur"] = [ selected_object.mapx + 1, selected_object.mapy - 1];
		}
		if (game_map_data.cells[selected_object.mapx - 1][selected_object.mapy - 1] == null) {
			move_directions["ul"] = [ selected_object.mapx - 1, selected_object.mapy - 1];
		}
		if (game_map_data.cells[selected_object.mapx + 1][selected_object.mapy + 1] == null) {
			move_directions["dr"] = [ selected_object.mapx + 1, selected_object.mapy + 1];
		}
		if (game_map_data.cells[selected_object.mapx - 1][selected_object.mapy + 1] == null) {
			move_directions["dl"] = [ selected_object.mapx - 1, selected_object.mapy + 1];
		}
	}
	
	update_game_map(game_id);
}

function callback_object_selected(answer)
{
	stop_ajax();
	
	if (answer.error) {
		$("#progress").show();
		$("#progress").html("Error:" + answer.error);
	}
	
	//check if arrow clicked complete
	for (direction in move_directions) {
		if ( move_directions[direction][0] == answer.mapx && move_directions[direction][1] == answer.mapy) {
			alert(direction + " clicked");
		}
	}
	
	//clear arrows
	move_directions = null;
	
	//check object selcted
	var object_html = "Nothing selected"
	if (answer.obj) {	
		selected_object = answer
		//object selected
		$("#wait-command").show();
		$("#move-command").show();

		if (answer.unit_type) {
			var object_html = "<img src=\"/controls/banners/" + answer.obj.banner + "\" /><br/>";
			object_html += answer.obj.count + "&nbsp;" + "<a href='/lobby/unit_info/" + answer.obj.unit_type_id + "' >" +
				answer.unit_type.short_name + "(s)</a><br/>";
			object_html += "<smaller>" + answer.unit_type.long_name + "</smaller>";
		}
		else {
			var object_html = "Object " + answer.obj.type + "(" + answer.obj.rotation + ")</p>";
		}
	}
	else {
		//nothing selected
		$("#wait-command").hide();
		$("#move-command").hide();
		$("#attack-command").hide();
	}
	//set html
	$("#object").html(object_html);
	update_game_map(answer.game_id)
}

function select(game_id, event)
{
	pos_x = event.layerX ? event.layerX : event.offsetX?event.offsetX : 0; // +document.body.scrollLeft
	pos_y = event.layerY ? event.layerY : event.offsetY? event.offsetY  : 0; //+document.body.scrollLeft
	
	map = document.getElementById("map");
	if ( !map ) {
		alert('Failed to selected map!');
	}
	
	start_ajax();
	
	$.getJSON('/api/get_object', { game_id: game_id, x: pos_x, y: pos_y,
								left: map.parentElement.offsetLeft,
								top: map.parentElement.offsetTop }, 
						callback_object_selected );
};

function draw_map()
{	
	var map_canvas = document.getElementById("map");
	var grass = new Image();
	grass.src = "/tiles/" + game_map_data.tileset + "/grass.png"
	grass.border = 0
	grass.style.zIndex = 0;
	
	if (map_canvas && map_canvas.getContext) {
		var context = map_canvas.getContext('2d');
		if (context) {
			for (var x = 0; x < game_map_data.width; x++) {
				for (var y = 0; y < game_map_data.height; y++) {
					
					context.drawImage(grass, 50 * x,  50 * y);
					
					if (move_directions) {
						for (var direction in move_directions) {
							if (move_directions[direction][0] == x && move_directions[direction][1] == y) {
								var arrowImage = new Image();
								arrowImage.src = "/controls/move-" + direction + ".png";
								arrowImage.border = 0;
								arrowImage.style.zIndex = 1;
								context.drawImage(arrowImage, 50 * x, 50 * y);
							}
						}
					}
					
					if (game_map_data.cells[x][y]) {
						var obj = game_map_data.cells[x][y];
						
						if (obj.faction) {
							context.strokeStyle = obj.faction;
							context.fillStyle = obj.faction;
							if (selected_object && selected_object.mapx == x && selected_object.mapy == y) {
								context.fillRect(50 * x + 5, 50 * y + 25, 45, 25);
							}
							else {
								context.strokeRect(50 * x + 5, 50 * y + 25, 45, 25);
							}
						}
						
						var objImage = new Image();
						objImage.src = "/tiles/" + game_map_data.tileset + "/" + obj.type + "/" + obj.rotation + ".png"
						objImage.border = 0;
						objImage.style.zIndex = 2;
						if (obj.unit_type) {
							objImage.id = obj.unit_id
						}
						context.drawImage(objImage, 50 * x, (50 * y) - (objImage.height - 50));
					}
				}
			}
		}
		else {
			alert('error: no context created');
		}
	}
	else {
		alert('error: no map-canvas found');
	}
}

function callback_map_data_received(map_data) 
{
	stop_ajax();
	
	game_map_data = map_data;
	
	if (map_data.error) {
		$("#progress").show();
		$("#progress").html("Error:" + map_data.error);
	}
	else {
		draw_map();
	
		$("#progress").hide();
		$("#viewport").show();
	}
}

function update_game_map(game_id)
{
	start_ajax();
	$.getJSON('/api/get_map',  { game_id: game_id}, callback_map_data_received );
}