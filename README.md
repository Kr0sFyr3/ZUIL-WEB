# Code Contract

## Gemaakt door Robin Muijs voor de webapplicatie van ZUIL uitleen

 Hierin hebben wij onze afspraken staan over hoe wij te werk gaan met onze code. Wij zijn hier in overleg tot gekomen en staan hier allebei achter. We hebben samen alle onderstaande onderwerpen besproken en zijn samen tot het volgende contract gekomen.

---

## Inhoud

1. Afspraken naamgevingen
2. Styles van naamgevingen
3. GIT en project structuur
4. Ontwerp
5. Taal
6. Inspringen
7. Wit regels
8. Maximum regel lengte

---

### Afspraken naamgevingen

> Voor de Naamgevingen hebben we de afsrpaken gemaakt om gebruik te gaan maken van camelCasing voor de variabelen. We zullen voor functies en classes gebruik gaan maken van PascalCasing. We hebben voor deze optie gekozen om gemakkelijk onderscheidd te kunnen maken tussen variabelen en classes/functies.

---

### Styles van naamgevingen

> Voor de style van naamgevingen gaan wij gebruik maken van een aantal regels:

> - We gaan geen gebruik maken van afkortingen om zo de leesbaarheid te verhogen en verwarring te voorkomen. **Voorbeeld: employeeId ipv eId**
> - We zullen variabelen gehele namen geven om zo duidelijk onderscheid te houden. **Voorbeeld: employeeName ipv Name**
> - We zullen in loops wel gebruik maken van eenletterige variabelen zodat deze niet in zoekvelden naar voren komen en verwarring veroorzaken.
> - We gaan geen gebruik maken "\_" in naamgevingen.
> - Voor functies zullen we gebruik maken van werkwoorden in de naamgevingen zodat er een duidelijk is tussen klasses en functies.
> - Code schoon houden en geen gebruik maken van onzin naamgevingen die grappig bedoeld zijn. **Voorbeeld: GetBalance() ipv ShowMeTheMoney()**

---

### GIT en project structuur

> Voor GIT hebben wij een aantal regels opgesteld waar wij ons beiden aan zullen moeten houden om een duidelijke structuur te behouden:
>
> - We zullen iedere commit koppelen met de jira task die erbij hoort. **Voorbeeld: BP5OT01-28 Scorepage-frontend 2.0**
> - We zullen gebruik maken van GitHub Desktop.
> - We zullen gebruik maken van versiebeheer. Hierbij word de versie verhoogt met 1.0 tot gehele getallen. **Voorbeeld: 1.0 -> 2.0 ... -> 1.1.0**
> - We zullen bij onze branches naamgevingen hanteren als volgt: featurenaam + front/backend. **Voorbeeld: Homepage-frontend**
> - We zullen bij onze commits naamgevingen hanteren als volgt: featurenaam + versienummer. **Voorbeeld: Homepage-frontend1.0 -> Homepage-frontend2.0**
> - We zullen bij onze commits ook commentaar leveren over welke veranderingen zijn doorgevoerd.

---

### Ontwerp

> Voor onze code gaan wij gebruik maken van static code omdat wij hier allebei meer kennis in hebben en het makkelijker toe zullen kunnen passen.

---

### Taal

> Onze applicatie zullen we volledig in het engels gaan ontwikkelen. Hierbij zullen we zowel code als commentaar in het engels schrijven.

---

### Inspringen

> Voor het inspringen bij een functie openen we de functie **{** op dezelfde lijn als de functienaam.
> Het sluiten van een functie doen we op een aparte regel. **}**
> De inhoud van een functie zullen we door middel van 1 tab indenteren.

---

### Wit regels

> Voor het project hebben wij afgesproken om 1 witregel tussen functies in te zetten.
> Binnen een functie zullen witregels gebruikt worden op de manier dat de code overzichtelijk blijft. Bijvoorbeeld denk aan het scheiden van variabelen of statements.

---

### Maximum regel lengte

> In het project zullen wij de maximum regel lengte houden op 120 tekens.
