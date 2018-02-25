def set_default(name):
    open('set.txt', 'w').close()
    file = open("set.txt", 'w')
    name_s = name.lower()
    file.write(name_s)


def get_default():
    file = open("set.txt", 'r')
    city = file.read()
    return city