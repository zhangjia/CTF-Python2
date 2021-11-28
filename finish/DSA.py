from Crypto.Hash import SHA
import gmpy2
y = int("45bb18f60eb051f9d48218df8cd956330a4ff30af5344f6c9540061d5383292d95c4dfc8ac26ca452e170dc79be15cc6159e037bccf564ef361c18c99e8aeb0bc1acf9c0c35d620d60bb7311f1cf08cfbc34ccaa79ef1dad8a7a6facce86659006d4faf057716857ec7ca604ade2c3d731d6d02f933198d390c3efc3f3ff046f", 16)
p = int("00c0596c3b5e933d3378be3626be315ee70ca6b5b11a519b5523d40e5ba74566e22cc88bfec56aad66918b9b30ad281388f0bbc6b8026b7c8026e91184bee0c8ad10ccf296becfe50505383cb4a954b37cb588672f7c0957b6fdf2fa0538fdad83934a45e4f99d38de57c08a24d00d1cc5d5fbdb73291cd10ce7576890b6ba089b", 16)
q = int("00868f78b8c8500bebf67a58e33c1f539d3570d1bd", 16)
g = int("4cd5e6b66a6eb7e92794e3611f4153cb11af5a08d9d4f8a3f250037291ba5fff3c29a8c37bc4ee5f98ec17f418bc7161016c94c84902e4003a7987f0d8cf6a61c13afd5673caa5fb411508cdb3501bdff73e747925f76586f4079fea12098b3450844a2a9e5d0a99bd865e0570d5197df4a1c9b8018fb99cdce9157b98500179", 16)
f3 = open(r"packet3/message3", 'r')
f4 = open(r"packet4/message4", 'r')
data3 = f3.read()
data4 = f4.read()
sha = SHA.new()
sha.update(data3)
m3 = int(sha.hexdigest(), 16)
sha = SHA.new()
sha.update(data4)
m4 = int(sha.hexdigest(), 16)
print m3, m4
s3 = 0x30EB88E6A4BFB1B16728A974210AE4E41B42677D
s4 = 0x5E10DED084203CCBCEC3356A2CA02FF318FD4123
r = 0x5090DA81FEDE048D706D80E0AC47701E5A9EF1CC
ds = s4 - s3
dm = m4 - m3
k = gmpy2.mul(dm, gmpy2.invert(ds, q))
k = gmpy2.f_mod(k, q)
tmp = gmpy2.mul(k, s3) - m3
x = tmp * gmpy2.invert(r, q)
x = gmpy2.f_mod(x, q)
print int(x)