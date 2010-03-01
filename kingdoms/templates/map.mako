<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<title>Kingdoms</title>
		
		<link rel="stylesheet" href="/interface.css" type="text/css">
		
		<script src="/js/jquery.js" type="application/javascript" ></script>
		<script src="/js/jquery.corner.js" type="application/javascript" ></script>
		<script src="/js/kingdoms.js" type="application/javascript" ></script>
		
	</head>
	<body onload="init_game('${c.game.id}');">	
		<!--
			Menu header
		-->
		<table width="250px" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>

				<td align="center">
					<img src="/controls/interface/menu-line-h.png" />
				</td>
				
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>
				
				<td align="center">
					<img src="/controls/interface/menu-line-h.png" />
				</td>
				
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>
				
			</tr>
			
				<!--
					Menu body
				-->
			
			<tr>
				<td width="30" valign="bottom" background="/controls/interface/menu-line-v.png"></td>

				<td valign="top" width="150" height="510">
					<div id="control">
						
						<div id="panel">
							<h3>Selected</h3>
							<div id="progress">
							</div>
							<div id="object">
								Nothing selected
							</div>
						</div>
						<br/>
						
						<div id="panel">
							<h3>Commands</h3>

							<a href="#" id="refresh-map" onclick="update_game_map('${c.game.id}');">Refresh map</a>

							<div id="wait-command">
								<a href="#" onclick="object_wait('${c.game.id}');">Wait</a>
							</div>

							<div id="move-command">
								<a href="#" onclick="object_move('${c.game.id}');">Move</a>
							</div>

							<div id="attack-command">
								<a href="#" onclick="object_attack('${c.game.id});'">Attack</a>
							</div>
						</div>
						
					</div>

				</td>

				<td width="30" valign="bottom" background="/controls/interface/menu-line-v.png"></td>
				

				<td align="center" valign="middle" >
					<canvas id="map" width="${50*int(c.game.map.width)}" height="${50*int(c.game.map.height)}" onclick="select('${c.game.id}', event);">
						Fallback content, in case the browser does not support Canvas.
					</canvas>
				</td>

				<td width="30" valign="bottom" background="/controls/interface/menu-line-v.png"></td>
			</tr>
			
			<!--
				Menu footer
			-->
			
			<tr>
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>

				<td align="center">
					<img src="/controls/interface/menu-line-h.png" />
				</td>
				
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>
				
				<td align="center">
					<img src="/controls/interface/menu-line-h.png" />
				</td>
				
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>
			</tr>
		</table>
	</body>
</html>