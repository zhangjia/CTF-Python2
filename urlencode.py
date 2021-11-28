import urllib

print(urllib.parse.quote("flag{url_encode_1234_!@#$}"))
d = {'name': 'bibi@flappypig.club', 'flag': 'flag{url_encode_1234_!@#$}'}
print(urllib.parse.urlencode(d))
