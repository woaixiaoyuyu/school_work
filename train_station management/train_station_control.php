<!DOCTYPE html>
<html>
<head>
	<title>Control System</title>
</head>
<body>
	<h1>Train Control System</h1>
	<?php
		$changetype=$_POST['changetype'];
		$changeterm=trim($_POST['changeterm']); //trim移除字符串两侧的字符
		$T_number=trim($_POST['T_number']); //trim移除字符串两侧的字符
		if(!$changetype||!$changeterm)
		{
			echo '<p>You have not entered change details.<br />
			Please go back ang try again.</p>';
			exit;
		}
		switch($changetype)  //检查并过滤输入数据
		{
			case 'number':
			case 'start':
			case 'terminal':
			case 'launchtime':
			case 'arrivetime':
				break;
			default:
			echo '<p>That is not a vaild search type.<br />
			Please go back and try again.</p>';
			exit;
		}
		$db =new mysqli('localhost','logging','log','train');   //连接对应的数据库
		if (mysqli_connect_errno())     //判断是否连接成功
		{
			echo '<p>ERROR: Could not connect to database.<br />
			Please try again later.</p>';
			exit;
		}
		//判断是否有该车辆
		$query="select therest from Tinfo where number=?";
		$stmt=$db->prepare($query);
		$stmt->bind_param('s',$T_number);
		$stmt->execute();
		$stmt->store_result();
		$stmt->bind_result($therest);
		
		if($stmt->affected_rows>0)
		{
			//echo "$T_number";
			//echo "$changetype";
			//echo "$changeterm";
			$query="update Tinfo set ?=? where number=?";//防止SQL注入,用?代替'$changeterm'
			$stmt=$db->prepare($query); //构造一个statement
			$stmt->bind_Param('sss',$changetype,$changeterm,$T_number); //告诉PHP用什么变量代替?，格式是字符串
			$stmt->execute(); //运行该查询
			//$stmt->store_result();
			//$stmt->bind_result($therest);
			//$stmt->fetch();
			if($stmt->affected_rows>0)
			{
				echo "$T_number: $changetype has changed to $changeterm";
			}
			else
			{
				echo "something errors happened";
			}
		}
		else
		{
			echo "<p>No this train! </p>";
			exit;
		}
		echo "<a href=\"AfterLogin.html\">Back to homepage</a>";
		$db->close(); //关闭数据库连接
	?>
</body>
</html>
