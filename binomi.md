# Binomijakauma

Eräs diskreeteistä todennäköisyysjakaumista on binomijakauma. Oletetaan, että suoritetaan toistokoe, jonka "onnistumisen" todennäköisyys on aina (riippumatta edellisistä tuloksista) $p$ ja "epäonnistumisen" todennäköisyys $1-p$. Käsitteillä "onnistuminen" tai "epäonnistuminen" tarkoitetaan tässä mitä tahansa tapahtumia $A$ ja $B$, jotka ovat toisensa poissulkevia ja joista jompikumpi varmasti tapahtuu. Tällöin satunnaismuuttuja $X$, joka kuvaa onnistumisten lukumäärää $n$ toistossa, noudattaa binomijakaumaa. Tätä merkitään $X \sim \text{Bin}(n,p)$.

Todennäköisyys sille, että $n$ toistossa onnistutaan $k$ kertaa, on 

$P(k)=\binom{n}{k} p^k (1-p)^{n-k}$

Kertauksena kombinatoriikasta: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

Kyseinen laskukaava on binomijakauman tiheys- tai todennäköisyysfunktio. Excelissä binomitodennäköisyys voidaan laskea funktiolla BINOMI.JAKAUMA. Funktioon täytyy antaa parametriksi myös se, lasketaanko todennäköisyyttä $P(X=a)$ vai $P(x \leq a)$. Laskun voi tietenkin suorittaa myös KOMBINAATIO-funktiota ja sopivia kertolaskuja yhdistelemällä.

**Esim.** Laske todennäköisyys sille, että saadaan kolmella nopanheitolla 2 kuutosta. 

:::{admonition} Ratkaisu
:class: tip, dropdown

Nyt yritysten määrä on $n=3$, ja onnistumisten määrä on $k=2$. Yksittäisessä yrityksessä onnistumisen, eli kuutosen, todennäköisyys on 1/6, ja epäonnistumisen, eli muun kuin kuutosen, todennäköisyys on 5/6. Todennäköisyys kahdelle kuutoselle on siis 

$\binom{3}{2} \left(\frac{1}{6}\right)^2 \left(1-\frac{1}{6}\right)^{(3-2)}=\frac{3!}{2!1!}\cdot \frac{1}{36}\cdot \frac{5}{6}=\frac{3}{36}\cdot {5}{6}=0.069 = 7~\%$

:::

**Esim.** Oletetaan, että tyttölapsen syntymisen todennäköisyys on 49 %. Laske todennäköisyys sille, että viisilapsisen perheen 
a) kaikki lapset ovat tyttöjä, b) lapsista 3 on poikia ja 2 tyttöjä.

:::{admonition} Ratkaisu
:class: tip, dropdown

Merkitään $X$ = tyttöjen lukumäärä. Toistojen määrä on $n=$5 ja kysytyn lopputuloksen todennäköisyys yhdessä toistossa on $p=0.49$. Tällöin $X \sim \text{Bin}(5,0.49)$.

a) Tässä tilanteessa binomikerroin on $\binom{5}{5}=1$, sillä on vain yksi mahdollinen kombinaatio, jolla viisi viidestä voi olla tyttöjä. Todennäköisyys voidaan siis laskea suoraan seuraavasti:

$P(\text{5 tyttöä})=0.49^5\cdot 0.51^0 = 2.8~\%$

b) $P(\text{2 tyttöä})= \binom{5}{2}\cdot 0.49^2\cdot 0.51^3=31.8~\%$

:::
 
Binomijakamastakin voidaan laskea "ainakin" tai "enintään" -tyyppisiä todennäköisyyksiä. Tällöin tarvitaan kertymäfunktiota. Kun kysytään todennäköisyyttä muodossa "ainakin", kannattaa muistaa komplementtiperiaate.

**Esim.** Tuotteen valmistusprosessissa on seurannassa havaittu, että 0.25 % valmistuneista tuotteista on jollakin lailla viallisia. Asiakas ostaa 1500 kappaleen erän ko. tuotteita. Millä todennäköisyydellä

a) erässä on korkeintaan yksi viallinen tuote?
b) erässä on ainakin yksi viallinen tuote?

:::{admonition} Ratkaisu
:class: tip, dropdown

Satunnaismuuttuja $X$ kuvaa viallisten tuotteiden määrää 1500 kappaleen erässä.

a) $P(\text{"korkeintaan 1 viallinen"}) = P(X=0~\text{tai}~X=1)$

Kyseessä on siis kertymäfunktio $F(1)$, joka määrittelee todennäköisyyden *enintään* yhdelle vialliselle tuotteelle. Voidaan myös laskea tiheysfunktion arvot 0 ja 1 vialliselle ja laskea ne yhteen, sillä kertymäfunktion arvohan lasketaan juuri tällä tavalla tiheysfunktion arvojen summana.

Excel: BINOMI.JAKAUMA(1;1500;0,0025;1), vastaus 0.111

tai: BINOMI.JAKAUMA(0;1500;0,0025;0) + BINOMI.JAKAUMA(1;1500;0,0025;0)

b) Nyt kannattaa käyttää komplementtiperiaatetta, sillä muuten pitäisi erikseen laskea todennäköisyys yhdelle, kahdelle, kolmelle, ... 1500:lle vialliselle tuotteelle.

$P(\text{"ainakin 1 viallinen"}) = 1-P(\text{"ei yhtään viallista"}) = 1- P(X=0) = 1-F(0)$

Excel: 1-BINOMI.JAKAUMA(0;1500;0,0025;0), vastaus 0.977

:::

Binomijakauman odotusarvo ja varianssi lasketaan seuraavasti:

$\mu=np$, $\sigma^2=np(1-p)$

**Esim.** Heitetään kolmea noppaa. Satunnaismuuttuja $X$ ilmoittaa kuutosten lukumäärän. Laske muuttujan odotusarvo ja varianssi.

:::{admonition} Ratkaisu
:class: tip, dropdown

Satunnaismuuttuja $X$ noudattaa binomijakaumaa, missä toistokokeiden lukumäärä on 3, tapahtuma $A$ on ”nopan pisteluku on 6” ja tapahtuman $A$ todennäköisyys yhdessä toistokokeessa on $p=\frac{1}{6}$.

Siis $X \sim \text{Bin}(3, \frac{1}{6})$

Odotusarvo on $\mu=3\cdot\frac{1}{6}=\frac{1}{2}$

Varianssi on $\sigma^2=3\cdot \frac{1}{6}\cdot (1-\frac{1}{6})=\frac{5}{12}$

:::