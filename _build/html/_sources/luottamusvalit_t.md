# t-jakauman luottamusvälit

Kun otoskoko on pieni ja kun populaation mitattavan ominaisuuden keskihajontaa ei tiedetä, pitää käyttää jotain muuta jakaumaa kuin normaalijakaumaa. Yleisesti käytetty vaihtoehto on nimeltään [t-jakauma](https://fi.wikipedia.org/wiki/Studentin_t-jakauma). Sen muoto riippuu otoskoosta, mikä näkyy alla olevassa kuvassa.

![t-jakauma](t_jakauma.png "t-jakauma")

Kuva: By Skbkekas - Own work, CC BY 3.0, [vasen](https://commons.wikimedia.org/w/index.php?curid=9546828), [oikea](https://commons.wikimedia.org/w/index.php?curid=9546841)

Koska t-jakauman tiheysfunktio on seuraava: $f(x)=\frac{\Gamma((\nu+1)/2)}{\sqrt{\nu \pi}\Gamma(\nu/2}(1+x^2/\nu)^{-(\nu+1)/2}$,
 
missä $\Gamma(r)=\int_0^{\infty} x^{r-1}e^{-x}~\text{d}x$,
  
niin sitä ei ole ainakaan tällä opintojaksolla tarkoituskaan käsitellä muutoin kuin tietokoneella valmiiden funktioiden avulla. 

Parametri, joka määrittää t-jakauman muodon, on vapausaste $f$. Kun havaintojen lukumäärä on $n$ ja niiden keskiarvo $\bar{X}$ on määritetty, on laskennassa vapaiden muuttujien lukumäärä $f = n - 1$, sillä keskiarvoa laskettaessa menetetään yksi vapausaste (eli kun keskiarvo on määritetty, vain $n-1$ muuttujaa voivat vaihdella vapaasti, "$n$:nnen" muuttujan arvo on tällöin sidottu). Otoskoon kasvaessa funktion kuvaajan muoto lähenee normaalijakauman muotoa.

Excelissä t-jakaumaan liittyvät funktiot ovat nimeltään T.JAKAUMA ja T.KÄÄNT. On olemassa myös funktiot T.JAKAUMA.2S ja T.KÄÄNT.2S, joissa loppupääte 2S viittaa kaksisuuntaisuuteen. Näitä kaksisuuntaisia funktioita käytettäessä todennäköisyydeksi merkitään jakauman kumpaankin päähän jäävien alueiden prosenttiosuuksien summa. Esimerkiksi jos haetaan luottamusväliä luottamustasolla 90 %, niin luottamusvälin ylä- ja alaraja löytyvät 5 % ja 95 % todennäköisyyksien kohdalta samalla tavalla kuin normaalijakaumassakin. 

Esimerkkinä jakauma, jonka vapausaste on 6:

Alaraja T.KÄÄNT(5%;6), tulos -1.94
Yläraja T.KÄÄNT(95%;6), tulos 1.94

Kaksisuuntaista funktiota käytettäessä tulee parametriksi $100~\%-2\cdot 5~\%=90~\%$, ja sekä ala- että ylärajalle saadaan itseisarvo komennolla T.KÄÄNT.2S(10%;6), tulos 1.94.

Koska t-jakauma on normitettu siten, että sen odotusarvo on 0 ja varianssi 1, niin todellisen virhemarginaalin laskemiseksi pitää vielä kertoa edellä saatu tulos keskiarvon keskivirheellä.

**Esim.** Populaatiosta saadaan seuraava otos: {12.6, 13.4, 12.8, 13.2, 12.8, 13.0, 13.1, 12.8}. 

Muodosta keskiarvon 99 % luottamusväli.

:::{admonition} Ratkaisu
:class: tip, dropdown

Otoskoko on pieni eikä keskihajontaa tiedetä, joten käytetään t-jakaumaa vapausasteella $8-1=7$.

Luottamustaso on 99 %, joten kuvaajan päihin jää yhteensä 1 %, jolloin haluttu yläraja on 99.5 % kohdalla.

Lasketaan tarvittavia lukuja: otoksen keskiarvo 12.9625, otoksen keskihajonta 0.26152, keskiarvon keskihajonta 0.0924614. Nämäkin laskut kannattaa tehdä Excelillä.

Luottamusväli: T.KÄÄNT(0,995;7), tulos 3.499,

Virhemarginaali: $\Delta=3.499\cdot 0.0924613=0.3236 \approx 0.32$.

Keskiarvon 99 % luottamusväli on siis $(12.96 - 0.32,12.96 + 0.32) = (12.64,13.29)$

:::