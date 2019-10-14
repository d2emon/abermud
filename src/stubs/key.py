"""
Key drivers
"""
global_state = {
    'key_buff': "",
}


MODE_0 = 0
MODE_1 = -1

pr_bf = ""
key_mode = MODE_1


def key_input(ppt, len_max):
    """
   char x;
   extern long pr_due;
   int len_cur=0;
   key_mode=0;
   strcpy(pr_bf,ppt);
   bprintf("%s",ppt);
   pbfr();
   pr_due=0;
   strcpy(key_buff,"");
   while(len_cur<len_max)
   {
   	x=getchar();
   	if(x=='\n')
   	{
   		printf("\n");
   		key_mode= -1;
    		return;
   	}
   	if(((x==8)||(x==127))&&(len_cur))
	{
		putchar(8);
		putchar(' ');
		putchar(8);
		len_cur--;
		key_buff[len_cur]=0;
		continue;
	}
	if(x<32) continue;
	if(x==127) continue;
	putchar(x);
	key_buff[len_cur++]=x;
	key_buff[len_cur]=0;
     }
    """


def key_reprint(state):
    state = state['pbfr']({
        **state,
        'pr_qcr': True,
    })
    if key_mode == MODE_0 and state['pr_due']:
        print("\n{}{}".format(pr_bf, state['key_buff']))
    return {
        **state,
        'pr_due': False,
    }
