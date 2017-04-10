def main(title='', user=None, id=0):
    from config import CONFIG
    print(CONFIG['EXE'])
    print({
        'title': title,
        'user': user,
        'id': id,
    })
    return 0
