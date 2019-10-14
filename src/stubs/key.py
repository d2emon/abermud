"""
Key drivers
"""
global_state = {
    'key_buff': "",
}


need_reprint = False
last_prompt = ''


def key_input(state, prompt, max_length):
    global last_prompt, need_reprint
    need_reprint = True
    last_prompt = prompt
    state = state['bprintf'](state, prompt)
    state = {
        **state['pbfr'](state),
        'pr_due': False,
        'key_buff': input()[:max_length],
    }
    need_reprint = False
    return state


def key_reprint(state):
    state = state['pbfr']({
        **state,
        'pr_qcr': True,
    })
    if state['pr_due'] and need_reprint:
        print("\n{}{}".format(last_prompt, state['key_buff']))
    return {
        **state,
        'pr_due': False,
    }
