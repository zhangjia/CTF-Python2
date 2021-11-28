def c01248_decode(c):
    l = c.split("0")
    origin = "abcdefghijklmnopqrstuvwxyz"
    r = ""
    for i in l:
        tmp = 0
        for num in i:
            tmp += int(num)
        r += origin[tmp - 1]
    return r


print(c01248_decode("8842101220480224404014224202480122"))
