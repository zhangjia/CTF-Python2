def shift_encrypt(m, k):
    l = len(k)
    c = ""
    for i in range(0, len(m), l):
        tmp_c = [""] * l
        if i + l > len(m):
            tmp_m = m[i:]
        else:
            tmp_m = m[i:i + l]
        for kindex in range(len(tmp_m)):
            tmp_c[int(k[kindex]) - 1] = tmp_m[kindex]
        c += "".join(tmp_c)
    return c


#
#
# m = "flag{easy_easy_crypto}"
# k = "3124"
# print(shift_encrypt(m, k))
#


def shift_decrypt(c, k):
    l = len(k)
    m = ""
    for i in range(0, len(c), l):
        tmp_m = [""] * l
        if i + l >= len(c):
            tmp_c = c[i:]
            use = []
            for kindex in range(len(tmp_c)):
                use.append(int(k[kindex]) - 1)
            use.sort()
            for kindex in range(len(tmp_c)):
                tmp_m[kindex] = tmp_c[use.index(int(k[kindex]) - 1)]
        else:
            tmp_c = c[i:i + l]
            for kindex in range(len(tmp_c)):
                tmp_m[kindex] = tmp_c[int(k[kindex]) - 1]
        m += "".join(tmp_m)
    return m


c = "lafgea{s_eyay_scyprt}o"
k = "3124"
print(shift_decrypt(c, k))
