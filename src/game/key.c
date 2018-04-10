/*  Key drivers */

#include <stdio.h>
/*#include <sgtty.h>*/
#include <termios.h>

long save_flag= -1;
char key_buff[256];
char pr_bf[32];
long key_mode= -1;

key_reprint()
{
	extern long pr_due;
	extern long pr_qcr;
	pr_qcr=1;
	pbfr();
	if((key_mode==0)&&(pr_due))
		printf("\n%s%s",pr_bf,key_buff);
	pr_due=0;
	fflush(stdout);
}

