<!DOCTYPE html>
<html>
<head>
	<title>Train info</title>
</head>
<body>
	<h1>Train information</h1>
	<?php
		$db =new mysqli('localhost','logging','log','train');
		if(mysqli_connect_errno())
		{
			echo "<p>Error: Could not connect to database.<br />
			Please try again later.<br />";
			exit;
		}
		$query="select * from Tinfo";
		$stmt=$db->prepare($query);
		$stmt->execute();
		$stmt->store_result();
		$stmt->bind_result($number,$start,$terminal,$launchtime,$arrivetime,$price,$therest,$total);
		if($stmt->num_rows==0)
		{
			echo "Sorry, there are some errors";
			exit;
		}
		else
		{
			while($stmt->fetch())
			{
				echo "<p><strong>number: ".$number."</strong>";
				echo "<br />start: ".$start;
				echo "<br />terminal: ".$terminal;
				echo "<br />launchtime: ".$launchtime;
				echo "<br />arrivetime: ".$arrivetime;
				echo "<br />price: ".$price;
				echo "<br />rest: ".$therest;
				echo "<br />total: ".$total."</p>";
			}
		}
		$stmt->free_result(); //释放结果集
		echo "<a href=\"AfterLogin.html\">Back to homepage</a>";
		$db->close(); //关闭数据库连接
	?>
</body>
</html>
