# Peruskäsitteitä

Aiemmin on jo todettu, että kun havainnoitava perusjoukko eli populaatio on hyvin suuri, käytetään otantaa haluttaessa arvioida populaation ominaisuuksia. Esimerkiksi jos halutaan selvittää suomalaisten keskimääräistä viikoittain liikuntaan käytettyä aikaa, ei käydä kysymässä asiaa jokaiselta erikseen, vaan valitaan tutkimukseen joukko, jonka perusteella tulos voidaan yleistää. Ideaalisin otantamenetelmä on satunnaisotanta, jossa jokainen perusjoukon jäsen voidaan valita yhtä todennäköisesti otokseen.

Tilastotieteessä pätevät seuraavat säännöt: 

1. Jos populaatiosta, jonka mitatut arvot voivat olla miten tahansa jakautuneet, otetaan kaikki mahdolliset osajoukkojen kombinaatiot ja lasketaan näiden osajoukkojen keskiarvojen keskiarvo, se on aina sama kuin populaation keskiarvo, vaikka yhden osajoukon keskiarvo voi erota siitä hyvinkin suuresti. 

2. Riippumattomasti valittujen otosten keskiarvojen $\mu_i$ muodostama jakauma on normaalisti jakautunut riippumatta siitä, onko populaatiossa kyseinen ominaisuus normaalisti jakautunut vai ei.

## Keskeinen raja-arvolause

Merkitään: $X$ on jokin populaation (mitattava) ominaisuus ja $X_i$:t ovat populaatiosta riippumattomasti mitattuja havaintoja muuttujasta $X$. Merkitään lisäksi: populaation keskiarvo on $\bar{X}$, keskihajonta on $\sigma$ ja varianssi on $\sigma^2$.

Keskeisen raja-arvolauseen mukaan havaintojen keskiarvo $\bar{X}$ on normaalisti jakautunut keskiarvona $\mu$ ja keskihajontana $\frac{\sigma}{\sqrt{n}}$, siis

$\bar{X}=\frac{1}{n} \sum_{i=1}^n X_i \sim N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$.

Toisin sanoen minkä tahansa jakauman otoskeskiarvot noudattavat normaalijakaumaa, jolloin populaation keskiarvoon liittyvissä tilastollisissa päättelyissä voidaan käyttää normaalijakaumaa. Lisäksi otoskeskiarvot ovat jo suhteellisen pienillä määrillä normaalisti jakautuneet, jolloin populaation keskiarvosta saadaan luotettavia estimaatteja.

Usein perusjoukon keskihajonta $\sigma$ ei ole tiedossa eikä sitä voida selvittää. Sen sijaan otoksesta keskihajonta on helppoa laskea. Tällöin populaation keskihajontaa arvioidaan otoskeskihajonnalla

$s=\sqrt{\frac{\sum_{i=1}^n (X_i-\bar{X})^2}{n-1}}$

 
## Keskiarvon keskivirhe

Keskiarvojen keskihajontaa $\frac{\sigma}{\sqrt{n}}$ kutsutaan keskiarvon keskivirheeksi (standard error, SE). Sitä käytetään, kun halutaan  muodostaa otoksen perusteella jollekin perusjoukon ominaisuudelle arvio virherajoineen. Otoksen keskivirheen avulla voidaan laskea todennäköisyys, että populaation keskiarvo $\mu$ on välillä 

$X-\frac{\sigma}{\sqrt{n}} \leq \mu \leq X + \frac{\sigma}{\sqrt{n}}$ 

Koska otoksen keskiarvo noudattaa normaalijakaumaa $N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$, todennäköisyys ylläolevalle voidaan laskea kyseisen jakauman avulla seuraavasti:

$P(X-\frac{\sigma}{\sqrt{n}} \leq \mu \leq X + \frac{\sigma}{\sqrt{n}})=P(-1 \leq z \leq 1)=0.68$,

missä $z \sim N(0,1)$.

Lukua 0.68 tai 68 % kutsutaan luottamustasoksi: siis 68 % luottamustasolla voidaan sanoa, että populaation todellinen keskiarvo on luvun $\frac{\sigma}{\sqrt{n}}$ etäisyydellä otoksen keskiarvosta. Lukuväliä $X-\frac{\sigma}{\sqrt{n}} \ldots \leq X + \frac{\sigma}{\sqrt{n}}$ sanotaan luottamusväliksi.

**Esim.** Tehtaassa valmistettavien jauhopussien painolle haluttiin arvioida virherajat käyttämällä keskiarvon keskivirhettä. Otokseen valittiin satunnaisesti 10 pussia, joiden keskipaino oli 995 g ja keskihajonta 22.6 g. Esitä arvioitu pussin keskipaino virherajoineen.

:::{admonition} Ratkaisu
:class: tip, dropdown

Otoskoko: $n=10$ kpl, otoskeskiarvo: $\bar{X}=995$ g, keskihajonta $\sigma=22.6$ g.

Keskiarvon keskivirhe on $\frac{\sigma}{\sqrt{n}}=\frac{22.6~\text{g}}{\sqrt{10}} = 7.15~\text{g}$.

Keskipaino on siis $\mu=\bar{X} \pm \frac{\sigma}{\sqrt{n}} = 995~\text{g} \pm 7~\text{g}$.

Luottamusväli on noin 988 g ... 1002 g.

:::
 
## Luottamustaso ja virhemarginaalit

Edellä luottamustaso, joka määriteltiin keskiarvon keskivirheen avulla, oli suuruudeltaan 68 %. Tilastollisessa analyysissa halutaan usein arvioida populaation jonkin ominaisuuden keskiarvoa paljon suuremmalla luottamustasolla, esimerkiksi 95 % tai 99 %.

Yleisesti luottamusväliä merkitään $(X-\Delta, X+\Delta)$. Merkintä $\Delta$ on niin sanottu virhemarginaali. Populaation mitattavan ominaisuuden todellinen keskiarvo on siis luottamustason mukaisella todennäköisyydellä enintään virhemarginaalin etäisyydellä otoksen perusteella lasketusta keskiarvosta.

Merkitsevyystasoksi kutsutaan luottamusvälin komplementtitapauksen "luottamusväli ei sisällä perusjoukon keskiarvoa" todennäköisyyttä. Yleensä merkitsevyystasoon viitataan kirjaimella $\alpha$, jolloin luottamustasoa merkitään lausekkeella $1-\alpha$. Luottamustasona hyvin yleisesti käytetään 95 %, jolloin merkitsevyystaso on 5 %. 