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
					<form name="which_hood_ya_from" action="/auth/submit">
						<table cellspacing="15" cellpadding="2">
						  <tr>
							<td>Login:</td>
							<td>
								<input name="login" type="text" />
							</td>
						  </tr>
						  <tr>
							<td>Password:</td>
							<td>
								<input name="password" type="password" />
							</td>
						  </tr>
						</table>

						%if len(c.error) > 0:
							${controls.error(c.error)}
						%endif

						<input type="submit" value="Log in" />
					</form>
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