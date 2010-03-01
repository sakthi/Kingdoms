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
	<body>	
		<!--
			Menu header
		-->
		<table width="500px" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td>
					<img src="/controls/interface/corners/${c.corner}" />
				</td>

				<td>
					<img src="/controls/interface/menu-line-h.png"  />
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
					<table class="details" border="0" cellspacing="5" cellpadding="0">
						<tr>
							<td>
								<img src="/tiles/default/${c.unit.tile_type}/right.png" border="0">
								<br/>
								<img src="/tiles/default/${c.unit.tile_type}/left.png" border="0">
							</td>
							<td>
								<img src="/tiles/default/${c.unit.tile_type}/info.png" border="0">
							</td>
						 </tr>
						<tr>
							<td class="name" >Name</td><td class="value">${c.unit.short_name} (${c.unit.tile_type})</td>
						</tr>
						<tr>
							<td class="name" >Description</td><td class="value">${c.unit.long_name}</td></td>
						</tr>
						<tr>
							<td class="name" >Armies</td>
							<td class="value" >
								%if len(c.unit.units_of_type) > 0:
								<ul>
									%for unit_of_type in c.unit.units_of_type:
										<il>${unit_of_type.count} unit(s) by command of 
											<a href="/lobby/army_info/${unit_of_type.army_id}">
												${unit_of_type.army.get_hero().name}
											</a>
											by
											<a href="/lobby/player_info/${unit_of_type.army.owner.id}">
												${unit_of_type.army.owner}
											</a>
										</il>
									%endfor
								</ul>
								%else:
									Not hired in any regular army
								%endif
							</td>
						</tr>
						
					</table>
					<a href="/">Back to game lobby</a>
				</td>

				<td width="30" valign="bottom" background="/controls/interface/menu-line-v.png"></td>
			</tr>
			
			<!--
				Menu footer
			-->
			
			<tr>
				<td>
					<img src="/controls/interface/corners/${c.corner}">
				</td>

				<td>
					<img src="/controls/interface/menu-line-h.png"  />
				</td>

				<td>
					<img src="/controls/interface/corners/${c.corner}">
				</td>
			</tr>
		</table>
	</body>
</html>
