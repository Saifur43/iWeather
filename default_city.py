def set_default(name):
    open('set.txt', 'w').close()
    file = open("set.txt", 'w')
    file.write(name)


def get_default():
    file = open("set.txt", 'r')
    city = file.read()
    return city