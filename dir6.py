c = 'A'
while c <= 'Z':
    path = r"/Users/kasymhan2005/Documents/PP2/" + c + ".txt"
    f = open(path, "w")
    f.close()
    c = chr(ord(c) + 1)

    #ord - символ в аски код, кхр из аски в символ