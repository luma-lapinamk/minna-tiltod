---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
  
---

# Kahden otoksen vertailu

Usein tilastollisissa tutkimuksissa on selvitettävä, poikkeavatko kaksi erillistä ryhmää toisistaan merkittävästi jonkin mitatun ominaisuuden suhteen. Esimerkiksi voitaisiin valita ryhmä insinööriopiskelijoita ja ryhmä tradenomiopiskelijoita. Kummaltakin ryhmältä mitattaisiin verenpaine, ja sitten ryhmien keskiarvoja verrattaisiin toisiinsa. Voitaisiinko tällaisen kokeen perusteella uskottavasti sanoa, että alojen opiskelijoiden verenpaineet poikkeaisivat toisistaan? Vastaus riippuu siitä, miten kaukana toisistaan otosten keskiarvot ovat, millaiset ovat otoskoot ja millainen on otosten hajonta.


```{code-cell} ipython3
:tags: [hide-input, hide-output, thebe-init]

# kaksi normaalijakaumaa

import matplotlib.pyplot as plt
import numpy as np
import math
import ipywidgets as widgets



def verenpaine_interaktiivisesti():
    interactive_plot = widgets.interactive(verenpaineet, mu1=widgets.FloatSlider(value=135, min=100, max=200, step=5, description = "$\mu_1$"),
                                           variance1=widgets.FloatSlider(value=30, min=10, max=100, step=5, description = "$\sigma_1$"), 
                                           mu2=widgets.FloatSlider(value=145, min=100, max=200, step=5, description = "$\mu_2$"),
                                           variance2=widgets.FloatSlider(value=40, min=10, max=100, step=5, description = "$\sigma_2$"))                        
    return interactive_plot


def verenpaineet(mu1,mu2,variance1,variance2):
    x = np.linspace(100, 200, 100)
    sigma1 = math.sqrt(variance1)
    sigma2 = math.sqrt(variance2)
    prob_density1 = 1/(sigma1*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu1)/sigma1)**2)
    prob_density2 = 1/(sigma2*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu2)/sigma2)**2)
    plt.plot(x, prob_density1, color="red")
    plt.plot(x, prob_density2, color="green")
    plt.xlabel("Verenpaine")
    plt.show()

```

Osoita hiirellä raketin kuvaa ja valitse "Live Code". Sen jälkeen paina Run!

```{code-cell} ipython3

interaktiivinen_graafi = verenpaine_interaktiivisesti()
interaktiivinen_graafi

```

## Riippumattomien otosten testi

Edellinen esimerkki on tilastotieteen termein ilmaistuna riippumattomien otosten testi. Riippumattomuus merkitsee tässä sitä, että mikään ryhmän jäsen ei saa kuulua molempiin ryhmiin. Sama henkilö ei siis esimerkissä voi opiskella molemmilla aloilla. Ryhmät muodostetaan usein  sukupuolen (mies/nainen) perusteella.

Riippumattomien otosten testi on järkevä, jos seuraavat asiat toteutuvat:
- mitatun ominaisuuden pitää olla vähintään välimatka-asteikolla mitattu
- mitatun ominaisuuden pitää olla normaalisti jakautunut molemmissa ryhmissä, ja niiden hajonnan tulisi olla samaa luokkaa
- otoskoko on kohtalaisen suuri (ainakin 20/ryhmä)

Hypoteesi on tutkimustulokselle asetettu ennakko-oletus, jota merkitään symbolilla $H_0$. Tarkemmin tällä tarkoitetaan ns. nollahypoteesia eli sitä, että ryhmillä ei ole mitään tilastollisesti merkitsevää eroa. Esimerkin kaltaisessa riippumattomien otosten testissä $H_0$ voidaan esittää vaikkapa muodossa "verenpaineiden keskiarvot eivät eroa merkittävästi".

Kun nollahypoteesi on asetettu, on seuraava vaihe tarkistaa laskennallisesti, pitääkö hypoteesi paikkansa. Tulos etsitään niin kutsutulla kahden otoksen t-testillä.


## Testisuureen laskeminen

Riippumattomien otosten testissä käytettävä suure, ns. t-arvo, lasketaan seuraavasti:

$\Large{t=\frac{\bar{x_1}-\bar{x_2}}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}}}$,

missä $\bar{x_1}$ on ryhmältä 1 mitatun suureen keskiarvo ja $\bar{x_2}$ vastaavasti ryhmältä 2 mitatun suureen keskiarvo, $s_1$ ja $s_2$ ovat ryhmien 1 ja 2 mittaustulosten keskihajonnat, ja $n_1$ ja $n_2$ ovat ryhmien 1 ja 2 koot.

Testisuureen $t$ perusteella tehdään päättely valitun merkitsevyystason $\alpha$ mukaisesti seuraavasti:

1) Etsitään normaalijakauman $N(0,1)$ valittua merkitsevyystasoa $\alpha$ vastaava kriittinen z-arvo $z_{\alpha}$, tai jos otoskoot ovat niin pieniä että normaalijakauman sijasta pitäisi käyttää t-jakaumaa, etsitään jakauman $t(n_1+n_2-2)$ pinta-alaa $\alpha$ vastaava kriittinen t-arvo $t_{\alpha}$.
2) Jos testisuure on suurempi kuin $z_{\alpha}$ (tai $t_{\alpha}$), on ero tilastollisesti merkittävä. Tällöin hypoteesi $H_0$ hylätään ja voidaan sanoa, että ryhmillä todella on eroa mitatun suureen suhteen.

Monet tilastollisten ohjelmien t-testin funktiot palauttavat testille ns. p-arvon. Se on t-arvon rajaaman, 0:sta kauempana olevan pinta-alan suuruus eli todennäköisyys, että laskettu tulos saataisiin täysin sattumalta. Tilastollinen päättely tehdään nyt suoraan valitun merkitsevyystason mukaisesti. Jos p-arvo on pienempi kuin $\alpha$, on ero tilastollisesti merkittävä, jolloin hypoteesi $H_0$ hylätään.

**Esim.** Kokeessa testattiin uuden lannoitteen vaikutusta hedelmäpuun satoon. Ryhmä 1, johon kuului 50 kasvia, ravittiin tällä uudella lannoitteella. Ryhmä 2, johon kuului 60 kasvia, sai vanhaa lannoitetta. Koejakson jälkeen kummankin ryhmän kasvien sato punnittiin.  Lannoitetta saaneella ryhmällä sadon keskipaino oli 2.4 kg ja keskihajonta 0.6 kg, kun taas kontrolliryhmällä keskipaino oli 2.1 kg ja keskihajonta 0.8 kg. Vaikuttaako uusi lannoite sadon määrään?

:::{admonition} Ratkaisu
:class: tip, dropdown

Asetetaan nollahypoteesi: $H_0 = $ "keskipaino ei eroa merkittävästi". Tutkitaan tilannetta 95 % merkitsevyystasolla.

Lasketaan aluksi testisuure t:

$\Large{t=\frac{2.4~\text{kg}-2.1~\text{kg}}{\sqrt{\frac{(0.6~\text{kg})^2}{50}+\frac{(0.8~\text{kg})^2}{60}}}}=2.244$

Vertailuarvoksi tarvitaan normaalijakaumasta $N(0,1)$ luvua 0.975 vastaava arvo. Tämä saadaan esim. Excelissä komennolla =NORM.S.INV(0,975), josta tuloksena on 1.960. Koska edellä laskettu $t$-arvo on suurempi kuin tämä, niin hypoteesi $H_0$ hylätään. Toisin sanoen uusi lannoite vaikuttaa sadon määrään.
:::