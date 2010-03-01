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
		<form name="new_skirmish" action="/engine/generate">
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
							<h3>${c.player.fullname}</h3>
							<table border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td>Faction</td>
									<td>
										<select name="player_0_faction">
											<option value="off" >[ OFF ]</option>
											<option value="red" selected="selected" >Red</option>
											<option value="blue" >Blue</option>
											<option value="green">Green</option>
											<option value="purple">Purple</option>
										</select>
									</td>
								</tr>
								<tr>
									<td>Footmans</td>
									<td><input name="player_0_footman" value="100" /></td>
								</tr>
								<tr>
									<td>Archers</td>
									<td><input name="player_0_archer" value="50" /></td>
								</tr>
							</table>
						
						</div>
					
						<div class="panel">
							<h3>Player 2</h3>
							<table border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td>Faction</td>
									<td>
										<select name="player_1_faction">
											<option value="off" >[ OFF ]</option>
											<option value="red">Red</option>
											<option value="blue" selected="selected" >Blue</option>
											<option value="green">Green</option>
											<option value="purple">Purple</option>
										</select>
									</td>
								</tr>
								<tr>
									<td>Footmans</td>
									<td><input name="player_1_footman" value="100" /></td>
								</tr>
								<tr>
									<td>Archers</td>
									<td><input name="player_1_archer" value="50" /></td>
								</tr>
							</table>
						
						</div>
					
						<div class="panel">
							<h3>Player 3</h3>
							<table border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td>Faction</td>
									<td>
										<select name="player_2_faction">
											<option value="off" selected="selected" >[ OFF ]</option>
											<option value="red" >Red</option>
											<option value="blue"  >Blue</option>
											<option value="green"  >Green</option>
											<option value="purple"  >Purple</option>
										</select>
									</td>
								</tr>
								<tr>
									<td>Footmans</td>
									<td><input name="player_2_footman" value="100" /></td>
								</tr>
								<tr>
									<td>Archers</td>
									<td><input name="player_2_archer" value="50" /></td>
								</tr>
							</table>
						
						</div>
					
						<div class="panel">
							<h3>Player 4</h3>
							<table border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td>Faction</td>
									<td>
										<select name="player_3_faction">
											<option value="off" selected="selected">[ OFF ]</option>
											<option value="red"  >Red</option>
											<option value="blue"  >Blue</option>
											<option value="green"  >Green</option>
											<option value="purple"  >Purple</option>
										</select>
									</td>
								</tr>
								<tr>
									<td>Footmans</td>
									<td><input name="player_3_footman" value="100" /></td>
								</tr>
								<tr>
									<td>Archers</td>
									<td><input name="player_3_archer" value="50" /></td>
								</tr>
							</table>
						</div>
						
						<br/>
						<input type="submit" value="Start!" />
					
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
		</form>
	</body>
</html>
