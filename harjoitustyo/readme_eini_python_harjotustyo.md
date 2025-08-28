#Yritysanalyysi: Kannattavuus ja Vakavaraisuus

Tekijä: Eini Leäslampi
Päivämäärä: 31.7.2025
Curssi:Ohjelmoinnin perusteet TT00CD77-3012/Jamk

##Linkki toteutukseen

[GitLab-projektin URL tähän]

##Tehtävän kuvaus

Toteutin ohjelman, joka tutkii yritysten kannattavuutta ja vakavaraisuutta CSV-tiedostosta saatavan datan perustella. 
Ohjelman ideana on  mahdollistaa toimialakohtaisen suodatuksen ja yritysten taloudellisen toiminan arvionti painotetun pisteluvun (score) perusteella.
Score -arvo syntyy kuvitteelllisten yritysten talousdatasta saatavien kannavuuden (paino 60% arvostaan) ja vakavaraisuuden (paino 40% arvostaa) pisteluvun arvona.
Lisäksi ohjelma näyttää käyttäjälle myös ratig -arvon, jolloin käyttäjä näkee suoraan luokituksen (Erinomainen score >= 0.71/vihreällä värillä,
Hyvä score >= 0,51 vaalean sinisellä värillä, kohtalainen score >= 0.39 kkeltaisella värillä ja heikko  score < 0.39 punaisella värillä
Karkealla tasolla tämä ohjelman olisi kohdennettu sijoitus, vakuutus,luottotoiminnan pohjatidoiksi päätöksen teon tueksi.
Nykyisin käytössäolevat vastaavanlaiset ohejlmat ovat paljon edistyksellisempi, mutta koska tämä on ohjelmoinnin peruskursi, niin en osannut tehdä vielä
haastavampia analyyseja.

##Käytännön toteutus

Käyttäjältä pyydetään CSV-tiedoston polku, josta tiedosto haetaan. Tiedotopolku tallennetaan muuttujaan nimeltä file_path.
Samalla strip() metodilla poistetaan kaikki ylimääräiset tyhjät merkit annetun tiedostopolun alusta ja lopusta, jotta tiedostopolku olisi varmasti oikein.
Tämä varmistaa, että tiedosto voidaan myöhemmin avata ilman virheitä.

Luodaan tyhjät listat, jotka vastaavat CSV-tiedoston sarakkeita vasemmalta oikealle. Sarakkeiden järjestystä ei saa muuttaa, jotta ohjelma toimii oikein myös 
uusilla CSV-tiedostoilla. Jokaisen sarakkeen nimeä vastaava muuttuja tallentaa yritysten vastaavia tietoja.
Näitä tietoja käytetään myöhemmin laskentaan ja analyysiin kuten yritysten tunnuslukujen laskentaan tai vertailuun yritysten välillä.

unktiolla clean_float puhdistetaan teksti ja muutetaan tekstimuotoinen lukuarvo desimaaliluvuksi (float).
Funktio ottaa yhden parametrin, value, joka on merkkijono (string) CSV-tiedoston sisällöstä.
Se yrittää poistaa ei-numeeriset merkit, kuten välilyönnit, erikoismerkit ja pilkut, ja muuntaa arvon desimaaliluvuksi.
Jos muunnos epäonnistuu, funktio palauttaa oletusarvoksi 0.0.
Tämä estää ohjelman kaatumisen virheeseen ja mahdollistaa tietojen käsittelyn myös puutteellisissa aineistoissa.

Funktio raiting_score luokittelee annetun numeerisen arvon (välillä 0–1) laadulliseen kategoriaan. Luokittelu perustuu arvon suuruuteen, ja 
tuloksena saadaan sanallinen arvio, joka ilmaisee arvon tason värikoodattuna:

•  Erinomainen → vihreä
•  Hyvä → vaaleansininen
•  Kohtalainen → keltainen
•  Heikko → punainen

open funktio avaa tiedoston, jonka polku on tallennettu file path muutujaan aikaisemmin, käsittelle rivivahdot ja lukee tiedooton UTF-8 -mallin mukaisesti ja
tallentaa tiedot csvfile muuttujaan, jota käytetään myöhemmässä vaiheessa. Sulkee tidoston, kun se on luettu.

Reader objektin avulla luetaan CSV-tiedoston rivejä ja ne luetaan sanakirjoina sekä erottelee sarakkeet puolipisteellä. 
reader.fieldnames on lista, joka sisältää CSV-tiedoston sarakkeet, jotka puhdistetaan poistamalla niistä ylimääräiset välilyönnit ja suodattamalla pois tyhjät nimet.
Käydään läpi jokainen rivi CSV-tiedostossa. Sarakenimien avulla haetaan tiedosta rivikohtaisesti kaikki tiedot ja siisti sekä yhtenästä sarakekohtaiset rivitiedot. Lisää lopuksi tiedon sarakkeittain listoihin. 
Kakki listat sisältävät kaikki CSV-tiedon tiedot. 
 
Luodaan sanakirja "Industry_codes", johon on tallennut toimialat ja niitä kuvaavat tunnisteet.
Pyydetään käyttäjää valitsemaan toimialat antamalla toimialojen esimmäisen kijaimen tai kaikki toimialat (erotetaan toimialat ",", kovataan välilyönnit ja muutetaan syöte aina isoiksi kirjaimiksi sekä tarkistetaan, että syöte on halutun mukainen. 
Jos käyttäjä antaa virheellisen arvon, niin käyttäjää ohjeistetaan lisää ja pyydetään uudelleen syöttämään toimialat, joita hän haluaa tarkastella. Tämä toistuu kunnes, käyttäjä antaa kelvollisen syötteen ja jatketaan eteenpäibn koodissa näyttäen,
ne toimialat, jotka käyttäjä on valinnut tarkasteltavaksi.

Selected_industries Muuttuja sisältää listan toimialoista käyttäjän valinnan perustella.

Luodaan lista "Company_analysis", joka käy läpi kaikki yritykset ja laskee kannattavuuden ja vakavaraisuuden niille, jotka kuuluvat valittuihin toimialoihin (selected_industries).
Tulokset tallennetaan kahden desimaalin tarkkuudella listaan company_analysis.

Tulostetaan taulukko f-string-muotoilulla, jossa sarakkeet ovat kiinteälevyisiä ja vasemmalle tasattuja. Numerot esitetään kahden desimaalin tarkkuudella. käyttäjän valitsemien toimialojen yritysten kannattavuudesta ja vakavaraisuudesta.

Kysytään käyttäjältä, haluaako hän nähdä yritykset paremmuusjärjestyksessä Score-arvon perusteellaKäyttäjän antama syöte muutetaan aina isoksi kirjaimeksi. Vastauksen perusteella joko suljetaan ohejelma, 
jos käyttäjä vastaa E eli ei. Jos käyttäjä vastaa k =kyllä siirrytään koodissa eteenpäin.

Määritetään kannataavuuden ja vakavaraisuuden panotukset "score" -arvossa. Lasketaan "score" arvo kaikille yrityksille 2-desimaalin tarkkuudelle ja tallennetaan se yrityksen tietohin. 
Rating score funktio antaa "score" -arvolle aiemmmin määritetyn luokituksen (rating_score -funktio).

Lajitellaan yritykset "rating" sarakkeeseen paremmuusjärjestykseen korkeimmasta "score" -arvosta laskevasti. Tulostetaa tulokset taulukkona edellä mainitun "score" -arvon mukaisesti ja tulotetaan taulukko samoilla muotoillulla ja tiedolla lisättynä "Score" ja "Rating" -arvoilla.  
##Sovelluksen rakenne

- **Pääohjelma**: 
  CSV-tiedoston luku: Käyttäjältä pyydetään tiedoston polku, ja tiedot luetaan csv.DictReader-objektilla.
•  Datan puhdistus: clean_float-funktiolla varmistetaan, että kaikki numeeriset arvot ovat käsiteltävissä.
•  Toimialasuodatus: Käyttäjä valitsee toimialat, joita haluaa tarkastella.
•  Tunnuslukujen laskenta:
    ◦  Kannattavuus = (Revenue - Variable_costs - Fixed_costs) / Revenue
    ◦  Vakavaraisuus = Equity / (Equity + Liabilities)
•  Score-laskenta: Painotettu yhdistelmä kannattavuudesta ja vakavaraisuudesta.
•  Luokitus: rating_score-funktio antaa sanallisen arvion Score-arvon perusteella.
•  Tulostus: Yritykset esitetään taulukkomuodossa, joko tunnuslukujen tai Score-arvon mukaan paremmuusjärjestyksessä.
- **Funktiot**:
  - `clean_float(value)`: puhdistaa numeeriset arvot.
  - `luokittele_score(arvo)`: palauttaa värikoodatun luokituksen sijoitusarvon perusteella.
- **Tietolähteet ja -rakenteet**: 
•  CSV-tiedosto, jossa sarakkeet: `CompanyID`, `Industry`, `Revenue`, `Variable_costs`, `Fixed_costs`, `Equity`, `Liabilities`.
•  Listat: Tallentavat CSV-tiedoston sarakkeiden arvot (esim. revenue, equity, industry).
•  Sanakirjat: company_analysis sisältää jokaisen yrityksen tunnusluvut ja Score-arvon.
•  Sanakirja industry_codes: Mahdollistaa toimialojen valinnan lyhenteillä (S, M, E, K).
##Funktiot ja luokat

| Funktio | Kuvaus | Parametrit | Paluuarvo |
|--------|--------|------------|-----------|
| `clean_float(value)` | Puhdistaa numeerisen arvon tekstistä | `value: str` | `float` |
| `raiting_score(value)` | Palauttaa luokituksen sijoitusarvolle | `arvo: float` | `str` (värikoodattu luokitus) |

##Tietovarastot

- **CSV-tiedosto**: sisältää yritysten taloustiedot.
- **Ei käytetty tietokantaa** tässä versiossa.

##Lähdekoodit

Koko lähdekoodi on selattavissa GitLabissa:  
[GitLab-projektin URL tähän]

##Ajan käyttö

| Vaihe | Aika (h) |
|------|----------|
| Suunnittelu | 3 |
| Toteutus | 13|
| Testaus | 3 |
| Dokumentointi | 3 |
| **Yhteensä** | **22 h** |

##Videoesittely

Videoesittely on julkaistu piilotettuna YouTubessa:  
ei viedoesittelyä


##Oma arviointi
**Vahvuudet**
•  Ohjelma toimii luotettavasti ja tuottaa analyysin yritysten taloudellisesta tilanteesta yleisellä tasolla.
•  Käytin mahdollisuuksien mukaan opintojaksolla opittuja tekniikoita, kuten tiedostonkäsittely, listat, sanakirjat, funktiot, ehtolauseet, silmukat.
•  Toteutetin toimialakohtainen suodatuksen ja painotetun Score-luokituksen, joka ei mielestäni ollut suoraan kurssimateriaalissa.
•  Käytettin ANSI-värikoodit luokitusten visuaaliseen erottamiseen ja käyttäjäystävällisempää luettavuuteen.
•  Dokumentaatiosta pyrin tekemään selkeä ja esittämään rakenteen, logiikan ja taulukot selkesäti.
•  Koodi oli mielestäni selkeää, eikä monimutkaista ja pyrin tekemään siitä helposti luettavaa.

**Heikkoudet**
•  Syötteen tarkistuksia voisi kehittää edelleen jatkossa kun osaaminen karttuu kuten tiedostopolun validointi ja  osa virheilmoituksista.
•  Score-laskenta perustuu yksinkertaistettuun malliin – jatkossa voisi lisätä myös maksuvalmiutta ja muita tunnuslukuja, kun osaaminen kartuu -> ohjelmasta
   tulisi r3ealistisempi ja siten käyttökelpoisempi

Arvio työn pistemäärästä 35-40 pistettä -> ainakin yritin tehdä mielenkiintoisen ja toimivan työn, jota voin kehittää itsenäisesti jatkossa realistisemmaksi, kun taidot karttuu :)






