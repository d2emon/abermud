def main(title='', user=None):
    from config import CONFIG
    print(CONFIG['EXE'])
    print({
        'title': title,
        'user': user,
    })
    return 0
