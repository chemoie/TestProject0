
def get_file(a,b):
    with open('./app/static/test.txt', 'w',encoding='utf8') as handle:
        handle.write(a)
        handle.write(b)
    return 'test.txt'

