<?php
//getunm
//showuser
//shu
//deluser
//edituser
//ed_fld
//delu2
//chpwd
//getkbd


define("FILE_DATA",    "mud.dat");
define("FILE_NOLOGIN", "nologin");

/*
 *	Check we are running on the correct host
 *	see the notes about the use of flock();
 *	and the affects of lockf();
 */
function checkHost()
{
	//gethostname(user,33);
	//return !strcmp(user,HOST_MACHINE);

	return true;
}

/*
 *	Check if there is a no logins file active
 */
function checkNologin()
{
	if(!file_exists(FILE_NOLOGIN)) return false;

    return join("\n", file(FILE_NOLOGIN));
}

function showFile($filename)
{
	if(file_exists($filename))
		$f = file($filename);
	else
		$f = array(sprintf("[Cannot Find -> %s]\n",$name));

	$text = "";
	foreach($f as $s)
	{
		$text .= sprintf("<p>%s</p>", $s);
	}
	return $text;
}

function loadData()
{
	if(!file_exists(FILE_DATA)) return false;
	//"<p>AberMUD has yet to ever start!!!</p>\n"

	$f = file(FILEDATA);

	return array(
		'start' => $f[0],
	);
}

function getShortTime($time)
{
    return date("d.m.y H:i:s", $time);
}

/*
 *	Elapsed time and similar goodies
 */
function getFullTime($time)
{
	$now     = time();
	$elapsed = $now - $time;

	if($elapsed > 24*60*60)
	{
		return "Game time elapsed: Over a day!!!";
	}

	$text    = "";
	$hours   = $elapsed/3600;
	$minutes = ($elapsed/60) % 60;
	$seconds = $elapsed % 60;

	if($hours >= 1)
	{
		if($hours < 2)
			$text .= "1 hour";
		else
			$text .= sprintf("%d hours", $hours);
	}

	if($minutes >= 1)
	{
		if($text) $text .= " and ";

		if($minutes < 2)
			$text .= "1 minute";
		else
			$text .= sprintf("%d minutes", $minutes);
	}

	if($seconds >= 1)
	{
		if($text) $text .= " and ";

		if($seconds < 2)
			$text .= "1 second";
		else
			$text .= sprintf("%d seconds", $seconds);
	}


    return sprintf("Game time elapsed: %s", $text);
}

function actionLogin()
{
	global $_POST, $_SESSION;

    $username  = $_POST['username'];
	$user_data = new User($username);
	$errors    = $user_data->errors;

	if(!$errors)
	{
		$_SESSION['user'] = $user_data;
	}

	return array(
		'view'   => "name.html",
		'text'   => "",
		'errors' => $errors,
	);
}

function actionMotd()
{
	return array(
		'view'   => "motd.html",
		'text'   => showFile("text/gmotd2"),
		'errors' => array(),
	);
}

function actionLogout($errors)
{
	global $_SESSION;

	$exit_text = "Bye Bye";

	print_r($errors);

	unset($_SESSION['user']);

	return array(
		'view'   => "quit.html",
		'text'   => $exit_text,
		'errors' => array(),
	);
}

function actionTalker()
{
	/*
long isawiz;
char z[60];
x1:
if(qnmrq) if(execl(EXE,"   --}----- ABERMUD -----{--    Playing as ",nam,0)==-1)
{
	crapup("mud.exe : Not found\n");
}
cls();
printf("Welcome To AberMUD II [Unix]\n\n\n");
printf("Options\n\n");
printf("1]  Enter The Game\n");
printf("2]  Change Password\n");
printf("\n\n0] Exit AberMUD\n");
printf("\n\n");
isawiz=0;
cuserid(z);
if((!strcmp(z,"wisner"))||(!strcmp(z,"wisner")))
{
printf("4] Run TEST game\n");
printf("A] Show persona\n");
printf("B] Edit persona\n"); 
printf("C] Delete persona\n");
isawiz=1;
}
printf("\n\n");
printf("Select > ");
l2:getkbd(z,2);
lowercase(z);
switch(z[0])
{
case'1':
cls();
printf("The Hallway\n");
printf("You stand in a long dark hallway, which echoes to the tread of your\n");
printf("booted feet. You stride on down the hall, choose your masque and enter the\n");
printf("worlds beyond the known......\n\n");
execl(EXE,"   --{----- ABERMUD -----}--      Playing as ",nam,0);
crapup("mud.exe: Not Found\n");
case '2':chpwd(nam);break;
case '0':exit(0);
case '4':if(isawiz) 
{
cls();
printf("Entering Test Version\n");
}
break;
case 'a':if(isawiz) showuser();break;
case 'b':if(isawiz) edituser();break;
case 'c':if(isawiz) deluser();break;
default:printf("Bad Option\n");
}
goto x1;	
	*/
}

session_start();
$user_data = $_SESSION['user'];
$page_data = $_GET['page'];

$errors = array();

/**/
$b[0]=0;
$b[1]=0;
$b[2]=0;
$num = 0;
/**/

$view_file = "mainmenu.html";    
$mud_data  = array();
$timestart = 0;
$username  = "";

if(!checkHost())   $errors[] = "AberMUD is only available on {{HOST_MACHINE}}, not on {{user}}";

$nologin  = checkNologin();
if($nologin) $errors[] = $nologin;

$mud_data = loadData();

$timestart   = getShortTime($mud_data['start']);
$timeelapsed = getFullTime( $mud_data['start']);
$view_file   = "splash.html";    

/**/
$qnmrq  = 1;
$ttyt   = 0;
/**/

if($errors)
	$page_data = "logout";

if($page_data == "login")
{
	$data = actionLogin();
}
elseif($page_data == "motd")
{
	$data = actionMotd();
}
else
{
	if($user_data)
	{
		//syslog("Game entry by %s : UID %s",$user,$user_id); // Log entry
		$data = actionTalker();
	}
}

if($data['errors']) 
	$page_data = "logout";

if($page_data == "logout")
{
	$data = actionLogout($errors);
	unset($user_data);
}

$view_file = $data['view'];
$text      = $data['text'];
include($view_file);