<!DOCTYPE html>
<html>
<head>
	<title>Delete tickets</title>
</head>
<body>
	<?php
		if(!isset($_POST['name'])||!isset($_POST['train'])||!isset($_POST['seat']))
		{
			echo "<p>You havn't entered all the required details.<br />
			Please go back and try again.</p>";
			exit;
		}
		$name=trim($_POST['name']);
		$T_Number=trim($_POST['train']);
		$seat=trim($_POST['seat']);
		@$db=new mysqli('localhost','logging','log','train');
		if(mysqli_connect_errno())
		{
			echo "<p>Error:Could not connect to database.<br />
			Please try again later.</p>";
			exit;	
		}
		$query="delete from Cus_ticket where name=? and T_number=? and seat=?";
		$stmt=$db->prepare($query);
		$stmt->bind_param('sss',$name,$T_Number,$seat);
		$stmt->execute();
		if($stmt->affected_rows>0)
		{
			echo "<p>You have deleted it ".$name."</p>";
		}
		else
		{
			echo "<p>An error has occured.<br />
			The ticket was not deleted</p>";
		}
		$db->close();
	?>
</body>
</html>
