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
		//查看该车票是否已购买
		$query="delete from Cus_ticket where name=? and T_number=? and seat=?";
		$stmt=$db->prepare($query);
		$stmt->bind_param('sss',$name,$T_Number,$seat);
		$stmt->execute();
		if($stmt->affected_rows>0)
		{
			//将车次的空闲车票数+1
			$query="select therest from Tinfo where number=?";
			$stmt=$db->prepare($query);
			$stmt->bind_param('s',$T_Number);
			$stmt->execute();
			$stmt->store_result();
			$stmt->bind_result($therest);
			$stmt->fetch();
			$rest=$therest+1;
			$query="update Tinfo set therest=? where number=?";
			$stmt=$db->prepare($query);
			$stmt->bind_param('ds',$rest,$T_Number);
			$stmt->execute();
			//将车票号添加到空闲车票中
			$query="insert into k_ticket (number,seat)values(?,?)";
			$stmt=$db->prepare($query);
			$stmt->bind_param('ss',$T_Number,$seat);
			$stmt->execute();
			//删除成功
			echo "<p>You have deleted it ".$name."</p>";
		}
		else
		{
			echo "<p>An error has occured.<br />
			The ticket was not deleted</p>";
		}
		echo "<a href=\"AfterLogin.html\">Back to homepage</a>";
		$db->close();
	?>
</body>
</html>
