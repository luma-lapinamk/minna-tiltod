# Mallin arviointi

Selityskerroin $R^2$ on hyvä työkalu lineaarisen mallin pätevyyden arviointiin. Excel laskee $R^2$-arvon myös muunlaisille sovituksille, vaikka luku onkin tarkoitettu kuvaamaan vain lineaarisen mallin sopivuutta dataan.

Epälineaarisissa sovituksissa luotettavampi luku on $S$-arvo, joka on datapisteiden keskimääräinen etäisyys sovitusmallin avulla lasketusta arvosta. Yleensä mitä lähempänä $S$ on nollaa, sitä parempi malli on kyseessä.

On hyvä tarkastella myös residuaaleja eli mallin antaman ja todellisen arvon eroja todellisen arvon funktiona. Jos residuaalit näyttävät satunnaiselta, malli on kelvollinen. Jos taas residuaalit ovat epätasaisesti jakautuneita, malli ei ole hyvä.

Alla on esimerkki residuaalien suuruudesta ja jakaumasta kahdelle eri sovitukselle. Samaan dataan on sovitettu suora (ylävasen) ja toisen asteen polynomifunktio (yläoikea). Lineaarisessa mallissa residuaalit (alavasen) ovat suurempia kuin polynomimallissa (alaoikea). Polynomimallissa residuaalit ovat jakautuneet tasaisemmin kuvaajan alueelle. Polynomin voi ylärivin kuvia katsomalla arvatakin datalle paremmin sopivaksi malliksi, mutta residuaalien avulla väitteelle saa matemaattista tukea ja uskottavuutta.

![Residuaalit](residuaalit.png "Residuaalit")