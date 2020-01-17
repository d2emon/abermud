import logging
from ..tk import Player, talker
from .error import on_error
from .user import User


def main(game_user, program_name, username):
    print("Entering Game ....")
    player = Player(username)
    print("Hello {}".format(player.name))
    logging.info("GAME ENTRY: %s[%s]", player.name, game_user.user_id)

    return talker(player)


"""
listfl(name)
char *name;
{
FILE *a;
char b[128];
a=Service.lock(name,"r+");
while(fgets(b,128,a)) printf("%s\n",b);
a.unlock()
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
