# Prosenttiosuuden luottamusväli

[Helsingin Sanomat](https://www.hs.fi/politiikka/art-2000008778872.html) uutisoi 28.4.2022, että 65 % suomalaisista haluaisi Suomen liittyvän Natoon. Uutisessa kerrotaan, että kyselyyn vastasi 1062 henkilöä, jotka edustavat 18-79-vuotiaita suomalaisia. Uutisen mukaan kyselyn  tuloksen virhemarginaali on 3 prosenttiyksikköä suuntaansa. Ei siis voida 100 % varmuudella sanoa, että tarkalleen 65 % suomalaisista kannatti tuolloin Natoon liittymistä. Voidaan kuitenkin 95 % varmuudella sanoa, että 61-68 % suomalaisista kannatti Natoon liittymistä.

Oletetaan, että tietyn ominaisuuden osuus $p$ populaatiosta, jossa on $n$ alkiota, noudattaa todennäköisyysjakaumaa $\text{Bin}(p,n)$. Kun $np \geq 5$ ja $n(1-p) \geq 5$, binomijakauma voidaan korvata normaalijakaumalla $N\left(np,\sqrt{np(1-p)}\right)$.

Kun populaatiosta otetaan otos, ja lasketaan sille vastaava otosprosenttiosuus, noudattaa se normaalijakaumaa 

$N\left(np,\sqrt{\frac{p(1-p)}{n}}\right)$.

Keskiarvon keskivirhettä vastaava otosprosenttiosuuden keskivirhe on yllämainitun normaalijakauman keskihajonta 

$s=\sqrt{\frac{p(1-p)}{n}}$

Populaation prosenttiosuutta $p$ ei useinkaan tiedetä, mutta kun otos on riittävän suuri, voidaan $p$ korvata otosprosenttiosuudella $p_s$. Tällöin saadaan prosenttiosuuden luottamusväliksi

$(p_s-\Delta, p_s+\Delta)$

missä 

$\Delta = z_c \sqrt{\frac{p_s(1-p_s)}{n}}$

ja $z_c$ on valittua luottamustasoa vastaava muuttujan arvo jakaumasta $N(0,1)$.

**Esim.** Otantaan satunnaisesti valituista 850 suomalaisesta 452:lla oli siniset silmät. Laske 95 % luottamustasolla, kuinka monella prosentilla kaikista suomalaisista on siniset silmät.

:::{admonition} Ratkaisu
:class: tip, dropdown

Sinisilmäisten suhteellinen osuus aineistosta on $p_s=\frac{452}{850}=0.5317$

Keskihajonta on $s=\sqrt{\frac{0.5317(1-0.5317)}{859}}=0.0171$

Lasketaan $z_c$ luottamustasoa 95 % vastaava arvo normitetusta normaalijakaumasta: 

Excel NORMAALI.JAKAUMA.KÄÄNT(97,5%;0;1), tulos 1.96

Virhemarginaali on siis $\Delta = z_c \cdot s = 1.96\cdot 0.0171=0.034=3.4~\%$

Luottamusväli on siis $(53.2~\% - 3.4~\%, 53.2~\% + 3.4~\%) = (49.8~\%, 56.6~\%)$.

:::
