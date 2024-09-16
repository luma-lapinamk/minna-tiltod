# Kombinatoriikkaa

Kombinatoriikka tarkastelee sitä, kuinka monella tavalla ja kuinka monessa eri järjestyksessä jostakin joukosta voidaan ottaa tietyn suuruinen osajoukko. Selvitetään ensin kombinatoriikan peruskäsitteet ja sitten sovelletaan niitä todennäköisyyslaskentaan.

## Permutaatio

Permutaatio on tietyssä järjestyksessä oleva alkioiden joukko, esimerkiksi ruokalaan tietyn ryhmän opiskelijoista muodostuva jono. Mukaan otetaan kaikki kyseisen joukon alkiot eli esimerkin tapauksessa henkilöt. Jos joukossa on $n$ alkiota, niin mahdollisia permutaatioita on $n!$ kappaletta, missä huutomerkki tarkoittaa kertomaa eli tuloa, jossa on mukana luku $n$ ja kaikki sitä pienemmät positiiviset kokonaisluvut. Esimerkiksi luvun $4$ kertoma on $4!=4\cdot 3\cdot 2 \cdot 1 =24$.

Jonon muodostuksen tapauksessa luvut, jotka muodostavat kertoman, vastaavat sitä kuinka monta vaihtoehtoa jonoon saapuville henkilöille on olemassa. Jos ryhmässä on neljä henkilöä, niin kuka tahansa heistä voi mennä jonon ensimmäiseksi. Seuraavalle paikalle tulee joku kolmesta muusta, seuraavalle paikalle on jäljellä kaksi vaihtoehtoa, ja viimeiselle paikalle jää tietenkin vain yksi mahdollinen henkilö.

Yleisesti laskukaava on

$n!=n\cdot (n-1)\cdot (n-2)\cdot \ldots \cdot 1$

Excelissä $n!$ lasketaan funktiolla KERTOMA.

**Esim.** Kuinka monella eri tavalla 12 ihmistä voi asettua jonoon?

:::{admonition} Ratkaisu
:class: tip, dropdown

$12!=12\cdot 11\cdot \ldots \cdot 2\cdot 1=479 001 600$

:::

## k-permutaatio

On mahdollista, että $n$ alkion joukosta valitaankin vain $k$:n alkion joukko. Esimerkiksi ruokajonoon meneekin vain osa ryhmän jäsenistä. Aluksi tarkastellaan tilannetta, jossa alkioiden järjestyksellä on merkitystä. Tällaiset järjestetyt osajoukot ovat nimeltään $k$-permutaatioita. Periaate on sama kuin edellä: esimerkiksi 8 henkilön ryhmästä ensimmäiselle paikalle on 8 vaihtoehtoa, toiselle 7, kolmannelle 6, ja niin edelleen. Kertolasku vain täytyy katkaista sopivasta kohdasta. Jos syömään lähtijöitä 8 henkilöstä olisi vain 3, niin mahdollisia järjestyksiä olisi \(8\cdot 7 \cdot 6\).

Matemaattisesti kertolaskun katkaisu onnistuu siten, että kertolasku muutetaan murtolausekkeeksi, jossa osoittajassa kertolaskua jatketaan numeroon 1 saakka kertoman määritelmän mukaisesti, ja nimittäjään kirjoitetaan sopiva kertolasku jolla yläpuolen kertolasku kumoutuu. Näin saadaan katkaistu kertolasku esitettyä kahden kertoman osamääränä.

Esimerkki:

$(8\cdot 7 \cdot 6 = frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}=\frac{8!}{5!}$

Yleisesti jos joukossa on $n$ alkiota, niin mahdollisten $k$-permutaatioiden määrä on

$n(n-1)\cdot \ldots \cdot (n-k+1)=\frac{n!}{(n-k)!}$

Excelissä osamäärä $\frac{n!}{(n-k)!}$ voidaan laskea suoraan funktiolla PERMUTAATIO.

**Esim.** Kuinka monta kolmen ihmisen jonoa voidaan muodostaa 12 ihmisen joukosta? 

:::{admonition} Ratkaisu
:class: tip, dropdown

$\frac{12!}{(12-3)!}=\frac{12!}{9!}=\frac{12\cdot 11 \cdot \ldots \cdot 2\cdot 1}{9\cdot 8\cdot \ldots \cdot 2 \cdot 1}=12\cdot 11\cdot 10=1320$

:::

## k-kombinaatio 

