def gen_cheese_map(k, use_Q=True, upper=True):
    k = k.upper()
    k0 = ""
    origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in k:
        if i not in k0:
            k0 += i
    for i in origin:
        if i not in k0:
            k0 += i
    if use_Q == True:
        k0 = k0[0:k0.index("J")] + k0[k0.index("J") + 1:]
    else:
        k0 = k0[0:k0.index("Q")] + k0[k0.index("Q") + 1:]
    if upper == False:
        k0 = k0.lower()
    assert len(k0) == 25
    r = []
    for i in range(5):
        r.append(k0[i * 5:i * 5 + 5])
    return r


def _playfair_2char(tmp, map):
    for i in range(5):
        for j in range(5):
            if tmp[i][j] == tmp[0]:
                ai = i
                aj = j
            if tmp[i][j] == tmp[1]:
                bi = i
                bj = j
    if ai == bi:
        axi = ai
        bxi = bi
        axj = (aj + 1) % 5
        bxj = (bj + 1) % 5
    elif aj == bj:
        axj = aj
        bxj = bj
        axi = (ai + 1) % 5
        bxi = (bi + 1) % 5
    else:
        axi = ai
        axj = bj
        bxi = bi
        bxj = bj
    return map[axi][axj] + map[bxi][bxj]


def playfair_encode(m, k="", cheese_map=[]):
    m = m.upper()
    origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tmp = ""
    for i in m:
        if i in origin:
            tmp += i
    m = tmp
    assert k != "" or cheese_map != []
    if cheese_map == []:
        map = gen_cheese_map(k)
    else:
        map = cheese_map
    m0 = []
    idx = 0
    while idx < len(m):
        tmp = m[idx:idx + 2]
        if tmp[0] != tmp[1]:
            m0.append(tmp)
            idx += 2
        elif tmp[0] != "X":
            m0.append(tmp[0] + 'X')
            idx += 1
        else:
            m0.append(tmp[0] + 'Q')
            idx += 1
        if idx == len(m) - 1:
            if tmp[0] != "X":
                m0.append(tmp[0] + 'X')
                idx += 1
            else:
                m0.append(tmp[0] + 'Q')
                idx += 1
    r = []
    for i in m0:
        r.append(_playfair_2char(i, map))
    return r


print(playfair_encode("Hide the gold in the tree stump", "playfairexample"))
