import shelve


def checkUser(ip, shelfName):
    s = shelve.open(shelfName)
    userStored = False

    if ip in s:
        userStored = True
    else:
        userStored = False

    s.close()

    return userStored    


def createNewUser(ip, name, shelfName):
    s = shelve.open(shelfName)
    s[ip] = name
    s.close()

    return checkUser(ip, shelfName)


def getUserName(ip, shelfName):
    s = shelve.open(shelfName)
    name = s[ip]
    s.close()

    return name