# Johdantoa

Ensimmäisessä osassa tutustuttiin tilastollisesta aineistosta laskettaviin tunnuslukuihin. Tunnuslukujen avulla saadaan tietoa menneestä tai tämänhetkisestä tilanteesta (esimerkiksi kesämökkien määrästä eri kunnissa eri vuosina). Tilastollista aineistoa voidaan käyttää myös siihen, että arvioidaan, mitä tulevaisuudessa tapahtuu (paljonko tontteja uusille kesämökeille kannattaisi varata).

Tilastotieteen ratkaisu ennustamiseen on etsiä jokin matemaattinen malli eli funktio, joka sopii käytettävissä olevaan dataan. Esimerkiksi jonkin kaupungin asukasluku saattaa kasvaa tai vähentyä suunnilleen lineaarisesti (joka vuosi saman verran), yrityksen tuotto voi olla kasvamassa karkeasti ottaen eksponentiaalisesti jne. Funktion kuvaajan ei tarvitse kulkea täsmälleen kaikkien tai edes yhdenkään datapisteen kautta. Tarkoituksena on muodostaa yksinkertainen malli, joka asettuu pisteiden joukkoon mahdollisimman hyvin. Tätä mallin asettumista pistejoukkoon voidaan arvioida eri tavoin.

Jos tiedetään, millaisia lakeja tutkittavan ilmiön taustalla vaikuttaa, voidaan malliksi suoraan valita sopivanlainen funktio. Esimerkiksi metsän kasvulle on kehitetty polynomimalleja, joidenkin tartuntatautien leviämisen tiedetään noudattavan eksponenttimallia jne. Tällöin funktion sovitus dataan tarkoittaa lähinnä sitä, että annetaan tietokoneen etsiä malliin kuuluville luvuille sopivat arvot.

Jos ilmiölle ei ole tiedossa perusteltua matemaattista mallia, voidaan kokeilla erilaisia malleja ja verrata jokaisen mallin antamia lukemia oikeaan dataan. Jos mallin ja oikean datan eroavaisuudet vaikuttavat satunnaisilta ja ovat suhteellisen pieniä, malli on kelvollinen. Seuraavaksi tarkastellaan muutamaa perusmallia. Esiteltyjen mallien lisäksi data-analyysissä käytetään ainakin sini- tai kosinifunktiota ja ns. logistista mallia, joka koostuu eksponenttilausekkeista. 