Kun $n$ alkion joukosta valitaan $k$:n alkion joukko, jossa alkioiden järjestyksellä ei ole merkitystä, kyse on $k$-kombinaatiosta. Tällöin ei siis olla jonossa, vaan vapaamuotoisessa porukassa. Näin ollen joukkojen määrä lasketaan siten, että edellisessä tapauksessa laskettujen järjestettyjen osajoukkojen määrä jaetaan sillä, kuinka monta erilaista jonoa joukosta on mahdollista muodostaa, eli osajoukon koon $k$ kertomalla.

Jos joukossa on $n$ alkiota, niin mahdollisten $k$-kombinaatioiden määrä on siis

$\frac{n!}{k!(n-k)!}$

Kaava $\frac{n!}{k!(n-k)!}$ kirjoitetaan lyhyemmin muodossa $\binom{n}{k}$ ja sitä kutsutaan binomikertoimeksi "n yli k:n". Excelissä laskun voi suorittaa funktiolla KOMBINAATIO.

**Esim.** Kuinka monta erilaista kolmen oppilaan ryhmää voidaan muodostaa 12 oppilaasta?

:::{admonition} Ratkaisu
:class: tip, dropdown

$\frac{12!}{3!\cdot (12-3!)}=\frac{12!}{3!\cdot 9!}=\frac{12\cdot 11 \cdot \ldots \cdot 2\cdot 1}{3\cdot 2\cdot 1 \cdot 9 \cdot 8 \cdot \ldots \cdot 2 \cdot 1)}=\frac{12\cdot 11 \cdot 10}{3\cdot 2\cdot 1}=220$

:::


## Esimerkkejä

Kombinatoriikkaa voidaan hyödyntää todennäköisyyslaskennassa seuraavien esimerkkien mukaisesti.

**Esim.** Karkkipussissa on 5 sinistä ja 3 punaista karkkia. Pussista otetaan neljä karkkia kerralla. Millä todennäköisyydellä saadaan 2 sinistä ja 2 punaista?
 
Lasku ratkeaa seuraavalla periaatteella:

$P(\text{2 punaista ja 2 sinistä})=\frac{\text{haluttujen kombinaatioiden määrä}}{\text{kaikkien 4 karkin kombinaatioiden määrä}}$,

missä haluttujen kombinaatioiden määrä muodostuu kertolaskulla eri vaihtoehtoihin liittyvistä kombinaatioista.

:::{admonition} Ratkaisu
:class: tip, dropdown

Suotuisten kombinaatioiden määrä voidaan päätellä seuraavasti: valitaan viidestä sinisestä mitkä tahansa 2 ja kolmesta punaisesta mitkä tahansa 2, siis

$\binom{5}{2}\cdot \binom{3}{2}$.

Neljän karkin kombinaatioita kahdeksasta on yhteensä $\binom{8}{4}$.

Siis $P(\text{2 punaista ja 2 sinistä})=\frac{\binom{5}{2} \binom{3}{2}}{\binom{8}{4}}$

Lasku suoritaan Excelillä komennolla: 

KOMBINAATIO(5;2)\*KOMBINAATIO(3;2)/KOMBINAATIO(8;4), tulos: 0.43 = 43 %

:::

**Esim.** Lotossa arvotaan 7 lukua satunnaisesti lukujen 1-40 joukosta. Pelaaja valitsee 7 lukua.

a) Kuinka monta erilaista lottoriviä on olemassa?

b) Kuinka suuri on todennäköisyys saada 7 oikein? 

c) Laske todennäköisyydet Loton pienemmille voitoille: 6, 5 ja 4 oikein. 

:::{admonition} Ratkaisu
:class: tip, dropdown

a) Lukujen järjestyksellä ei ole väliä, joten kyseessä on 7-kombinaatio $\binom{40}{7}$.

Excel: =KOMBINAATIO (40;7), vastaus 18 643 560

b) Rivejä, joissa on 7 oikeaa lukua, on vain yksi, joten 

$P(\text{7 oikein})=\frac{1}{18 643 560}=0.000005~\%$.

c) Oikeita lukuja on 7 ja ”vääriä” lukuja 40 – 7 = 33. Valitaan siis 6, 5 tai 4 lukua oikeiden 7 luvun joukosta ja loput 1, 2 tai 3 lukua 33 väärän luvun joukosta.

$P(\text{6 oikein})= \frac{\binom{7}{6}\binom{33}{1}}{\binom{40}{7}}=0.001~\%$,

$P(\text{5 oikein})= \frac{\binom{7}{5}\binom{33}{2}}{\binom{40}{7}}=0.06~\%$,

$P(\text{4 oikein})= \frac{\binom{7}{4}\binom{33}{4}}{\binom{40}{7}}=1.02~\%$.

:::