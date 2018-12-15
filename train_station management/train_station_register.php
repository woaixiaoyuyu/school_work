<?php
	$name=trim($_POST['name']);
	$password=trim($_POST['password']);
	$s_pass=trim($_POST['s_pass']);
	$phone=trim($_POST['phone']);
	//echo "$name";
	if($password!=$s_pass)
	{
		echo htmlspecialchars("please input the same password to register");
		exit;
	}
	@$db =new mysqli('localhost','logging','log','train');
	if(mysqli_connect_errno())
	{
		echo "Error: Could not connect to database.<br />
		Please try again later.<br />";
		exit;
	}
	$hash=password_hash($password,PASSWORD_DEFAULT);
	$query="insert into train_log (Name,Password,Phone_number)values(?,?,?)";
	$stmt=$db->prepare($query);
	$stmt->bind_param('sss',$name,$hash,$phone);
	$stmt->execute();
	if($stmt->affected_rows>0)
	{
		echo "<p>Inserted into the database.</p>";
	}
	else
	{
		echo "<p>An error has occured.<br />
		The item was not added.</p>";
	}
	$db->close();
?>
