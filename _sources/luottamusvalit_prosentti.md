# Prosenttiosuuden luottamusväli

Oletetaan, että tietyn ominaisuuden osuus $p$ populaatiosta, jossa on $n$ alkiota, noudattaa todennäköisyysjakaumaa $\text{Bin}(p,n)$. Kun $n \geq 5$ ja $n(1-p) \geq 5$, niin binomijakauma voidaan korvata normaalijakaumalla 

$N\left(np,\sqrt{np(1-p)}\right)$.  

Kun populaatiosta otetaan otos ja lasketaan sille vastaava otosprosenttiosuus, noudattaa se normaalijakaumaa

$N\left(np, \sqrt{\frac{np(1-p)}{n}}\right)$.  

Keskiarvon keskivirhettä vastaava otosprosenttiosuuden keskivirhe on yllämainitun normaalijakauman keskihajonta 

$s=\sqrt{\frac{p(1-p)}{n}}$.  

Populaation prosenttiosuutta $p$ ei useinkaan tiedetä, mutta kun otos on riittävän suuri, voidaan $p$ korvata otosprosenttiosuudella, jota merkitään tässä $p_s$. Tällöin saadaan prosenttiosuuden luottamusväliksi $(p_s-\Delta, p_s + \Delta)$, missä 
missä 

$\Delta=z_c \sqrt{\frac{p_s(1-p_s)}{n}}$  

ja $z_c$ on luottamustasoa vastaava muuttujan arvo jakaumasta $N(0,1)$.

**Esim.** Otantaan satunnaisesti valituista 850 suomalaisesta 452:lla oli siniset silmät. 
Laske 95 % luottamustasolla, kuinka monella prosentilla suomalaisista on siniset silmät.

:::{admonition} Ratkaisu
:class: tip, dropdown

Sinisilmäisten suhteellinen osuus aineistosta on $p_s=\frac{452}{850}=0.5317$.

Keskihajonta on $s=\sqrt{\frac{p_s (1-p_s)}{n}}= \sqrt{\frac{0.5317\cdot 0.4683}{850}} = 0.0171$.  

Luottamustasoa 95 % vastaava arvo normitetusta normaalijakaumasta saadaan seuraavalla Excel-komennolla:

=NORMAALI.JAKAUMA.KÄÄNT(97,5%;0;1), josta tuloksena on 1.96.

Virhemarginaali on $\Delta = 1.96 \cdot 0.0171 = 0.034 = 3.4 ~\%$.   

Luottamusväli on siis (53.2 % - 3.4 %, 53.2 % + 3.4 %) = (49.8 %, 56.6 %)

:::