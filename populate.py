# IMPORTS:
from datetime import date

from google.cloud.ndb import Client, Key, delete_multi

from models.db.game_night import GameNight, Vote
from models.db.user import User

# CLEAR DB:

with Client().context():

    delete_multi(User.query().fetch(keys_only=True))
    delete_multi(GameNight.query().fetch(keys_only=True))
    delete_multi(Vote.query().fetch(keys_only=True))

    # Persons:
    # Person(id=5629499534213120, userid=u'101546228613686788745', nickname=u'andre.okul', name=u'André', activated=True).put()
    #
    # Person(id=5651124426113024, userid=u'108028669467192825661', nickname=u'damidub1989', name=u'Damian', activated=True).put()
    #
    # Person(id=5659456662667264, userid=u'114614998739363880603', nickname=u'OThorvaldsen', name=u'Øivind', activated=True).put()
    #
    # Person(id=5723348596162560, userid=u'110679903128030931478', nickname=u'stian.soerebo', name=u'Stian', activated=True).put()
    #
    # Person(id=5724160613416960, userid=u'109962652513125112369', nickname=u'olejri', name=u'Ole', activated=True).put()


    # GameNights:
    GameNight(id=4657391668822016, date=date.fromtimestamp(1447372800), host=u'Damian', description=u'Toast m speke, laks, bringerbærsorbet, knightsquad. Dato usikker.', sum=3.5).put()

    GameNight(id=4798129157177344, date=date.fromtimestamp(1409702400), host=u'André', description=u'avokadobrødskiv, fattigmannstaco, eggedosis CIV 2.0', sum=3.41666666667).put()

    GameNight(id=4804625295212544, date=date.fromtimestamp(1422921600), host=u'Ole', description=u'noe med egg, pasta carbonera og pannacotta - tankspill', sum=4.04166666667).put()

    GameNight(id=4824175986343936, date=date.fromtimestamp(1415664000), host=u'Damian', description=u'Fylt sopp, baconsnurret indrefilet, rullekake + supermario', sum=3.25).put()

    GameNight(id=5073368378245120, date=date.fromtimestamp(1402358400), host=u'Ole', description=u'DOTA2 !!!!!!! rekeavokado, indrefil, \"smoodie\"', sum=3.33333333333).put()

    GameNight(id=5074692033478656, date=date.fromtimestamp(1544486400), host=u'Stian', description=u'Nybakt Focciacia Sandwich, Baccalao, Eplekake med karamell-Is m/krisp. Terraforming Mars Colonies', sum=4.5625).put()

    GameNight(id=5080816245800960, date=date.fromtimestamp(1661817600), host=u'Øivind', description=u'Amsterdam mix, Amsterdam burger, kake, 7 wonders', sum=4.25).put()

    GameNight(id=5081225274327040, date=date.fromtimestamp(1656374400), host=u'Ole', description=u'Øl chips i bil, havnerestaur, muffin, seiling', sum=4.5625).put()

    GameNight(id=5081456606969856, date=date.fromtimestamp(1399939200), host=u'Stian', description=u'Eggerøre into kjøttgryte into smoothie into castlecrush', sum=3.58333333333).put()

    GameNight(id=5085604337418240, date=date.fromtimestamp(1401148800), host=u'André', description=u'Baktpotet?? + Eget spill', sum=2.79166666667).put()

    GameNight(id=5091364022779904, date=date.fromtimestamp(1390262400), host=u'André', description=u'Civapancakes', sum=3.08333333333).put()

    GameNight(id=5122315436163072, date=date.fromtimestamp(1454457600), host=u'André', description=u'Nært og fjærnt. Sandw fra joe, rein, milkshake. ticket2ride', sum=3.875).put()

    GameNight(id=5129512190738432, date=date.fromtimestamp(1397520000), host=u'Ole', description=u'Bruschetta, HOTHOTikka, splittasjokkoBAN + magic', sum=3.95833333333).put()

    GameNight(id=5142615859134464, date=date.fromtimestamp(1663632000), host=u'Damian', description=u'Rista brød + hjemmelaget eggesalat, pulled pork taco, lime pannacotta, 7 wounders', sum=4.5).put()

    GameNight(id=5149590550478848, date=date.fromtimestamp(1660608000), host=u'André', description=u'Joe and J, Skogsgryte, donoughts, 7wonders', sum=4.20833333333).put()

    GameNight(id=5162157834502144, date=date.fromtimestamp(1403568000), host=u'Damian', description=u'Tomat&mozarella, lasagn, milkshake, dominion', sum=3.91666666667).put()

    GameNight(id=5178081291534336, date=date.fromtimestamp(1412121600), host=u'Damian', description=u'baguett m speke, hjemmelaga pizza, smoothie', sum=3.375).put()

    GameNight(id=5361079110598656, date=date.fromtimestamp(1424131200), host=u'Damian', description=u'Italiensk omelett, calzone, panna repeat-cotta - diablocore', sum=4.0).put()

    GameNight(id=5367575248633856, date=date.fromtimestamp(1447286400), host=u'Ole', description=u'krabber, spekemat, kakerosa, mobilspill. Dato usikker.', sum=3.91666666667).put()

    GameNight(id=5382773795717120, date=date.fromtimestamp(1438560000), host=u'André', description=u'Tema nordland: Tørrfisk/skinke, møsbrøm, brownies, diablo', sum=3.375).put()

    GameNight(id=5387125939765248, date=date.fromtimestamp(1442880000), host=u'Ole', description=u'Chiliskampi, KinaKylling, Kokospudding, FIFA16', sum=3.58333333333).put()

    GameNight(id=5393792802750464, date=date.fromtimestamp(1441065600), host=u'Damian', description=u'Polish growup food: egg&majo, Svinekotletter m div, \"eplekake\" + idarb og worms', sum=4.54166666667).put()

    GameNight(id=5432688026583040, date=date.fromtimestamp(1439856000), host=u'Ole', description=u'avokado med reke, pizza, brødsmula i glass ', sum=3.625).put()

    GameNight(id=5631076886118400, date=date.fromtimestamp(1603152000), host=u'Øivind', description=u'Meny salat, nachos, kristina kake, superclub', sum=3.9375).put()

    GameNight(id=5631383682678784, date=date.fromtimestamp(1478563200), host=u'Stian', description=u'Trumpnight. Kyllingklubber, mac n cheese, Ch-IS-cake. Amerikaner og byggelópespill', sum=4.29166666667).put()

    GameNight(id=5631986051842048, date=date.fromtimestamp(1389225600), host=u'Stian', description=u'Lammebra tekken', sum=3.95833333333).put()

    GameNight(id=5632763172487168, date=date.fromtimestamp(1510012800), host=u'André', description=u'To sorter hjemmelaget potetgull, fransk biffgryte + dannelsesopplevelse, gulrotkake, dominion med adhd ole', sum=3.25).put()

    GameNight(id=5632908932939776, date=date.fromtimestamp(1467590400), host=u'Ole', description=u'Melon med skinke, reker, \"ostekake\", båttur', sum=3.79166666667).put()

    GameNight(id=5633226290757632, date=date.fromtimestamp(1542067200), host=u'Damian', description=u'Squash m fyll, hjemmelagd lasagne, brownies is og saus, settlers of catan', sum=4.0625).put()

    GameNight(id=5636026810761216, date=date.fromtimestamp(1481673600), host=u'Damian', description=u'Onion chees rings, burger, banansplit, cheatscreen & towerfall', sum=3.625).put()

    GameNight(id=5636139285217280, date=date.fromtimestamp(1511827200), host=u'Damian', description=u'Damian’s bruschetta, langtidskokt kremet oksegryte, cakepops + ticket to ride USA', sum=4.20833333333).put()

    GameNight(id=5636318331666432, date=date.fromtimestamp(1393891200), host=u'Stian', description=u'Vårrull, wok, bakst med bomberman + castle crush', sum=3.91666666667).put()

    GameNight(id=5636953047302144, date=date.fromtimestamp(1534204800), host=u'Damian', description=u'Guac + salmlaks, kjøttgryte, sjokocotta, terra', sum=4.46875).put()

    GameNight(id=5638346151821312, date=date.fromtimestamp(1653350400), host=u'Damian', description=u'Spekefat/lasagn/cakepops+is/7 wounders', sum=4.59375).put()

    GameNight(id=5639221461123072, date=date.fromtimestamp(1491782400), host=u'Ole', description=u'SCÆMPI, BIFF, KAKE OG IS, brettspill (evo og underworld)', sum=3.70833333333).put()

    GameNight(id=5639955095224320, date=date.fromtimestamp(1540944000), host=u'André', description=u'Kanelboller, pølsefest, dobbel pistasjis, jackbox 5', sum=3.5).put()

    GameNight(id=5642554087309312, date=date.fromtimestamp(1382227200), host=u'André', description=u'Gulasj Civverz', sum=2.5).put()

    GameNight(id=5642790067240960, date=date.fromtimestamp(1651536000), host=u'André', description=u'3 enheter øl+gt+øl, brochetta, suppe, is, 7 wonders', sum=4.15625).put()

    GameNight(id=5643440998055936, date=date.fromtimestamp(1524528000), host=u'André', description=u'Asparges og sopp, kylling, fruktsalat med multisupport, overcooked', sum=3.25).put()

    GameNight(id=5644378534051840, date=date.fromtimestamp(1552348800), host=u'Stian', description=u'Avolakstårn, 3pizza, limekake, smash', sum=4.3125).put()

    GameNight(id=5645937472962560, date=date.fromtimestamp(1551139200), host=u'Damian', description=u'Chillimarinert scampi + mangochutney, indisk gryte m nanbrød og dressing, is+jordbærsaus+sjokolade, worms+speedrunners', sum=3.83333333333).put()

    GameNight(id=5646862031781888, date=date.fromtimestamp(1552953600), host=u'Ole', description=u'Cheese havnen, Biff Fking perfect Wellington, holy chocolate. Dungeon and dragon\'s', sum=4.25).put()

    GameNight(id=5650665401483264, date=date.fromtimestamp(1525737600), host=u'Damian', description=u'Mango/rekesalat - torsk, bacon, ertepuré, ovnsbakte poteter og gulrot - pistasjeis og eplekake - clank!', sum=4.54166666667).put()

    GameNight(id=5651144718155776, date=date.fromtimestamp(1574121600), host=u'Damian', description=u'Wraps m smøreost - salat - kalkun - avocado, hjemmelaget pizza x 3 - brownies + is, Poker', sum=4.33333333333).put()

    GameNight(id=5652156384280576, date=date.fromtimestamp(1596499200), host=u'André', description=u'Drinks, hvitløksbrød, egenvalt middag på colonels, snikkers og mars is, sorcerer', sum=4.125).put()

    GameNight(id=5653294995210240, date=date.fromtimestamp(1537228800), host=u'Stian', description=u'Toast Chevre m/honningmandler, chilli og fruktøl // Poké Bowl m/biff og laks // Crepes m/is, blåbær og daim // Dead of Winter feat. Mario Pre party // Damian syk', sum=4.4375).put()

    GameNight(id=5654153720233984, date=date.fromtimestamp(1477958400), host=u'Damian', description=u'Nanbrød m dressing, butter chicken m nan, salat og ris, mango lassi, mortal combat x', sum=3.29166666667).put()

    GameNight(id=5655638436741120, date=date.fromtimestamp(1519689600), host=u'Øivind', description=u'Bacondadler, biff m. sprøstekte poteter og asparges, brownies m. is og Axis and Allies Europe', sum=4.04166666667).put()

    GameNight(id=5657058552578048, date=date.fromtimestamp(1576540800), host=u'Stian', description=u'Toast, biff, cheesecakepepperkake, speedterra', sum=4.375).put()

    GameNight(id=5657382461898752, date=date.fromtimestamp(1466380800), host=u'André', description=u'Melon, Bortelaga pizza, hjemmelaga gulrotkake med saklig mye glasur, AirConsole spill', sum=3.33333333333).put()

    GameNight(id=5657582312095744, date=date.fromtimestamp(1476144000), host=u'Ole', description=u'Løkringer, burger, hvitsjokomosse, coop dudes og fifa', sum=4.08333333333).put()

    GameNight(id=5667370274127872, date=date.fromtimestamp(1547510400), host=u'Øivind', description=u'Avokadobakte egg m. chorizo, Indrefilet av svin rullet i bacon m. ovnsbakte poteter toppet med ost ,Kvargpannacotta m. bær og hvit sjokolade, TERRA', sum=4.25).put()

    GameNight(id=5667908084563968, date=date.fromtimestamp(1479772800), host=u'André', description=u'Texasstyle, Jalapenos m ost n bacon, texas chiligryte, texas sjokoladekake, europa ticket to ride', sum=4.125).put()

    GameNight(id=5668600916475904, date=date.fromtimestamp(1383264000), host=u'Ole', description=u'Magic Burger', sum=3.625).put()

    GameNight(id=5671038738235392, date=date.fromtimestamp(1646697600), host=u'Øivind', description=u'Pizza, hotellspeedterra, sjokokake på hotell', sum=3.3125).put()

    GameNight(id=5671831268753408, date=date.fromtimestamp(1489449600), host=u'Stian', description=u'Smaksfull suppe med rek og skink, pulled pork sandw, sjokopanacotta, Cry Havoc', sum=4.04166666667).put()

    GameNight(id=5672749318012928, date=date.fromtimestamp(1391472000), host=u'Ole', description=u'Dungeon Biff med mousse', sum=3.625).put()

    GameNight(id=5674038840000512, date=date.fromtimestamp(1580774400), host=u'André', description=u'Lefse og gifler, sushi, crepe, cyclades', sum=4.20833333333).put()

    GameNight(id=5676982813589504, date=date.fromtimestamp(1505260800), host=u'Damian', description=u'Fylt sopp, lakselasagne, blåbærfromasj, brawlhalla+speedrunners', sum=4.125).put()

    GameNight(id=5677751478517760, date=date.fromtimestamp(1465171200), host=u'Stian', description=u'Mexikansk Pølse / Angus Burger m/Brioche brød og chips / Jordbærsmoothie // Ute Kubb + Google Trends', sum=4.25).put()

    GameNight(id=5679846214598656, date=date.fromtimestamp(1484611200), host=u'Stian', description=u'Pannekake, lasagne, sjokoladefondant og Dead of Winter', sum=4.41666666667).put()

    GameNight(id=5681034041491456, date=date.fromtimestamp(1384905600), host=u'Damian', description=u'Wokka Poker', sum=3.25).put()

    GameNight(id=5681788370288640, date=date.fromtimestamp(1654473600), host=u'Øivind', description=u'Fake, øiv står over', sum=None).put()

    GameNight(id=5682274280407040, date=date.fromtimestamp(1543276800), host=u'Ole', description=u'Ribbelefsa, juleburger, hjemmelaget varm sjokolade med krem og julesnacks. OG MAGIC!', sum=4.0).put()

    GameNight(id=5684666375864320, date=date.fromtimestamp(1453161600), host=u'Stian', description=u'Hvitløksbrød med parmaskinke, Luksustaco med biff, Hjemmelaget Sjokoladepudding med vaniljesaus. Minigames som spill. André borte', sum=4.5).put()

    GameNight(id=5684961520648192, date=date.fromtimestamp(1548115200), host=u'Ole', description=u'Digg brød med Aioli! Pinnekjøtt!!! <3 <3 Flattbrødbrownies med deilig vanlije IS! + MAGIC PENTA :D', sum=4.5625).put()

    GameNight(id=5685288500199424, date=date.fromtimestamp(1581984000), host=u'Damian', description=u'Avokado+brie+spekeskinke toast, lammegryte, pasjonsfrukt ostekake', sum=4.15625).put()

    GameNight(id=5686589850124288, date=date.fromtimestamp(1528156800), host=u'Ole', description=u'Bruschetta, Caesar salat, jordbær med fløte og modifisert TERRA.', sum=4.125).put()

    GameNight(id=5688424874901504, date=date.fromtimestamp(1462233600), host=u'Ole', description=u'Eggicado, taco, daimkake, fifa', sum=3.41666666667).put()

    GameNight(id=5689792285114368, date=date.fromtimestamp(1515456000), host=u'Ole', description=u'Frukt og skinke, pizza, jordbær og sjoko + escape room spill', sum=3.625).put()

    GameNight(id=5692352580550656, date=date.fromtimestamp(1647907200), host=u'Stian', description=u'Maobun, veggisnachos, mosse, speedterra', sum=4.3125).put()

    GameNight(id=5693341270278144, date=date.fromtimestamp(1512950400), host=u'Øivind', description=u'God jul. Pepperkaker og gløgg, Rekecocktail + baguette, pinnekjøtt og rotmos, riskrem m. saus + Sheriff of Nottingham', sum=4.5).put()

    GameNight(id=5695132296806400, date=date.fromtimestamp(1630972800), host=u'Ole', description=u'Melon+skinke, pizza, is+sjokofudge, terra short', sum=3.875).put()

    GameNight(id=5696807065616384, date=date.fromtimestamp(1592265600), host=u'Stian', description=u'Stektmelonskive, grilltallerken med svart bacon, is med nonstoo, poker', sum=4.1875).put()

    GameNight(id=5697423099822080, date=date.fromtimestamp(1471910400), host=u'Damian', description=u'Nachos, luxustaco, brown m is, nhl oh litt worms', sum=3.875).put()

    GameNight(id=5698390272770048, date=date.fromtimestamp(1501545600), host=u'Ole', description=u'Ræserbårtur, melon og skinke, svinekjøtt der noe hadde fugleinfluensa, banan med smelta skjokolade, munchkin', sum=3.83333333333).put()

    GameNight(id=5698549949923328, date=date.fromtimestamp(1571788800), host=u'Ole', description=u'Aoilibrød, pizza, sjokokake, magic', sum=3.0).put()

    GameNight(id=5700735861784576, date=date.fromtimestamp(1493769600), host=u'Damian', description=u'Lefserull, Pulled pork burger MPOMFRI, panna cotta, kortspill', sum=3.625).put()

    GameNight(id=5700911208857600, date=date.fromtimestamp(1570060800), host=u'Stian', description=u'Arme Riddere m/ triple topping, Innbakt Laks, Milkshake’n’Donut. World of Warcraft', sum=3.1875).put()

    GameNight(id=5701325169885184, date=date.fromtimestamp(1555372800), host=u'Damian', description=u'Ferske vårruller, indisk red curry lammegryte, crêpes m nutella, is og bær, terra', sum=4.25).put()

    GameNight(id=5704471946461184, date=date.fromtimestamp(1516665600), host=u'André', description=u'Brokkoliblomkålmix, Viltgryte, sveler, 2player overcooked', sum=4.04166666667).put()

    GameNight(id=5707090131681280, date=date.fromtimestamp(1535414400), host=u'Øivind', description=u'Broccolisalat m bacon og baguette. Pizza. Jordbærfluff. Terra prelude og Venus med nye sleeves og tidlig ferdig', sum=3.71875).put()

    GameNight(id=5707424224772096, date=date.fromtimestamp(1629763200), host=u'Stian', description=u'Forett med ost, pizza, sitruskake, coop-spill', sum=4.125).put()

    GameNight(id=5707725409353728, date=date.fromtimestamp(1557360000), host=u'Øivind', description=u'Lefse og coockie. Pizza. Mars is og brownie. Terra', sum=3.46875).put()

    GameNight(id=5710211792764928, date=date.fromtimestamp(1562112000), host=u'André', description=u'3500kr night; Max burger, sushi, crepe, terra', sum=3.875).put()

    GameNight(id=5712076815204352, date=date.fromtimestamp(1554163200), host=u'André', description=u'Oslo mek dag. Joe and the juice, sushi, muffins, terra', sum=4.0).put()

    GameNight(id=5713990399295488, date=date.fromtimestamp(1539734400), host=u'Øivind', description=u'Dumplings, crispy duck, bløt brownie m. Ekte vanilje is. Secret Hitler', sum=4.25).put()

    GameNight(id=5715999101812736, date=date.fromtimestamp(1380585600), host=u'Stian', description=u'Tikkafifa + vaniljesaus', sum=3.29166666667).put()

    GameNight(id=5716010132832256, date=date.fromtimestamp(1565740800), host=u'Øivind', description=u'Meloner og serrona, Bacon cheese burgers m fries, Key lime pie m. vanilje is, Sheriff', sum=3.71875).put()

    GameNight(id=5717495361044480, date=date.fromtimestamp(1506038400), host=u'Øivind', description=u'Scampibags, burgers, brownie+is, battlestar galactica', sum=4.41666666667).put()

    GameNight(id=5717989642993664, date=date.fromtimestamp(1632787200), host=u'André', description=u'Travernan, vr', sum=4.3125).put()

    GameNight(id=5719677699358720, date=date.fromtimestamp(1649721600), host=u'Ole', description=u'Soppsuppe, pasta carbonera, timatsu, terra', sum=3.875).put()

    GameNight(id=5720929187397632, date=date.fromtimestamp(1458172800), host=u'Stian', description=u'baconsurra asparges, frechelaks, brødsurra kvikklunsj', sum=3.66666666667).put()

    GameNight(id=5722467590995968, date=date.fromtimestamp(1480982400), host=u'Ole', description=u'Pannekaker, Buffalo wings, cookies and vanilje milkshake, evolution, andre borte', sum=4.125).put()

    GameNight(id=5725107787923456, date=date.fromtimestamp(1395100800), host=u'André', description=u'Vårull, and, 7kr rimi dessert + digitale 7kamp', sum=3.66666666667).put()

    GameNight(id=5725641328558080, date=date.fromtimestamp(1654560000), host=u'Stian', description=u'Toast, gyro, crepe, 7wonders', sum=4.78125).put()

    GameNight(id=5726607939469312, date=date.fromtimestamp(1456790400), host=u'Damian', description=u'Egg og asparges, indrefilet, brownies og is, Idarb, worms, something', sum=3.5).put()

    GameNight(id=5728757302165504, date=date.fromtimestamp(1488240000), host=u'Damian', description=u'Avocado m avocado og skinke og bacon, cremet pazta kyllingbacon, smoothie', sum=3.91666666667).put()

    GameNight(id=5730602795925504, date=date.fromtimestamp(1549324800), host=u'André', description=u'Chilikveld; avokadojordbærchilisalsa, chiligryte med choritzo, chilisjokolade, mario party', sum=3.0).put()

    GameNight(id=5730774057746432, date=date.fromtimestamp(1529971200), host=u'André', description=u'Smash/sombreros, Foodora GN, crepes, is, terra, dami syk', sum=4.25).put()

    GameNight(id=5731563417370624, date=date.fromtimestamp(1572825600), host=u'André', description=u'Vegansk snacks, pizza travern, vegansk ben and j, terra', sum=2.6875).put()

    GameNight(id=5733311175458816, date=date.fromtimestamp(1485820800), host=u'André', description=u'Grønnsakssmoothie, biffstrimler i fløtesaus, muffins, dead of winter victory', sum=3.91666666667).put()

    GameNight(id=5736126123868160, date=date.fromtimestamp(1517875200), host=u'Damian', description=u'Spekefat+eggerøre, spaghetti bolonese, pavlova m karamel og sjokoladesaus+smash og blåbær, treadnauts', sum=4.25).put()

    GameNight(id=5737437254909952, date=date.fromtimestamp(1594252800), host=u'Ole', description=u'Melonskink, burger, milkshake, sorcerer', sum=3.65625).put()

    GameNight(id=5741571395813376, date=date.fromtimestamp(1575331200), host=u'Øivind', description=u'Risgrøt, grandis hjemmelaga, vaniljeis med nonstop og sjoko saus, terra turmoil', sum=3.09375).put()

    GameNight(id=5742397807919104, date=date.fromtimestamp(1563408000), host=u'Damian', description=u'Brie/asparges i spekeskinke, burger, jordbær-vaniljesaus-sjokolade-is, ticket to ride', sum=3.84375).put()

    GameNight(id=5745251142598656, date=date.fromtimestamp(1560902400), host=u'Ole', description=u'Aiolibrød, pizza, mandelkake, ubermagic', sum=3.6875).put()

    GameNight(id=5745865499082752, date=date.fromtimestamp(1464048000), host=u'Damian', description=u'Innnbakt shrom bac, hjemb fiskep, jorbermose m sjok, speedrunners', sum=3.95833333333).put()

    GameNight(id=5746066179751936, date=date.fromtimestamp(1578960000), host=u'Ole', description=u'Brokkolisalat, nachoburger, oreoglass, crank', sum=4.0).put()

    GameNight(id=5747610597982208, date=date.fromtimestamp(1487635200), host=u'Ole', description=u'Hvitlkbagg m spekeskinke, pulled pork n chick, sjokolpdding, dead of winter', sum=3.91666666667).put()

    GameNight(id=5749328048029696, date=date.fromtimestamp(1392681600), host=u'Damian', description=u'Dungeon Biffsnadder med is og hvitløksbrød', sum=3.54166666667).put()

    GameNight(id=5749563331706880, date=date.fromtimestamp(1474934400), host=u'André', description=u'(Classic) Peppra Gulrot, helstekt kylling, is med jordbær, Would i Lie To You?', sum=3.375).put()

    GameNight(id=5750082376826880, date=date.fromtimestamp(1636416000), host=u'Damian', description=u'Lefse med skinke og mørapølse ++, torsk wellington, oreo-kremdessert. Poker', sum=4.04166666667).put()

    GameNight(id=5750173443555328, date=date.fromtimestamp(1558310400), host=u'Stian', description=u'Bakt Potet // Nachos // Brownie + Is //// Port Royal', sum=4.1875).put()

    GameNight(id=5750790484393984, date=date.fromtimestamp(1398729600), host=u'Damian', description=u'Indrefilet, brownies m is, dominion+film', sum=3.45833333333).put()

    GameNight(id=5750943224168448, date=date.fromtimestamp(1523318400), host=u'Ole', description=u'Ost, pølse og hvitløksbrød, lasagne med brokkolibaconsalat og vaffel med sjokoladeis og smeltet hvit sjokolade. Clank! Build your own deck!', sum=4.45833333333).put()

    GameNight(id=5752571553644544, date=date.fromtimestamp(1490659200), host=u'André', description=u'Avocadobaconparmaost, laksegryte, sjokoladepudding, epic mario party 2 runde', sum=3.66666666667).put()

    GameNight(id=5752754626625536, date=date.fromtimestamp(1410912000), host=u'Ole', description=u'briebrød, taconormal, isbrown, no outbreak', sum=3.875).put()

    GameNight(id=5754456129929216, date=date.fromtimestamp(1599696000), host=u'Damian', description=u'Hjemmelagde hvitløksbaguetter, pokebowl, smuldrepai + poker', sum=4.34375).put()

    GameNight(id=5757334940811264, date=date.fromtimestamp(1455667200), host=u'Ole', description=u'pøls quesidillas brownis teamwork', sum=3.625).put()

    GameNight(id=5759180434571264, date=date.fromtimestamp(1508803200), host=u'Ole', description=u'Kamskjell? Nachos. Vaffle is sjoko. Who r i + easy pandemic', sum=4.41666666667).put()

    GameNight(id=5759381115240448, date=date.fromtimestamp(1583798400), host=u'Øivind', description=u'Cæsarsalat, butter chicken, snickers kake, pandemic on the brink', sum=4.4375).put()

    GameNight(id=5761673931522048, date=date.fromtimestamp(1527033600), host=u'Øivind', description=u'Grillnight og Terraforming Mars! Scampi, grillede grønnsaker, avokado. Entrecote, salat, potetbåter. Grillet banan med sjokolade, vaniljeis og marshmellows.', sum=4.58333333333).put()

    GameNight(id=5762637883244544, date=date.fromtimestamp(1473724800), host=u'Stian', description=u'Hjemmlag pizza, Fiskesuppe, vaffle is og sjoko. CAH og minigames', sum=4.375).put()

    GameNight(id=5764017373052928, date=date.fromtimestamp(1502755200), host=u'André', description=u'Potetgull med øl, godt stekt kyllinggryte, jorbær med vaniljesaus, marioparty, samt mye whining fra boisa', sum=2.875).put()

    GameNight(id=5769928858664960, date=date.fromtimestamp(1459814400), host=u'André', description=u'Grønnsakscocktail, chorizo m tilb, dyreste is med jorbær og 6 kamp i chromecast games', sum=3.625).put()

    GameNight(id=5924029064019968, date=date.fromtimestamp(1414454400), host=u'André', description=u'Gulerot, fishyballs, sjokkosaus + CS GO', sum=3.0).put()

    GameNight(id=5930525202055168, date=date.fromtimestamp(1445299200), host=u'Stian', description=u'chilisuppe. svinegreier. mangorislol', sum=3.625).put()

    GameNight(id=5935788952911872, date=date.fromtimestamp(1413244800), host=u'Stian', description=u'ChinaPancake, boller med is + FFA archergame', sum=3.83333333333).put()

    GameNight(id=5945723749138432, date=date.fromtimestamp(1416873600), host=u'Ole', description=u'PinnekjøttfraMENY', sum=3.875).put()

    GameNight(id=5950075893186560, date=date.fromtimestamp(1437264000), host=u'Stian', description=u'lefsa med laks, Pita , pain au chocolat. Bombsquad + parking', sum=4.0).put()

    GameNight(id=5956742756171776, date=date.fromtimestamp(1421712000), host=u'André', description=u'Spekeskinke tallerken/Spagetti Bolognese/HAHAha.. - TP?', sum=3.20833333333).put()

    GameNight(id=5995637980004352, date=date.fromtimestamp(1420502400), host=u'Stian', description=u'Minipizza/Saltimbocca i hvitvin/Panna Cotta - Risk', sum=4.25).put()

    GameNight(id=6255412097581056, date=date.fromtimestamp(1408579200), host=u'Stian', description=u'enchilada, laksepasta, sjokomousse SPEEDRUNNERS', sum=4.45833333333).put()

    GameNight(id=6486979017441280, date=date.fromtimestamp(1446508800), host=u'André', description=u'marinert kylling, japansk biffsuppe, asiatiske muffins. togspill', sum=4.0).put()

    GameNight(id=6508673702559744, date=date.fromtimestamp(1444089600), host=u'Damian', description=u'Vårruller, pad thai, is+banan+sjoko, orbit', sum=3.29166666667).put()

    GameNight(id=6519692709593088, date=date.fromtimestamp(1447200000), host=u'André', description=u'Reker m eggerør, ørret, abstrakt rosa is. togspill. Dato usikker.', sum=3.625).put()

    GameNight(id=6558587933425664, date=date.fromtimestamp(1447113600), host=u'Stian', description=u'sandwitchgreie, biff, vaniljeis m bringerbærkrem, rocket league. Dato usikker.', sum=4.04166666667).put()


    # Votes:
    Vote(id=4787561121710080, voter=u'André', dessert=4, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5178081291534336)).put()

    Vote(id=4791893401534464, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5945723749138432)).put()

    Vote(id=4799981630259200, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5361079110598656)).put()

    Vote(id=4804129360707584, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=2, present=True, game_night=Key(GameNight, 4824175986343936)).put()

    Vote(id=4809889046069248, voter=u'André', dessert=3, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 6255412097581056)).put()

    Vote(id=4819823842295808, voter=u'Damian', dessert=2, main_course=2, appetizer=4, game=4, present=True, game_night=Key(GameNight, 4798129157177344)).put()

    Vote(id=4830842849329152, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=2, present=True, game_night=Key(GameNight, 5178081291534336)).put()

    Vote(id=4831648155697152, voter=u'Stian', dessert=4, main_course=5, appetizer=3, game=3, present=True, game_night=Key(GameNight, 4824175986343936)).put()

    Vote(id=4836609111359488, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5752754626625536)).put()

    Vote(id=4848037214027776, voter=u'Damian', dessert=1, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5956742756171776)).put()

    Vote(id=4855880898052096, voter=u'Stian', dessert=2, main_course=3, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5924029064019968)).put()

    Vote(id=4860816083910656, voter=u'André', dessert=3, main_course=4, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5935788952911872)).put()

    Vote(id=4863277368606720, voter=u'Ole', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 6486979017441280)).put()

    Vote(id=4865814888972288, voter=u'Stian', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5945723749138432)).put()

    Vote(id=4869738073161728, voter=u'Damian', dessert=3, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5752754626625536)).put()

    Vote(id=4871574171680768, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5162157834502144)).put()

    Vote(id=4875722304782336, voter=u'André', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5995637980004352)).put()

    Vote(id=4880682857791488, voter=u'Damian', dessert=5, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5995637980004352)).put()

    Vote(id=4896606314823680, voter=u'André', dessert=2, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5432688026583040)).put()

    Vote(id=4904903117897728, voter=u'André', dessert=3, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5387125939765248)).put()

    Vote(id=4906365554262016, voter=u'Damian', dessert=2, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5930525202055168)).put()

    Vote(id=4908329696493568, voter=u'André', dessert=3, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 6508673702559744)).put()

    Vote(id=4916395376640000, voter=u'André', dessert=3, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5393792802750464)).put()

    Vote(id=4924590711111680, voter=u'Ole', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5930525202055168)).put()

    Vote(id=5066880297467904, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5142615859134464)).put()

    Vote(id=5068423386103808, voter=u'Damian', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5149590550478848)).put()

    Vote(id=5069036098420736, voter=u'Stian', dessert=2, main_course=5, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5725107787923456)).put()

    Vote(id=5069673288695808, voter=u'André', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5081225274327040)).put()

    Vote(id=5070907085160448, voter=u'André', dessert=3, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5080816245800960)).put()

    Vote(id=5072543601917952, voter=u'Ole', dessert=4, main_course=5, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5149590550478848)).put()

    Vote(id=5073358639071232, voter=u'Øivind', dessert=3, main_course=4, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5081225274327040)).put()

    Vote(id=5074283197890560, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5080816245800960)).put()

    Vote(id=5075893944844288, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5149590550478848)).put()

    Vote(id=5077556231405568, voter=u'Stian', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5080816245800960)).put()

    Vote(id=5079595200020480, voter=u'Damian', dessert=3, main_course=4, appetizer=2, game=6, present=True, game_night=Key(GameNight, 5081225274327040)).put()

    Vote(id=5079604133888000, voter=u'Stian', dessert=5, main_course=4, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5672749318012928)).put()

    Vote(id=5082523629518848, voter=u'Øivind', dessert=5, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5142615859134464)).put()

    Vote(id=5083293435297792, voter=u'Stian', dessert=4, main_course=5, appetizer=3, game=6, present=True, game_night=Key(GameNight, 5081225274327040)).put()

    Vote(id=5086100271923200, voter=u'André', dessert=3, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5129512190738432)).put()

    Vote(id=5096168749006848, voter=u'Damian', dessert=5, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5122315436163072)).put()

    Vote(id=5099075594616832, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5700911208857600)).put()

    Vote(id=5101298819006464, voter=u'André', dessert=4, main_course=3, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5749328048029696)).put()

    Vote(id=5101952727777280, voter=u'Damian', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5684666375864320)).put()

    Vote(id=5104947787988992, voter=u'Stian', dessert=5, main_course=4, appetizer=3, game=4, present=False, game_night=Key(GameNight, 5142615859134464)).put()

    Vote(id=5105650963054592, voter=u'Damian', dessert=5, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5672749318012928)).put()

    Vote(id=5109799364591616, voter=u'Stian', dessert=4, main_course=5, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5750790484393984)).put()

    Vote(id=5112317826039808, voter=u'Ole', dessert=2, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5725107787923456)).put()

    Vote(id=5113123132407808, voter=u'Damian', dessert=2, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5081456606969856)).put()

    Vote(id=5118084088070144, voter=u'André', dessert=2, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5636318331666432)).put()

    Vote(id=5137355874762752, voter=u'André', dessert=6, main_course=4, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5672749318012928)).put()

    Vote(id=5138892256706560, voter=u'André', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5142615859134464)).put()

    Vote(id=5142291060621312, voter=u'Damian', dessert=5, main_course=3, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5129512190738432)).put()

    Vote(id=5143843011821568, voter=u'Damian', dessert=3, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5080816245800960)).put()

    Vote(id=5144752345317376, voter=u'Ole', dessert=2, main_course=3, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5924029064019968)).put()

    Vote(id=5147289865682944, voter=u'Ole', dessert=3, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5749328048029696)).put()

    Vote(id=5151213049872384, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5636318331666432)).put()

    Vote(id=5151226664583168, voter=u'Øivind', dessert=3, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5149590550478848)).put()

    Vote(id=5153049148391424, voter=u'Ole', dessert=5, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5631986051842048)).put()

    Vote(id=5157197281492992, voter=u'Damian', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5636318331666432)).put()

    Vote(id=5186378094608384, voter=u'André', dessert=3, main_course=4, appetizer=4, game=2, present=True, game_night=Key(GameNight, 4824175986343936)).put()

    Vote(id=5186613378285568, voter=u'Damian', dessert=4, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5749563331706880)).put()

    Vote(id=5187840530972672, voter=u'Damian', dessert=4, main_course=5, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5935788952911872)).put()

    Vote(id=5189804673204224, voter=u'André', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5945723749138432)).put()

    Vote(id=5197870353350656, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5631986051842048)).put()

    Vote(id=5198965662285824, voter=u'Øivind', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5746066179751936)).put()

    Vote(id=5206065687822336, voter=u'Ole', dessert=4, main_course=5, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5935788952911872)).put()

    Vote(id=5354843354955776, voter=u'Ole', dessert=3, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 6508673702559744)).put()

    Vote(id=5362931583680512, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 4657391668822016)).put()

    Vote(id=5367079314128896, voter=u'Damian', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5387125939765248)).put()

    Vote(id=5394598109118464, voter=u'Stian', dessert=3, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5387125939765248)).put()

    Vote(id=5410987167449088, voter=u'Damian', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 6519692709593088)).put()

    Vote(id=5418830851473408, voter=u'Stian', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 6486979017441280)).put()

    Vote(id=5423766037331968, voter=u'André', dessert=2, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5930525202055168)).put()

    Vote(id=5428764842393600, voter=u'Stian', dessert=3, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 6508673702559744)).put()

    Vote(id=5434524125102080, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5393792802750464)).put()

    Vote(id=5438672258203648, voter=u'André', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 6558587933425664)).put()

    Vote(id=5443632811212800, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 6558587933425664)).put()

    Vote(id=5629522644828160, voter=u'André', dessert=2, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5645937472962560)).put()

    Vote(id=5630110493310976, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5761673931522048)).put()

    Vote(id=5630142764285952, voter=u'Stian', dessert=4, main_course=5, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5710211792764928)).put()

    Vote(id=5630455256711168, voter=u'Damian', dessert=3, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5696807065616384)).put()

    Vote(id=5630742793027584, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5636953047302144)).put()

    Vote(id=5630756441292800, voter=u'Damian', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5646862031781888)).put()

    Vote(id=5630978613575680, voter=u'Damian', dessert=5, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5759180434571264)).put()

    Vote(id=5632006343884800, voter=u'André', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5644378534051840)).put()

    Vote(id=5632510532780032, voter=u'Øivind', dessert=4, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5674038840000512)).put()

    Vote(id=5633236919123968, voter=u'Øivind', dessert=3, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5750173443555328)).put()

    Vote(id=5634140607086592, voter=u'Øivind', dessert=4, main_course=3, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5692352580550656)).put()

    Vote(id=5634208160546816, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5736126123868160)).put()

    Vote(id=5634387206995968, voter=u'Ole', dessert=3, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5733311175458816)).put()

    Vote(id=5634457830686720, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5645937472962560)).put()

    Vote(id=5634612826996736, voter=u'Damian', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5698390272770048)).put()

    Vote(id=5635698069602304, voter=u'Damian', dessert=1, main_course=1, appetizer=1, game=1, present=False, game_night=Key(GameNight, 5712076815204352)).put()

    Vote(id=5635703144710144, voter=u'Damian', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5639955095224320)).put()

    Vote(id=5635949232914432, voter=u'Stian', dessert=2, main_course=4, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5639955095224320)).put()

    Vote(id=5635999187075072, voter=u'Ole', dessert=3, main_course=2, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5671038738235392)).put()

    Vote(id=5636621084917760, voter=u'Damian', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5681788370288640)).put()

    Vote(id=5636928644841472, voter=u'Øivind', dessert=6, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5644378534051840)).put()

    Vote(id=5637489247125504, voter=u'Damian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5688424874901504)).put()

    Vote(id=5637641986899968, voter=u'Stian', dessert=2, main_course=3, appetizer=3, game=6, present=True, game_night=Key(GameNight, 5682274280407040)).put()

    Vote(id=5637864410841088, voter=u'Damian', dessert=3, main_course=2, appetizer=1, game=4, present=False, game_night=Key(GameNight, 5717989642993664)).put()

    Vote(id=5638159220080640, voter=u'Damian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5745251142598656)).put()

    Vote(id=5638186843766784, voter=u'André', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5684961520648192)).put()

    Vote(id=5638830484881408, voter=u'André', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5720929187397632)).put()

    Vote(id=5639026912526336, voter=u'André', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5713990399295488)).put()

    Vote(id=5639047607222272, voter=u'Stian', dessert=5, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5646862031781888)).put()

    Vote(id=5639272220590080, voter=u'Ole', dessert=6, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5759381115240448)).put()

    Vote(id=5639274879778816, voter=u'André', dessert=5, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5726607939469312)).put()

    Vote(id=5639456635748352, voter=u'Øivind', dessert=4, main_course=4, appetizer=4, game=4, present=False, game_night=Key(GameNight, 5645937472962560)).put()

    Vote(id=5639574185312256, voter=u'Ole', dessert=5, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5632763172487168)).put()

    Vote(id=5640077560512512, voter=u'André', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5716010132832256)).put()

    Vote(id=5640941595525120, voter=u'André', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5686589850124288)).put()

    Vote(id=5641142922117120, voter=u'Ole', dessert=3, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5654153720233984)).put()

    Vote(id=5641497726681088, voter=u'André', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5682274280407040)).put()

    Vote(id=5641508757700608, voter=u'Ole', dessert=5, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5750173443555328)).put()

    Vote(id=5641906755207168, voter=u'Stian', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5730774057746432)).put()

    Vote(id=5641927449903104, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5644378534051840)).put()

    Vote(id=5642355134693376, voter=u'Ole', dessert=6, main_course=6, appetizer=6, game=5, present=True, game_night=Key(GameNight, 5725641328558080)).put()

    Vote(id=5642684278505472, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5717495361044480)).put()

    Vote(id=5642779036221440, voter=u'Damian', dessert=2, main_course=3, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5632908932939776)).put()

    Vote(id=5643144871804928, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5712076815204352)).put()

    Vote(id=5643172898144256, voter=u'Øivind', dessert=2, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5639955095224320)).put()

    Vote(id=5643307107483648, voter=u'Stian', dessert=3, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5652156384280576)).put()

    Vote(id=5644406560391168, voter=u'Damian', dessert=1, main_course=3, appetizer=1, game=2, present=True, game_night=Key(GameNight, 5642554087309312)).put()

    Vote(id=5645012914143232, voter=u'Øivind', dessert=5, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5710211792764928)).put()

    Vote(id=5645260881395712, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5631076886118400)).put()

    Vote(id=5645784439586816, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5677751478517760)).put()

    Vote(id=5645914630782976, voter=u'Damian', dessert=4, main_course=4, appetizer=2, game=5, present=False, game_night=Key(GameNight, 5730774057746432)).put()

    Vote(id=5646239437684736, voter=u'Damian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5757334940811264)).put()

    Vote(id=5646491456634880, voter=u'André', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5681788370288640)).put()

    Vote(id=5646620347596800, voter=u'André', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5722467590995968)).put()

    Vote(id=5646874153320448, voter=u'Stian', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5636953047302144)).put()

    Vote(id=5647214755971072, voter=u'Øivind', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5707424224772096)).put()

    Vote(id=5647438564032512, voter=u'Damian', dessert=3, main_course=3, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5642790067240960)).put()

    Vote(id=5647591547076608, voter=u'Øivind', dessert=5, main_course=5, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5650665401483264)).put()

    Vote(id=5647648723828736, voter=u'Ole', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5752571553644544)).put()

    Vote(id=5648334039547904, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5639955095224320)).put()

    Vote(id=5648456504836096, voter=u'Ole', dessert=5, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5707424224772096)).put()

    Vote(id=5648554290839552, voter=u'Stian', dessert=4, main_course=3, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5749328048029696)).put()

    Vote(id=5649050225344512, voter=u'Stian', dessert=4, main_course=3, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5091364022779904)).put()

    Vote(id=5649073335959552, voter=u'André', dessert=3, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5746066179751936)).put()

    Vote(id=5649202965118976, voter=u'Stian', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5728757302165504)).put()

    Vote(id=5649521866440704, voter=u'Stian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5667908084563968)).put()

    Vote(id=5649695233802240, voter=u'Øivind', dessert=4, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5754456129929216)).put()

    Vote(id=5652383656837120, voter=u'André', dessert=4, main_course=5, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5676982813589504)).put()

    Vote(id=5652405962145792, voter=u'Øivind', dessert=4, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5725641328558080)).put()

    Vote(id=5652536396611584, voter=u'Stian', dessert=3, main_course=5, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5684961520648192)).put()

    Vote(id=5652720409116672, voter=u'Øivind', dessert=1, main_course=5, appetizer=3, game=6, present=True, game_night=Key(GameNight, 5686589850124288)).put()

    Vote(id=5652771571236864, voter=u'Ole', dessert=4, main_course=5, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5716010132832256)).put()

    Vote(id=5652786310021120, voter=u'Stian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5757334940811264)).put()

    Vote(id=5653164804014080, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5759180434571264)).put()

    Vote(id=5653391690694656, voter=u'Damian', dessert=2, main_course=2, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5741571395813376)).put()

    Vote(id=5654313976201216, voter=u'Damian', dessert=4, main_course=4, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5715999101812736)).put()

    Vote(id=5654477344342016, voter=u'Ole', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5681788370288640)).put()

    Vote(id=5654617534758912, voter=u'André', dessert=3, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5685288500199424)).put()

    Vote(id=5655242385391616, voter=u'Ole', dessert=1, main_course=4, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5731563417370624)).put()

    Vote(id=5655869022797824, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5726607939469312)).put()

    Vote(id=5655980960382976, voter=u'Ole', dessert=5, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5736126123868160)).put()

    Vote(id=5656030914543616, voter=u'André', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5737437254909952)).put()

    Vote(id=5656058538229760, voter=u'Ole', dessert=3, main_course=5, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5726607939469312)).put()

    Vote(id=5657379802710016, voter=u'André', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5692352580550656)).put()

    Vote(id=5657535201673216, voter=u'André', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5636139285217280)).put()

    Vote(id=5658514613600256, voter=u'Ole', dessert=5, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5742397807919104)).put()

    Vote(id=5658962204557312, voter=u'Damian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5643440998055936)).put()

    Vote(id=5659539030409216, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5707424224772096)).put()

    Vote(id=5660991467552768, voter=u'Damian', dessert=2, main_course=3, appetizer=4, game=1, present=True, game_night=Key(GameNight, 5737437254909952)).put()

    Vote(id=5662329727352832, voter=u'André', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5639221461123072)).put()

    Vote(id=5662543133540352, voter=u'Damian', dessert=4, main_course=3, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5657382461898752)).put()

    Vote(id=5663284820705280, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5747610597982208)).put()

    Vote(id=5663474965282816, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5710211792764928)).put()

    Vote(id=5663890436259840, voter=u'Ole', dessert=6, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5657058552578048)).put()

    Vote(id=5663944903491584, voter=u'Ole', dessert=6, main_course=4, appetizer=6, game=5, present=True, game_night=Key(GameNight, 5074692033478656)).put()

    Vote(id=5663998322147328, voter=u'Stian', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5636026810761216)).put()

    Vote(id=5664248772427776, voter=u'André', dessert=4, main_course=5, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5668600916475904)).put()

    Vote(id=5664512065667072, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5759381115240448)).put()

    Vote(id=5665370564198400, voter=u'Damian', dessert=5, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5655638436741120)).put()

    Vote(id=5665844310835200, voter=u'Damian', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5710211792764928)).put()

    Vote(id=5666886175948800, voter=u'Stian', dessert=4, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5671038738235392)).put()

    Vote(id=5667039158992896, voter=u'Øivind', dessert=3, main_course=3, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5643440998055936)).put()

    Vote(id=5667383922393088, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5746066179751936)).put()

    Vote(id=5668316433612800, voter=u'Stian', dessert=2, main_course=4, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5731563417370624)).put()

    Vote(id=5668387241852928, voter=u'Øivind', dessert=3, main_course=4, appetizer=2, game=6, present=True, game_night=Key(GameNight, 5636953047302144)).put()

    Vote(id=5668624027090944, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5707725409353728)).put()

    Vote(id=5668753656250368, voter=u'Damian', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5667908084563968)).put()

    Vote(id=5669468231434240, voter=u'Ole', dessert=5, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5704471946461184)).put()

    Vote(id=5669544198668288, voter=u'Ole', dessert=4, main_course=5, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5122315436163072)).put()

    Vote(id=5669845274198016, voter=u'Ole', dessert=6, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5701325169885184)).put()

    Vote(id=5670249378611200, voter=u'Ole', dessert=1, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5730602795925504)).put()

    Vote(id=5670766611791872, voter=u'Damian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5698549949923328)).put()

    Vote(id=5671853574062080, voter=u'Ole', dessert=5, main_course=5, appetizer=6, game=5, present=True, game_night=Key(GameNight, 5692352580550656)).put()

    Vote(id=5671984008527872, voter=u'André', dessert=4, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5074692033478656)).put()

    Vote(id=5672325550702592, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5696807065616384)).put()

    Vote(id=5672734579228672, voter=u'André', dessert=3, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5707725409353728)).put()

    Vote(id=5672889575538688, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5750943224168448)).put()

    Vote(id=5673251619471360, voter=u'Damian', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5731563417370624)).put()

    Vote(id=5673309542809600, voter=u'André', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5650665401483264)).put()

    Vote(id=5673385510043648, voter=u'Øivind', dessert=2, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5764017373052928)).put()

    Vote(id=5674368789118976, voter=u'Damian', dessert=3, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5671831268753408)).put()

    Vote(id=5674823384563712, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5667370274127872)).put()

    Vote(id=5674844079259648, voter=u'André', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5646862031781888)).put()

    Vote(id=5675214360805376, voter=u'Damian', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5689792285114368)).put()

    Vote(id=5675267779461120, voter=u'André', dessert=4, main_course=4, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5631986051842048)).put()

    Vote(id=5676073085829120, voter=u'Stian', dessert=5, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5668600916475904)).put()

    Vote(id=5676084116848640, voter=u'Øivind', dessert=1, main_course=1, appetizer=1, game=1, present=False, game_night=Key(GameNight, 5651144718155776)).put()

    Vote(id=5676201666412544, voter=u'André', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5693341270278144)).put()

    Vote(id=5676511768084480, voter=u'André', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5700911208857600)).put()

    Vote(id=5676827414626304, voter=u'Stian', dessert=5, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5631076886118400)).put()

    Vote(id=5676830073815040, voter=u'Damian', dessert=4, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5769928858664960)).put()

    Vote(id=5677303661068288, voter=u'Øivind', dessert=5, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5074692033478656)).put()

    Vote(id=5677324355764224, voter=u'Øivind', dessert=4, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5701325169885184)).put()

    Vote(id=5678187241537536, voter=u'Stian', dessert=3, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5651144718155776)).put()

    Vote(id=5678444713082880, voter=u'Damian', dessert=5, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5713990399295488)).put()

    Vote(id=5678544864673792, voter=u'Stian', dessert=2, main_course=3, appetizer=1, game=5, present=True, game_night=Key(GameNight, 5745251142598656)).put()

    Vote(id=5678701068943360, voter=u'André', dessert=2, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5632908932939776)).put()

    Vote(id=5679413765079040, voter=u'Ole', dessert=3, main_course=5, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5769928858664960)).put()

    Vote(id=5679778661138432, voter=u'Damian', dessert=1, main_course=2, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5707725409353728)).put()

    Vote(id=5679790782676992, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5653294995210240)).put()

    Vote(id=5681006015152128, voter=u'Damian', dessert=3, main_course=2, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5716010132832256)).put()

    Vote(id=5681717746597888, voter=u'Øivind', dessert=3, main_course=5, appetizer=3, game=6, present=True, game_night=Key(GameNight, 5684961520648192)).put()

    Vote(id=5681777339269120, voter=u'Ole', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5636026810761216)).put()

    Vote(id=5682246254067712, voter=u'Øivind', dessert=6, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5742397807919104)).put()

    Vote(id=5682418589630464, voter=u'André', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5707424224772096)).put()

    Vote(id=5682747733442560, voter=u'Stian', dessert=3, main_course=3, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5747610597982208)).put()

    Vote(id=5683582030839808, voter=u'André', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5761673931522048)).put()

    Vote(id=5684453372329984, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5697423099822080)).put()

    Vote(id=5684473664372736, voter=u'Øivind', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5685288500199424)).put()

    Vote(id=5684903597309952, voter=u'André', dessert=3, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5719677699358720)).put()

    Vote(id=5685057352105984, voter=u'Stian', dessert=5, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5700735861784576)).put()

    Vote(id=5685925472370688, voter=u'André', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5717495361044480)).put()

    Vote(id=5686135749607424, voter=u'Stian', dessert=3, main_course=5, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5717989642993664)).put()

    Vote(id=5686683802533888, voter=u'Ole', dessert=4, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5631383682678784)).put()

    Vote(id=5687379545292800, voter=u'Øivind', dessert=3, main_course=2, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5719677699358720)).put()

    Vote(id=5687539843203072, voter=u'Stian', dessert=2, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5085604337418240)).put()

    Vote(id=5687798237495296, voter=u'Øivind', dessert=3, main_course=3, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5737437254909952)).put()

    Vote(id=5689399052337152, voter=u'André', dessert=3, main_course=4, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5671038738235392)).put()

    Vote(id=5689413791121408, voter=u'Stian', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5745865499082752)).put()

    Vote(id=5689864552972288, voter=u'Stian', dessert=5, main_course=4, appetizer=1, game=5, present=True, game_night=Key(GameNight, 5674038840000512)).put()

    Vote(id=5689922476310528, voter=u'Damian', dessert=4, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5074692033478656)).put()

    Vote(id=5690145009303552, voter=u'Damian', dessert=4, main_course=2, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5632763172487168)).put()

    Vote(id=5690278513999872, voter=u'Damian', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5719677699358720)).put()

    Vote(id=5691122005311488, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5685288500199424)).put()

    Vote(id=5691878833913856, voter=u'Stian', dessert=2, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5707090131681280)).put()

    Vote(id=5692462144159744, voter=u'Ole', dessert=3, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5715999101812736)).put()

    Vote(id=5692592335355904, voter=u'Øivind', dessert=6, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5759180434571264)).put()

    Vote(id=5693417237512192, voter=u'André', dessert=4, main_course=4, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5636026810761216)).put()

    Vote(id=5693582954463232, voter=u'Øivind', dessert=2, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5652156384280576)).put()

    Vote(id=5694209793196032, voter=u'André', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5728757302165504)).put()

    Vote(id=5694979263430656, voter=u'Stian', dessert=3, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5686589850124288)).put()

    Vote(id=5695159920492544, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5697423099822080)).put()

    Vote(id=5695872079757312, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5762637883244544)).put()

    Vote(id=5696082356994048, voter=u'Ole', dessert=3, main_course=2, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5741571395813376)).put()

    Vote(id=5696459148099584, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5671831268753408)).put()

    Vote(id=5696605713858560, voter=u'André', dessert=4, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5671831268753408)).put()

    Vote(id=5697325615808512, voter=u'Stian', dessert=2, main_course=5, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5695132296806400)).put()

    Vote(id=5699257587728384, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5745865499082752)).put()

    Vote(id=5700239927279616, voter=u'Øivind', dessert=5, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5704471946461184)).put()

    Vote(id=5700291089399808, voter=u'Ole', dessert=5, main_course=3, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5645937472962560)).put()

    Vote(id=5700305828184064, voter=u'Stian', dessert=1, main_course=3, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5642554087309312)).put()

    Vote(id=5700866052980736, voter=u'André', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5750943224168448)).put()

    Vote(id=5700983627710464, voter=u'Øivind', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5633226290757632)).put()

    Vote(id=5701213970497536, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5692352580550656)).put()

    Vote(id=5701241594183680, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5747610597982208)).put()

    Vote(id=5701330244993024, voter=u'Øivind', dessert=4, main_course=4, appetizer=4, game=4, present=False, game_night=Key(GameNight, 5730602795925504)).put()

    Vote(id=5702143428263936, voter=u'Stian', dessert=6, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5701325169885184)).put()

    Vote(id=5702167830724608, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5713990399295488)).put()

    Vote(id=5702666986455040, voter=u'André', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5081456606969856)).put()

    Vote(id=5702797177651200, voter=u'André', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5689792285114368)).put()

    Vote(id=5702918200098816, voter=u'Damian', dessert=5, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5725641328558080)).put()

    Vote(id=5703374003503104, voter=u'André', dessert=4, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5698549949923328)).put()

    Vote(id=5703401627189248, voter=u'Damian', dessert=3, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5684961520648192)).put()

    Vote(id=5703697669554176, voter=u'Ole', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5750082376826880)).put()

    Vote(id=5704093720903680, voter=u'Damian', dessert=2, main_course=3, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5730602795925504)).put()

    Vote(id=5704147139559424, voter=u'Ole', dessert=3, main_course=4, appetizer=1, game=5, present=True, game_night=Key(GameNight, 5749563331706880)).put()

    Vote(id=5705241014042624, voter=u'Ole', dessert=5, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5091364022779904)).put()

    Vote(id=5705261306085376, voter=u'Øivind', dessert=3, main_course=6, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5646862031781888)).put()

    Vote(id=5706163895140352, voter=u'Damian', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5762637883244544)).put()

    Vote(id=5706275094528000, voter=u'Damian', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5682274280407040)).put()

    Vote(id=5706285722894336, voter=u'André', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5745251142598656)).put()

    Vote(id=5706803308396544, voter=u'Damian', dessert=4, main_course=3, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5631383682678784)).put()

    Vote(id=5707103779946496, voter=u'Øivind', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5745251142598656)).put()

    Vote(id=5707532110659584, voter=u'Damian', dessert=4, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5704471946461184)).put()

    Vote(id=5707648880082944, voter=u'Damian', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5657582312095744)).put()

    Vote(id=5707702298738688, voter=u'Ole', dessert=1, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5642554087309312)).put()

    Vote(id=5708345528811520, voter=u'Øivind', dessert=1, main_course=3, appetizer=2, game=2, present=True, game_night=Key(GameNight, 5698549949923328)).put()

    Vote(id=5708658021236736, voter=u'Ole', dessert=5, main_course=5, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5696807065616384)).put()

    Vote(id=5709068098338816, voter=u'André', dessert=3, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5667370274127872)).put()

    Vote(id=5709436928655360, voter=u'Ole', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5667908084563968)).put()

    Vote(id=5709447959674880, voter=u'Ole', dessert=3, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5642790067240960)).put()

    Vote(id=5709596605808640, voter=u'Damian', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5750173443555328)).put()

    Vote(id=5709624632147968, voter=u'Stian', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5633226290757632)).put()

    Vote(id=5710239819104256, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5668600916475904)).put()

    Vote(id=5710999223009280, voter=u'Stian', dessert=2, main_course=3, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5632908932939776)).put()

    Vote(id=5711049177169920, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=False, game_night=Key(GameNight, 5701325169885184)).put()

    Vote(id=5711129414205440, voter=u'Damian', dessert=2, main_course=3, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5707090131681280)).put()

    Vote(id=5711670806577152, voter=u'Øivind', dessert=1, main_course=1, appetizer=1, game=1, present=True, game_night=Key(GameNight, 5731563417370624)).put()

    Vote(id=5712088936742912, voter=u'Damian', dessert=5, main_course=5, appetizer=5, game=4, present=False, game_night=Key(GameNight, 5653294995210240)).put()

    Vote(id=5712453606309888, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5722467590995968)).put()

    Vote(id=5712536552865792, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5720929187397632)).put()

    Vote(id=5713320610889728, voter=u'André', dessert=5, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5742397807919104)).put()

    Vote(id=5713573250596864, voter=u'Ole', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5728757302165504)).put()

    Vote(id=5714163003293696, voter=u'Stian', dessert=3, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5681034041491456)).put()

    Vote(id=5714315743068160, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5717495361044480)).put()

    Vote(id=5715161717407744, voter=u'André', dessert=2, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5707090131681280)).put()

    Vote(id=5715182412103680, voter=u'Ole', dessert=6, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5644378534051840)).put()

    Vote(id=5715683958587392, voter=u'André', dessert=4, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5633226290757632)).put()

    Vote(id=5715806423875584, voter=u'Stian', dessert=5, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5716010132832256)).put()

    Vote(id=5715921523965952, voter=u'Øivind', dessert=5, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5636139285217280)).put()

    Vote(id=5716646702350336, voter=u'Damian', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5720929187397632)).put()

    Vote(id=5717023518621696, voter=u'Ole', dessert=5, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5633226290757632)).put()

    Vote(id=5717044213317632, voter=u'Øivind', dessert=3, main_course=4, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5712076815204352)).put()

    Vote(id=5717268826685440, voter=u'Damian', dessert=2, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5652156384280576)).put()

    Vote(id=5717271485874176, voter=u'Stian', dessert=3, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5769928858664960)).put()

    Vote(id=5717424225648640, voter=u'Stian', dessert=3, main_course=5, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5639221461123072)).put()

    Vote(id=5718864172154880, voter=u'Damian', dessert=4, main_course=4, appetizer=1, game=4, present=False, game_night=Key(GameNight, 5674038840000512)).put()

    Vote(id=5718922095493120, voter=u'André', dessert=5, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5653294995210240)).put()

    Vote(id=5718998062727168, voter=u'Damian', dessert=4, main_course=5, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5693341270278144)).put()

    Vote(id=5719223305240576, voter=u'Øivind', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5717989642993664)).put()

    Vote(id=5719238044024832, voter=u'Stian', dessert=3, main_course=2, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5688424874901504)).put()

    Vote(id=5719378301550592, voter=u'Øivind', dessert=4, main_course=4, appetizer=2, game=6, present=True, game_night=Key(GameNight, 5730774057746432)).put()

    Vote(id=5720001365409792, voter=u'André', dessert=5, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5725641328558080)).put()

    Vote(id=5720147234914304, voter=u'André', dessert=2, main_course=4, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5681034041491456)).put()

    Vote(id=5720605454237696, voter=u'André', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5631383682678784)).put()

    Vote(id=5720853220163584, voter=u'André', dessert=5, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5655638436741120)).put()

    Vote(id=5721694119395328, voter=u'Ole', dessert=3, main_course=5, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5651144718155776)).put()

    Vote(id=5722950196002816, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5631076886118400)).put()

    Vote(id=5723368888205312, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5651144718155776)).put()

    Vote(id=5723920363683840, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5650665401483264)).put()

    Vote(id=5724183724032000, voter=u'Stian', dessert=3, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5746066179751936)).put()

    Vote(id=5724313353191424, voter=u'Stian', dessert=5, main_course=3, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5752571553644544)).put()

    Vote(id=5724623454863360, voter=u'André', dessert=3, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5750082376826880)).put()

    Vote(id=5724681378201600, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5667370274127872)).put()

    Vote(id=5725417520496640, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5695132296806400)).put()

    Vote(id=5725851488354304, voter=u'Damian', dessert=3, main_course=3, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5764017373052928)).put()

    Vote(id=5726618567835648, voter=u'Øivind', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5750082376826880)).put()

    Vote(id=5727389891952640, voter=u'Damian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5639221461123072)).put()

    Vote(id=5728689748705280, voter=u'Damian', dessert=3, main_course=3, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5700911208857600)).put()

    Vote(id=5729201025974272, voter=u'André', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5697423099822080)).put()

    Vote(id=5729623769874432, voter=u'Damian', dessert=4, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5631076886118400)).put()

    Vote(id=5730082031140864, voter=u'Stian', dessert=4, main_course=3, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5657382461898752)).put()

    Vote(id=5730450056151040, voter=u'Ole', dessert=4, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5679846214598656)).put()

    Vote(id=5730548328693760, voter=u'Stian', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5685288500199424)).put()

    Vote(id=5730827476402176, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5684666375864320)).put()

    Vote(id=5732312192909312, voter=u'Øivind', dessert=4, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5698390272770048)).put()

    Vote(id=5732793992609792, voter=u'Ole', dessert=5, main_course=4, appetizer=1, game=5, present=True, game_night=Key(GameNight, 5717989642993664)).put()

    Vote(id=5733612049661952, voter=u'Damian', dessert=5, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5759381115240448)).put()

    Vote(id=5733679603122176, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5636139285217280)).put()

    Vote(id=5733935958982656, voter=u'André', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5762637883244544)).put()

    Vote(id=5734027520638976, voter=u'Ole', dessert=4, main_course=5, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5754456129929216)).put()

    Vote(id=5734055144325120, voter=u'André', dessert=4, main_course=3, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5745865499082752)).put()

    Vote(id=5734183724908544, voter=u'Damian', dessert=2, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5686589850124288)).put()

    Vote(id=5735369295265792, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5750173443555328)).put()

    Vote(id=5736253521657856, voter=u'Stian', dessert=2, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5642790067240960)).put()

    Vote(id=5736599870504960, voter=u'Stian', dessert=2, main_course=1, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5741571395813376)).put()

    Vote(id=5736754531270656, voter=u'André', dessert=3, main_course=5, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5657582312095744)).put()

    Vote(id=5737611108810752, voter=u'Damian', dessert=4, main_course=5, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5667370274127872)).put()

    Vote(id=5737664527466496, voter=u'Ole', dessert=3, main_course=3, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5764017373052928)).put()

    Vote(id=5737686832775168, voter=u'Ole', dessert=5, main_course=5, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5638346151821312)).put()

    Vote(id=5738369707409408, voter=u'Damian', dessert=3, main_course=5, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5761673931522048)).put()

    Vote(id=5738466402893824, voter=u'André', dessert=3, main_course=3, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5741571395813376)).put()

    Vote(id=5738600293466112, voter=u'Øivind', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5676982813589504)).put()

    Vote(id=5739238230327296, voter=u'Øivind', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5750943224168448)).put()

    Vote(id=5739392471662592, voter=u'Ole', dessert=3, main_course=2, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5707725409353728)).put()

    Vote(id=5739719937753088, voter=u'Damian', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5679846214598656)).put()

    Vote(id=5740087962763264, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5643440998055936)).put()

    Vote(id=5740141138149376, voter=u'Stian', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5719677699358720)).put()

    Vote(id=5740329646948352, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5754456129929216)).put()

    Vote(id=5740874747084800, voter=u'André', dessert=3, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5679846214598656)).put()

    Vote(id=5741031244955648, voter=u'Ole', dessert=2, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5681034041491456)).put()

    Vote(id=5741642204053504, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5713990399295488)).put()

    Vote(id=5742636757417984, voter=u'Stian', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5657582312095744)).put()

    Vote(id=5742796208078848, voter=u'André', dessert=4, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5684666375864320)).put()

    Vote(id=5742816500121600, voter=u'Øivind', dessert=1, main_course=1, appetizer=1, game=1, present=True, game_night=Key(GameNight, 5700911208857600)).put()

    Vote(id=5743573328723968, voter=u'Ole', dessert=5, main_course=5, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5655638436741120)).put()

    Vote(id=5744125232021504, voter=u'André', dessert=4, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5654153720233984)).put()

    Vote(id=5744277971795968, voter=u'Øivind', dessert=3, main_course=5, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5682274280407040)).put()

    Vote(id=5744378123386880, voter=u'Stian', dessert=2, main_course=3, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5698549949923328)).put()

    Vote(id=5744845133971456, voter=u'Damian', dessert=4, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5657058552578048)).put()

    Vote(id=5745060998021120, voter=u'Damian', dessert=3, main_course=4, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5733311175458816)).put()

    Vote(id=5746055551385600, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5757334940811264)).put()

    Vote(id=5747306418667520, voter=u'Stian', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5742397807919104)).put()

    Vote(id=5747621629001728, voter=u'Stian', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5681788370288640)).put()

    Vote(id=5749095851360256, voter=u'Ole', dessert=4, main_course=6, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5693341270278144)).put()

    Vote(id=5749339079049216, voter=u'Ole', dessert=4, main_course=4, appetizer=1, game=5, present=True, game_night=Key(GameNight, 5674038840000512)).put()

    Vote(id=5750031617359872, voter=u'Ole', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5676982813589504)).put()

    Vote(id=5750085036015616, voter=u'André', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5688424874901504)).put()

    Vote(id=5751011029286912, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5712076815204352)).put()

    Vote(id=5752241604526080, voter=u'Stian', dessert=5, main_course=4, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5737437254909952)).put()

    Vote(id=5753006645575680, voter=u'André', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5638346151821312)).put()

    Vote(id=5753341694967808, voter=u'Stian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5722467590995968)).put()

    Vote(id=5754258133614592, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5677751478517760)).put()

    Vote(id=5754903989321728, voter=u'Øivind', dessert=5, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5736126123868160)).put()

    Vote(id=5755079336394752, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5754456129929216)).put()

    Vote(id=5755685136498688, voter=u'Damian', dessert=3, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5677751478517760)).put()

    Vote(id=5755696167518208, voter=u'Damian', dessert=4, main_course=3, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5671038738235392)).put()

    Vote(id=5756596743307264, voter=u'Øivind', dessert=5, main_course=5, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5653294995210240)).put()

    Vote(id=5756936406433792, voter=u'Stian', dessert=5, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5638346151821312)).put()

    Vote(id=5757332281622528, voter=u'Stian', dessert=5, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5759381115240448)).put()

    Vote(id=5757487680585728, voter=u'Ole', dessert=4, main_course=3, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5700735861784576)).put()

    Vote(id=5757907245203456, voter=u'Stian', dessert=1, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5730602795925504)).put()

    Vote(id=5757952401080320, voter=u'Øivind', dessert=2, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5642790067240960)).put()

    Vote(id=5758401703313408, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5730774057746432)).put()

    Vote(id=5759409141579776, voter=u'Stian', dessert=3, main_course=3, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5749563331706880)).put()

    Vote(id=5760415195725824, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5750082376826880)).put()

    Vote(id=5760744339537920, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5700735861784576)).put()

    Vote(id=5760820306771968, voter=u'André', dessert=3, main_course=4, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5715999101812736)).put()

    Vote(id=5761915615707136, voter=u'André', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5657058552578048)).put()

    Vote(id=5763155720404992, voter=u'Øivind', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5696807065616384)).put()

    Vote(id=5763263606292480, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5698390272770048)).put()

    Vote(id=5763764733345792, voter=u'Øivind', dessert=6, main_course=5, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5657058552578048)).put()

    Vote(id=5765606242516992, voter=u'Ole', dessert=5, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5657382461898752)).put()

    Vote(id=5765867027562496, voter=u'Damian', dessert=3, main_course=4, appetizer=5, game=3, present=True, game_night=Key(GameNight, 5752571553644544)).put()

    Vote(id=5766466041282560, voter=u'Stian', dessert=3, main_course=3, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5733311175458816)).put()

    Vote(id=5766596232478720, voter=u'Øivind', dessert=4, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5689792285114368)).put()

    Vote(id=5766837916663808, voter=u'Ole', dessert=4, main_course=4, appetizer=4, game=5, present=True, game_night=Key(GameNight, 5652156384280576)).put()

    Vote(id=5767253387640832, voter=u'Damian', dessert=4, main_course=5, appetizer=2, game=4, present=True, game_night=Key(GameNight, 5695132296806400)).put()

    Vote(id=5767281011326976, voter=u'Stian', dessert=3, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5654153720233984)).put()

    Vote(id=5767409591910400, voter=u'André', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5636953047302144)).put()

    Vote(id=5768699919204352, voter=u'Øivind', dessert=6, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5638346151821312)).put()

    Vote(id=5768939674009600, voter=u'Øivind', dessert=3, main_course=1, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5632763172487168)).put()

    Vote(id=5769015641243648, voter=u'Damian', dessert=4, main_course=3, appetizer=2, game=3, present=True, game_night=Key(GameNight, 5091364022779904)).put()

    Vote(id=5769324769837056, voter=u'Øivind', dessert=None, main_course=None, appetizer=None, game=None, present=False, game_night=Key(GameNight, 5695132296806400)).put()

    Vote(id=5769720821186560, voter=u'Ole', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5707090131681280)).put()

    Vote(id=5917793308377088, voter=u'Damian', dessert=4, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5382773795717120)).put()

    Vote(id=5925881537101824, voter=u'Damian', dessert=3, main_course=5, appetizer=4, game=4, present=True, game_night=Key(GameNight, 6486979017441280)).put()

    Vote(id=5930029267550208, voter=u'Damian', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5950075893186560)).put()

    Vote(id=5957548062539776, voter=u'André', dessert=3, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5950075893186560)).put()

    Vote(id=5973937120870400, voter=u'Ole', dessert=5, main_course=5, appetizer=5, game=5, present=True, game_night=Key(GameNight, 5393792802750464)).put()

    Vote(id=5981780804894720, voter=u'Stian', dessert=4, main_course=4, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5361079110598656)).put()

    Vote(id=5986715990753280, voter=u'Stian', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 4804625295212544)).put()

    Vote(id=5989177275449344, voter=u'André', dessert=3, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 4657391668822016)).put()

    Vote(id=5991714795814912, voter=u'Stian', dessert=4, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5382773795717120)).put()

    Vote(id=5997474078523392, voter=u'Stian', dessert=1, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5956742756171776)).put()

    Vote(id=6001622211624960, voter=u'Stian', dessert=3, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5432688026583040)).put()

    Vote(id=6006582764634112, voter=u'Damian', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5432688026583040)).put()

    Vote(id=6022506221666304, voter=u'Ole', dessert=3, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 6558587933425664)).put()

    Vote(id=6032265461104640, voter=u'Damian', dessert=1, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 5367575248633856)).put()

    Vote(id=6042295283482624, voter=u'Ole', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 6519692709593088)).put()

    Vote(id=6050490617954304, voter=u'André', dessert=1, main_course=4, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5367575248633856)).put()

    Vote(id=6194936005263360, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5162157834502144)).put()

    Vote(id=6199268285087744, voter=u'Stian', dessert=4, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5752754626625536)).put()

    Vote(id=6205504040730624, voter=u'André', dessert=4, main_course=4, appetizer=1, game=4, present=True, game_night=Key(GameNight, 5750790484393984)).put()

    Vote(id=6207356513812480, voter=u'Damian', dessert=3, main_course=3, appetizer=1, game=5, present=True, game_night=Key(GameNight, 5924029064019968)).put()

    Vote(id=6211504244260864, voter=u'Ole', dessert=2, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 4798129157177344)).put()

    Vote(id=6212000178765824, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=5, present=True, game_night=Key(GameNight, 6255412097581056)).put()

    Vote(id=6217263929622528, voter=u'Stian', dessert=3, main_course=3, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5129512190738432)).put()

    Vote(id=6227198725849088, voter=u'Ole', dessert=3, main_course=3, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5085604337418240)).put()

    Vote(id=6227852634619904, voter=u'Stian', dessert=5, main_course=3, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5122315436163072)).put()

    Vote(id=6231550869897216, voter=u'Ole', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5081456606969856)).put()

    Vote(id=6238217732882432, voter=u'André', dessert=4, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5162157834502144)).put()

    Vote(id=6239023039250432, voter=u'Stian', dessert=2, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 4798129157177344)).put()

    Vote(id=6243983994912768, voter=u'Stian', dessert=2, main_course=4, appetizer=3, game=2, present=True, game_night=Key(GameNight, 5073368378245120)).put()

    Vote(id=6263255781605376, voter=u'Ole', dessert=4, main_course=5, appetizer=1, game=3, present=True, game_night=Key(GameNight, 5750790484393984)).put()

    Vote(id=6268190967463936, voter=u'Damian', dessert=4, main_course=3, appetizer=5, game=5, present=True, game_night=Key(GameNight, 6255412097581056)).put()

    Vote(id=6270652252160000, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5361079110598656)).put()

    Vote(id=6273189772525568, voter=u'Damian', dessert=1, main_course=2, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5085604337418240)).put()

    Vote(id=6277112956715008, voter=u'André', dessert=2, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 5073368378245120)).put()

    Vote(id=6278949055234048, voter=u'Damian', dessert=3, main_course=3, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5725107787923456)).put()

    Vote(id=6283097188335616, voter=u'Damian', dessert=2, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5073368378245120)).put()

    Vote(id=6288057741344768, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5178081291534336)).put()

    Vote(id=6303981198376960, voter=u'Ole', dessert=5, main_course=4, appetizer=4, game=4, present=True, game_night=Key(GameNight, 5995637980004352)).put()

    Vote(id=6312278001451008, voter=u'Ole', dessert=4, main_course=4, appetizer=5, game=4, present=True, game_night=Key(GameNight, 5950075893186560)).put()

    Vote(id=6313740437815296, voter=u'Damian', dessert=4, main_course=4, appetizer=3, game=5, present=True, game_night=Key(GameNight, 4804625295212544)).put()

    Vote(id=6315704580046848, voter=u'Ole', dessert=4, main_course=4, appetizer=3, game=3, present=True, game_night=Key(GameNight, 5382773795717120)).put()

    Vote(id=6323770260193280, voter=u'Ole', dessert=1, main_course=3, appetizer=4, game=3, present=True, game_night=Key(GameNight, 5956742756171776)).put()

    Vote(id=6331965594664960, voter=u'André', dessert=4, main_course=4, appetizer=3, game=4, present=True, game_night=Key(GameNight, 4804625295212544)).put()

    Vote(id=6544730758316032, voter=u'Stian', dessert=4, main_course=4, appetizer=4, game=3, present=True, game_night=Key(GameNight, 4657391668822016)).put()

    Vote(id=6549665944174592, voter=u'Stian', dessert=1, main_course=4, appetizer=2, game=5, present=True, game_night=Key(GameNight, 5367575248633856)).put()

    Vote(id=6560424031944704, voter=u'Stian', dessert=3, main_course=3, appetizer=4, game=4, present=True, game_night=Key(GameNight, 6519692709593088)).put()
