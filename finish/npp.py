n = 19402643768027967294480695361037227649637514561280461352708420192197328993512710852087871986349184383442031544945263966477446685587168025154775060178782897097993949800845903218890975275725416699258462920097986424936088541112790958875211336188249107280753661467619511079649070248659536282267267928669265252935184448638997877593781930103866416949585686541509642494048554242004100863315220430074997145531929128200885758274037875349539018669336263469803277281048657198114844413236754680549874472753528866434686048799833381542018876362229842605213500869709361657000044182573308825550237999139442040422107931857506897810951
npp = 19402643768027967294480695361037227649637514561280461352708420192197328993512710852087871986349184383442031544945263966477446685587168025154775060178782897097993949800845903218890975275725416699258462920097986424936088541112790958875211336188249107280753661467619511079649070248659536282267267928669265252935757418867172314593546678104100129027339256068940987412816779744339994971665109555680401467324487397541852486805770300895063315083965445098467966738905392320963293379345531703349669197397492241574949069875012089172754014231783160960425531160246267389657034543342990940680603153790486530477470655757947009682859
e = 65537

pq = n
paq = (npp - n - 4) / 2
import gmpy2

gn1 = gmpy2.mpz(n)
gn2 = gmpy2.mpz(npp)
a = gmpy2.mpz(1)
b = gmpy2.mpz(-paq)
c = gmpy2.mpz(n)
i = gmpy2.mpz(gmpy2.iroot(b * b - 4 * a * c, 2)[0])
x1 = (-b - i) / 2
x2 = (-b + i) / 2
print x1 * x2 - n
p1 = x1
q1 = x2
p2 = x1 + 2
q2 = x2 + 2

print p1
print p2
print q1
print q2

from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, isPrime
import primefac


def modinv(a, n):
    return primefac.modinv(a, n) % n


c = 7991219189591014572196623817385737879027208108469800802629706564258508626010674513875496029177290575819650366802730803283761137036255380767766538866086463895539973594615882321974738140931689333873106124459849322556754579010062541988138211176574621668101228531769828358289973150393343109948611583609219420213530834364837438730411379305046156670015024547263019932288989808228091601206948741304222197779808592738075111024678982273856922586615415238555211148847427589678238745186253649783665607928382002868111278077054871294837923189536714235044041993541158402943372188779797996711792610439969105993917373651847337638929
d2 = modinv(65537, (p2 - 1) * (q2 - 1))
m2 = pow(c, d2, npp)
d1 = modinv(65537, (p1 - 1) * (q1 - 1))
m1 = pow(m2, d1, n)
print long_to_bytes(m1)
