<?php
	$name=trim($_POST['name']);
	$password=trim($_POST['password']);
	//echo "$name";
?>
<!DOCTYPE html>
<html>
<head>
	<title>Loging</title>
</head>
<body>
	<h1>Loging</h1>
	<?php
		$db =new mysqli('localhost','logging','log','train');
		if(mysqli_connect_errno())
		{
			echo "<p>Error: Could not connect to database.<br />
			Please try again later.<br />";
			exit;
		}
		if(!$name||!$password)
		{
			echo "<p>Please input your name and password<br /></p>";
		}
		$query="select * from train_log where Name=?";
		$stmt=$db->prepare($query);
		$stmt->bind_param('s',$name);
		$stmt->execute();
		$stmt->store_result();
		$stmt->bind_result($ID,$Name,$password,$phone);
		if($stmt->num_rows==0)
		{
			echo "<p>Please register first</p>";
			exit;
		}
		else
		{
			$query="select Password from train_log where Name=?";
			$stmt=$db->prepare($query);
			$stmt->bind_param('s',$name);
			$stmt->execute();
			$stmt->store_result();
			$stmt->bind_result($hash);
			if($stmt->num_rows==0||password_verify($password,$hash))
			{
				echo "<p>Wrong password!<br />
				Try again.</p>";
				exit;
			}
			else
			{
				//跳转到下一级界面
				header("Location: http://localhost:81//train_station//AfterLogin.html");
			}
		}
		$stmt->free_result(); //释放结果集
		$db->close(); //关闭数据库连接
	?>
</body>
</html>
