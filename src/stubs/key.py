"""
Key drivers
"""
# State
global_state = {
    'key_buff': "",
}


need_reprint = False
last_prompt = ''


# Mutations
def set_key_buff(state, key_buff):
    state.update({
        'is_clean': True,
        'key_buff': key_buff,
    })
    return state


# Actions
def key_input(state, prompt, max_length):
    global last_prompt, need_reprint
    last_prompt = prompt
    state = state['bprintf'](state, prompt)
    state = state['pbfr'](state)
    state = set_key_buff(state, input()[:max_length])
    return state


def key_reprint(state):
    state = state['pbfr']({
        **state,
        'pr_qcr': True,
    })
    if state['is_clean']:
        print("\n{}{}".format(last_prompt, state['key_buff']))
    return {
        **state,
        'pr_due': False,
    }
