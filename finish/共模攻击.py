from Crypto.Util.number import long_to_bytes

from finish.all import  same_n_sttack

n1=21660190931013270559487983141966347279666044468572000325628282578595119101840917794617733535995976710097702806131277006786522442555607842485975616689297559583352413160087163656851019769465637856967511819803473940154712516380580146620018921406354668604523723340895843009899397618067679200188650754096242296166060735958270930743173912010852467114047301529983496669250671342730804149428700280401481421735184899965468191802844285699985370238528163505674350380528600143880619512293622576854525700785474101747293316814980311297382429844950643977825771268757304088259531258222093667847468898823367251824316888563269155865061
e1=65537
c1=11623242520063564721509699039034210329314238234068836130756457335142671659158578379060500554276831657322012285562047706736377103534543565179660863796496071187533860896148153856845638989384429658963134915230898572173720454271369543435708994457280819363318783413033774014447450648051500214508699056865320506104733203716242071136228269326451412159760818676814129428252523248822316633339393821052614033884661649376604245744651142959498917235138077366818109892738298251161767344501687113868331134288984466294415889635863660753717476594011236542159800099371872396181448655448842148998667568104710807411358117939831241620315

n2=21660190931013270559487983141966347279666044468572000325628282578595119101840917794617733535995976710097702806131277006786522442555607842485975616689297559583352413160087163656851019769465637856967511819803473940154712516380580146620018921406354668604523723340895843009899397618067679200188650754096242296166060735958270930743173912010852467114047301529983496669250671342730804149428700280401481421735184899965468191802844285699985370238528163505674350380528600143880619512293622576854525700785474101747293316814980311297382429844950643977825771268757304088259531258222093667847468898823367251824316888563269155865061
e2=70001
c2=8180690717251057689732022736872836938270075717486355807317876695012318283159440935866297644561407238807004565510263413544530421072353735781284166685919420305808123063907272925594909852212249704923889776430284878600408776341129645414000647100303326242514023325498519509077311907161849407990649396330146146728447312754091670139159346316264091798623764434932753276554781692238428057951593104821823029665203821775755835076337570281155689527215367647821372680421305939449511621244288104229290161484649056505784641486376741409443450331991557221540050574024894427139331416236263783977068315294198184169154352536388685040531
print(long_to_bytes(same_n_sttack(n1,e1,e2,c1,c2)))