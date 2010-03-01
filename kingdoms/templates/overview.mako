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
					<div class="panel">
						<h3>Running games</h3>
						<ul>
							<li><a href="/lobby/skirmish">New Skirmish Game</a></li>
						%for game_id in c.games:
							<li><a href="/engine/map/${game_id}">${game_id}</a></li>
						%endfor
						</ul>
					</div>
					
					<div class="panel">
						<h3>Available units</h3>
						<ul>
						%for unit in c.units:
							<li><a href="/unit?unit_id=${unit.id}">${unit.short_name}</a></li>
						%endfor
						</ul>
					</div>
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
	