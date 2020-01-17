import logging
from ..tk import get_name, set_name
from .error import on_error
from .user import User


def talker(name):
    raise NotImplementedError()


def main(game_user, program_name, username):
    print("Entering Game ....")
    if username == "Phantom":
        name = "The {}".format(username)
    else:
        name = username
    set_name(name)

    print("Hello {}".format(get_name()))
    logging.info("GAME ENTRY: %s[%s]", get_name(), game_user.user_id)

    return talker(get_name())


"""
listfl(name)
char *name;
{
FILE *a;
char b[128];
a=openlock(name,"r+");
while(fgets(b,128,a)) printf("%s\n",b);
fcloselock(a);
}

char *getkbd(s,l)   /* Getstr() with length limit and filter ctrl */
 char *s;
 int l;
    {
    char c,f,n;
    f=0;c=0;
    while(c<l)
       {
       regec:n=getchar();
       if ((n<' ')&&(n!='\n')) goto regec;
       if (n=='\n') {s[c]=0;f=1;c=l-1;}
       else
          s[c]=n;
       c++;
       }
    if (f==0) {s[c]=0;while(getchar()!='\n');}
    return(s);
    }
"""


"""
set_progname(n,text)
char *text;
{
	/*
	int x=0;
	int y=strlen(argv_p[n])+strlen(argv_p[1]);  
	y++;
	if(strcmp(argv_p[n],text)==0) return;

	while(x<y)
	   argv_p[n][x++]=0; 
	strcpy(argv_p[n],text);
	*/
}
"""
