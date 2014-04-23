<?php
define("ERROR_BANNED", 1);
define("ERROR_LOGIN",  2);
define("ERROR_NOFILE", 3);

class User
{
	var $name;
	var $errors = array();

	function User($name)
	{
		$this->name = $name;

		/*
		 * Check if banned first
		 */    
		if($this->isBanned())
		{
       		$errors[] = ERROR_BANNED;
		}
		else
		{
			/*
			 * Check for legality of names
			 */
			if(!$this->checkName())
			{
				$errors[] = ERROR_LOGIN;
			}
			else
			{
			    $user = $this->find();

			    /* Password checking */
			    if($user)
			    {
			    	$this->checkPassword();
			    }
			    else
			    {
			    	$this->newPassword();
			    }
			}
		}
	}

	function getError($errorcode)
	{
		if($errorcode == ERROR_BANNED)
			return "I'm sorry- that userid has been banned from the Game";
		elseif($errorcode == ERROR_LOGIN)
			return "Illegal characters in user name";
		elseif($errorcode == ERROR_NOFILE)
			return "No persona file";
	}
	
	function isBanned()
	{
   		$name = strtolower($this->name);

    	$a = file("banned");
    	if(!$a) return false;
    	foreach($a as $b)
    	{
	    	$b = strtolower($b);
       		if($name == $b)
        		return true;
   		}
    	return false;
	}

	function checkName()
	{
		$name = strtolower($this->name);

		if(!$name) return false;
		foreach($name as $ch)
		{
			if($ch<'a') return false;
			if($ch>'z') return false;
		}
	    //if(!validname(usrnam)) return false;

		return true;
	}

	function find()
	{
	    $unit = false;
	    //$unit=openlock(PFL,"r");f=0;
	    if(!$unit)
	    {
	    	$errors[] = ERROR_NOFILE;
	    	return false;
	    } 

	    /*
	    foreach($unit as $block)
	    {
	       	$found = strtolower(dcrypt($block));
	       	$user  = strtolower($name);
	       	//scan(wkng,block,0,"",".");

	        if($wkng == $wk2)
	        	return $block;
	    }
	    */

	    return false;
	}

	/* this bit registers the new user */
	function newPassword()
	{
		    /*
			printf("Creating new persona...\n");
			printf("Give me a password for this persona\n");
			repass:
			printf("*");
			fflush(stdout);
		    gepass(block);
		    printf("\n");
		    if (any('.',block)!= -1)
	        {
	           	printf("Illegal character in password\n");
	           	goto repass;
	        }
		    if (!strlen(block)) goto repass;
		    strcpy(uid,pwd);
		    strcpy(pwd,block);
		    sprintf(block,"%s%s%s%s",uid,".",pwd,"....");
	  	    fl=openlock(PFL,"a");
		    if(fl==NULL) 
	 	    {
				exit_text("No persona file....\n");
			    return;
		    }
		    qcrypt(block,lump,strlen(block));
		    strcpy(block,lump);
		    fprintf(fl,"%s\n",block);
		    fclose(fl);
			*/
		
		return true;	
	}

	function checkPassword()
	{
	    // a=scan(uid,block,0,"",".");
	    // a=scan(pwd,block,a+1,"",".");
	    // tries=0;
	    // pastry:
	    // printf("\nThis persona already exists, what is the password ?\n*");
	    // $block = gepass();
	    /*
	    if ($block == $pwd)
	    {
	        if (tries<2)
	        {
	          	tries++;
	           	goto pastry;
	        }
	        else
	            crapup("\nNo!\n\n");
	    }
	    */
		
		return true;	
	}


}