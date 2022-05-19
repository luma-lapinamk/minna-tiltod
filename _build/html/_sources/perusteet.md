# Perusteita

Todennäköisyyslaskenta liittyy tilanteisiin, jossa mahdollisten tapahtumien lukumäärä on rajallinen. Esimerkiksi säätilasta voidaan selkeästi rajata vaihtoehdot "sataa" tai "ei sada". Vaihtoehtoja voi olla enemmänkin kuin kaksi, esimerkiksi tikanheitossa ne voisivat olla "osuu numeroon 10", "osuu numeroon 9",  .... , "ei osu tauluun ollenkaan".

Hankalaa todennäköisyyslaskennassa on se, että kaikille mahdollisille tapahtumille pitäisi jollakin tavalla tietää tapahtumisen todennäköisyys. Joskus tämäkin on helppoa: esimerkiksi todennäköisyys sille, että satunnaisesti pakasta nostettu pelikortti on hertta, määräytyy suoraan herttojen ja koko pakan korttien lukumäärän suhteesta. Jos taas laskentaa käyttää apuna vaikkapa kalliin rakennushankkeen kannattavuuden arvioinnille, mahdollisille tapahtumille ja niiden todennäköisyyksille on vain päätettävä jonkinlaisia järkiperusteisia arvoja.

Kun tapahtumat ja todennäköisyydet on selvillä, onkin helppoa laittaa luvut kaavoihin, joiden avulla voi harrastaa varsinaista todennäköisyyslaskentaa. Näillä kaavoilla voi tutkia jonkin prosessin lopputulosta yhdistelemällä sen vaiheiden mahdollisia tapahtumia ja niiden todennäköisyyksiä. 

Mihin tilastotieteessä tarvitaan todennäköisyyslaskentaa? Myöhemmin sovitetaan havaintoarvoihin erilaisia jakaumia, joiden avulla voidaan tehdä yleistyksiä populaatiosta mittausten perusteella. Voidaan esimerkiksi pyydystää järvestä kohtuullinen määrä kaloja, mitata niiden pituus ja paino, ja sen jälkeen päätellä, minkä kokoisia yleisesti ottaen ovat kyseisen järven saman lajiset kalat. Toisin sanoen otoksen – eli mitattujen kalojen – avulla luodaan jakauma, joka kuvaa eri kokoisten kalojen osuuksia kalastossa. Jakaumasta voidaan laskea todennäköisyyksiä sille, että satunnainen saalis on vaikkapa painavampi kuin 5 kg, tai että minkä painon ylittää vain 10 % kaloista. 

Todennäköisyydet siis liittyvät läheisesti sellaisiin jakaumiin, jotka kuvaavat jonkin populaation jotakin mitattavaa ominaisuutta.
Todennäköisyyslaskentaan liittyy läheisesti matematiikan osa-alue, jonka nimi on kombinatoriikka. Sen avulla tutkitaan, montako erilaista vaihtoehtoa on saada tietynlainen otos koko populaatiosta. Eräs käytännönläheinen sovellus tälle on tarkastella, kuinka monella tavalla lottokupongin voi täyttää ja kuinka monella tavalla lottoarvonnassa voi tulla vaikkapa "5 oikein" -tulos. Suhteuttamalla nämä vaihtoehtojen lukumäärät toisiinsa saadaan "5 oikein" -voiton todennäköisyys.

 
## Klassinen todennäköisyys

Klassista todennäköisyyslaskentaa sovelletaan tapahtumiin, jotka ovat yhtä todennäköisiä. Esimerkiksi noppaa heitettäessä mikä tahansa silmäluku väliltä 1...6 saadaan samalla todennäköisyydellä. Tietyn tapahtuman $A$ klassinen todennäköisyys $P(A)$ on kyseiselle tapahtumalle suotuisten tapauksien määrä $f$ jaettuna kaikkien mahdollisten tapahtumien määrällä $n$, siis

$P(A)=\frac{f}{n}$.

Minkä tahansa tapahtuman todennäköisyys on lukujen 0 (mahdoton) ja 1 (varma) välillä. Se ilmaistaan prosenttilukuna tai desimaalilukuna. Kun käytetään erilaisia monimutkaisempiin tilanteisiin liittyviä todennäköisyyden laskusääntöjä, kannattaa aina lopuksi tarkistaa, että tulos on  varmasti sallitulla välillä!

**Esim.** Laatikossa on 4 sinistä, 1 keltainen ja 3 punaista palloa. Laatikosta nostetaan yksi pallo. 
Mikä on todennäköisyys sille, että pallo on a) sininen, b) keltainen, c) punainen? 

:::{admonition} Ratkaisu
:class: tip, dropdown

a) $P(\text{sininen}) = \frac{4}{8} = 50 \%$

b) $P(\text{keltainen}) = \frac{1}{8} = 12.5 \%$

c) $P(\text{punainen}) = \frac{3}{8} = 37.5 \%$

:::

**Esim.** Heität kahta noppaa. Millä todennäköisyydellä pistelukujen summa on vähintään 10?

:::{admonition} Ratkaisu
:class: tip, dropdown

Tapahtuma ”pistelukujen summa on vähintään 10” on mahdollista kuudella eri tavalla. Taulukossa lainausmerkeissä olevat luvut kuvaavat ensimmäisellä ja toisella nopalla saatuja silmälukuja, ja muissa ruuduissa on kyseisten silmälukujen summat.

|summa|”1”|”2”|”3”|”4”|”5”|”6”|
|-----|---|---|---|---|---|---|
|**”1”**|2|3|4|5|6|7|
|**”2”**|3|4|5|6|7|8|
|**”3”**|4|5|6|7|8|9|
|**”4”**|5|6|7|8|9|10|
|**”5”**|6|7|8|9|10|11|
|**”6”**|7|8|9|10|11|12|

Siis $P(\text{summa ainakin 10})=\frac{6}{36}=16.7 \%$

:::

## Tilastollinen todennäköisyys

Tilastollinen todennäköisyys tarkoittaa tietyn tapahtuman esiintymisen lukumäärää $f$ jaettuna kaikkien tapahtumien määrällä $n$. Tarkemmin määriteltynä tapahtuman $A$ tilastollinen todennäköisyys $P(A)$ on tapahtuman $A$ suhteellisen frekvenssin raja-arvo, jota lähestytään, kun satunnaista koetta toistetaan äärettömän monta kertaa.

Tilastollista todennäköisyyttä hyödyntävät mm. vakuutusyhtiöt määrittäessään vakuutusmaksun suuruutta sekä autonvalmistajat määrittäessään takuuaikaa. 

**Esim.** Tietyssä lentokonemallissa tapahtuu moottorivika 2 kertaa 1000 lennon aikana. Mikä on vian todennäköisyys yksittäisen lennon aikana?

:::{admonition} Ratkaisu
:class: tip, dropdown

$P(\text{moottorivika})=\frac{2}{1000}=0.002=0.2 \%$

:::