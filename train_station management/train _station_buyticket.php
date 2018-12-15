<!DOCTYPE html>
<html>
<head>
	<title>buy tickets</title>
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
		//echo $T_Number;
		$seat=trim($_POST['seat']);
		@$db=new mysqli('localhost','logging','log','train');
		if(mysqli_connect_errno())
		{
			echo "<p>Error:Could not connect to database.<br />
			Please try again later.</p>";
			exit;	
		}
		
		//查看是否有该车次
		$query="select therest,launchtime from Tinfo where number=?";
		$stmt=$db->prepare($query);
		$stmt->bind_Param('s',$T_Number);
		$stmt->execute();
		$stmt->store_result();
		$stmt->bind_result($therest,$launchtime);
		if($stmt->affected_rows==0)
		{
			echo "<p>No this train! </p>";
			exit;
		}
		else
		{
			$stmt->fetch();
			$rest=$therest;
			//查看座位是否有余量
			if ($rest==0)
			{
				echo "<p>No rest seats</p>";
				echo $rest;
				exit;
			}
			else
			{
				//更新车次信息
				$rest=$rest-1;
				//echo $rest;
				$query="update Tinfo set therest=? where number=?";
				$stmt=$db->prepare($query);
				$stmt->bind_param('ds',$rest,$T_Number);
				$stmt->execute();
				//更新车票信息
				$query="insert into Cus_ticket(name,T_Number,seat,flag) values(?,?,?,1)";
				$stmt=$db->prepare($query);
				$stmt->bind_param('sss',$name,$T_Number,$seat);
				$stmt->execute();
				if($stmt->affected_rows>0)
				{
					$stmt->fetch();
					echo "<p>Congratulations on your successful purchase! ".$name."</p>";
					echo "<h4>Your ticket</h4>
					Train:&nbsp&nbsp&nbsp&nbsp".$T_Number."<br />
					Seat:&nbsp&nbsp&nbsp&nbsp".$seat."<br />
					launch time:&nbsp&nbsp&nbsp&nbsp".$launchtime."</p>";
					echo "<a href=\"AfterLogin.html\">Back to homepage</a>";
				}
				else
				{
					echo "<p>An error has occured.<br />
					The ticket was not sold.</p>";
				}
			}
		}
		$db->close();
	?>
</body>
</html>
