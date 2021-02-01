#haetaan json
import json
 
#tehdään luokka pelaaja, mallintaa pelaajaa, jolla on attribuutit nimi, kansallisuus,
#syötöt, maalit, rankut, joukkue, pelit ja pisteet
class Pelaaja:
    def __init__(self, nimi, kansallisuus, syotot, maalit, rankut, joukkue, pelit):
        self.nimi = nimi
        self.kansallisuus = kansallisuus
        self.syotot = syotot
        self.maalit = maalit
        self.rankut = rankut
        self.joukkue = joukkue
        self.pelit = pelit
        self.pisteet = maalit + syotot
        
    #palautetaan tiedot
    def __str__(self):
        return f"{self.nimi:21}{self.joukkue:1}  {self.maalit:2} + {self.syotot:2} = {self.pisteet:>3}"

#tehdään luokka joukkue,jolla on attribuutit lyhenne ja pelaajat
class Joukkue:
    def __init__(self, lyhenne):
        self.lyhenne = lyhenne
        self.__pelaajat = []
    
    #lisätään joukkueeseen pelaaja
    def lisaa_pelaaja(self, Pelaaja):
        self.__pelaajat.append(Pelaaja)
        
    #haetaan joukkueesta tietty pelaaja nimellä
    def hae_pelaaja(self, nimi):
        lista = []
        #palautetaan pelaaja, jos löytyy joukkueesta
        for pelaaja in self.__pelaajat:
            lista.append(pelaaja.nimi)
            if pelaaja.nimi == nimi:
                return pelaaja
        #palauttaa None, jos pelaajaa ei löydy
        if nimi not in lista:
            return None
        
    #antaa sulejtun attrubuutin, joukkueen tiedot
    def anna_joukkue(self):
        return self.__pelaajat

        
#luodaan luokka JoukkueRekisteri, jolla on attributtii rekisteri
class JoukkueRekisteri:
    def __init__(self):
        self.__rekisteri = []
    
    #lisätään joukkueeseen pelaaja
    def lisaa_joukkue(self, Joukkue):
        self.__rekisteri.append(Joukkue)
    
    #haetaan pelaaja joukkueesta nimen perusteella
    def hae_pelaaja(self, nimi):
        for joukkue in self.__rekisteri:
            #jos pelaajaa ei löydy, ei palauteta mitään
            if joukkue.hae_pelaaja(nimi) == None:
                continue
            #palautetaan pelaaja, jos löytyy listasta
            else:
                return joukkue.hae_pelaaja(nimi)
            
    #haetaan tietty joukkue sen lyhenteen perusteella
    def hae_joukkue(self, lyhenne):
        for alkio in self.__rekisteri:
            #kun rekisteristä löytyvä joukkue vastaa annettua lyhennettä, palautetaan se joukkue
            if lyhenne == alkio.lyhenne:
                return alkio
            
    #haetaan joukkueen tiedot käyttöön sen lyhenteen perusteella
    def anna_joukkue(self, lyhenne):
        for joukkue in self.__rekisteri:
            if joukkue.lyhenne == lyhenne:
                return joukkue.anna_joukkue()

    


#tehdään luokka RekisteriSovellus, jolla on attribuutti rekisteri
class RekisteriSovellus:
    def __init__(self):
        self.__rekisteri = JoukkueRekisteri()
    
    #lisätään rekisteriin joukkue
    def lisaa_joukkue(self, joukkue):
        self.__rekisteri.lisaa_joukkue(joukkue)
    
    #haetaan pelaaja rekisteristä nimen avulla
    def hae_pelaaja(self, nimi):
        return self.__rekisteri.hae_pelaaja(nimi)
    
    #haetaan joukkue rekisteristä sen lyhenteen avulla
    def hae_joukkue(self, lyhenne):
        return self.__rekisteri.hae_joukkue(lyhenne)
    
    #otetaan joukkueen tiedot käyttöön sen lyhenteen avulla
    def anna_joukkue(self, lyhenne):
        return self.__rekisteri.anna_joukkue(lyhenne)
    
    #tällä käynnistetään sovelluksen toiminta
    def suorita(self):
        #alustetaan avuksi tyhjät listat sekä sanakirja
        lista = []
        joukkueet = []
        maat = []
        maa_pelaajat = {}
        tieto = input("tiedosto: ")
        
        #otetaan tiedostosta tarvittavat tiedot
        with open(tieto) as tiedosto:
            data = tiedosto.read()
            tiedot = json.loads(data)
        #käydään jokainen tiedoston alkio läpi ja tehdään niistä Pelaaja-oliot
        for alkio in tiedot:
            pelaaja = Pelaaja(alkio["name"], alkio["nationality"], alkio["assists"], alkio["goals"], alkio["penalties"], alkio["team"], alkio["games"])
            lista.append(pelaaja)
        
       
        for pelaaja in lista:
            #tehdään lista, joka sisältää kaikki mukana olevat joukkueet
            if pelaaja.joukkue not in joukkueet:
                joukkueet.append(pelaaja.joukkue)
            #tehdään lista, joka sisältää kaikki maat, joista pelaajia on
            if pelaaja.kansallisuus not in maat:
                maat.append(pelaaja.kansallisuus)
                
        #luodaan jokaisesta mukana olevasta joukkueesta Joukkue-olio
        for alkio in joukkueet:
            joukkue = Joukkue(alkio)
            self.__rekisteri.lisaa_joukkue(joukkue)
            #lisätään pelaajat oikeisiin joukkueisiin
            for pelaaja in lista:
                if pelaaja.joukkue == alkio:
                    joukkue.lisaa_pelaaja(pelaaja)
        
        #luodaan jokaisen maan kohdalle sanakirjaan lista, johon voi lisätä kyseisestä maasta tulevat pelaajat
        for maa in maat:
            maa_pelaajat[maa] = []
        
        #lisätään pelaajat oikeaan maahan
        for pelaaja in lista:
            for alkio in maat:
                if pelaaja.kansallisuus == alkio:
                    maa_pelaajat[alkio].append(pelaaja)
        
        #apumetodi
        def jarjesta(alkio):
            return alkio
        
        #palauttaa tehdyt pisteet
        def pisteiden_mukaan(olio):
            return olio.pisteet
        
        #järjestää ensisijaisesti pisteiden, sitten maalien mukaan
        def pisteet_ja_maalit(olio):
            return (olio.pisteet, olio.maalit)
        
        #palauttaa maalien määrän
        def eniten_maaleja(olio):
            return olio.maalit
        
        #palauttaa pelien määrän
        def vahiten_peleja(olio):
            return olio.pelit
        
        #tulostetaan käyttäjälle tiedoksi toiminnot ja niiden komennot
        print(f"luettiin {len(lista)} pelaajan tiedot")

        print("komennot: ")
        print("0 lopeta")
        print("1 hae pelaaja")
        print("2 joukkueet")
        print("3 maat")
        print("4 joukkueen pelaajat")
        print("5 maan pelaajat")
        print("6 eniten pisteitä")
        print("7 eniten maaleja")
        
        #käyttäjä antaa komentoja, ja tämä silmukka suorittaa niin kauan niitä, kuin annetaan lopetuskäsky
        while True:
            komento = int(input("komento: "))
            #suoritus loppuu
            if komento == 0:
                break
            #tulostaa pelaajan tiedot annetun nimen perusteella
            elif komento == 1:
                nimi = input("nimi: ")
                print(self.hae_pelaaja(nimi))
            #tulostaa joukkueet aakkosjärjestyksessä
            elif komento == 2:
                j = sorted(joukkueet, key=jarjesta)
                for alkio in j:
                    print(alkio)
                    
            #tulostaa maat aakkosjärjestyksessä
            elif komento == 3:
                m = sorted(maat, key=jarjesta)
                for alkio in m:
                    print(alkio)
                    
            #tulostaaa annetun joukkueen pelaajat käänteisesti pisteiden mukaan järjestettynä
            elif komento == 4:
                j = input("joukkue: ")
                joukkue = self.anna_joukkue(j)
                for alkio in sorted(joukkue, key=pisteiden_mukaan, reverse=True):
                    print(alkio)
            
            #tulostaa annetun maan pelaajat käänteisesti pisteiden mukaan järjestettynä
            elif komento == 5:
                maa = input("maa: ")
                for alkio in sorted(maa_pelaajat[maa], key=pisteiden_mukaan, reverse = True):
                    print(alkio)
            
            #tulostaa annetun luvun verran parhaita pelaajia pisteiden ja maalien mukaan käänteisesti järjestettynä
            elif komento == 6:
                luku = int(input("kuinka monta: "))
                parhaat = sorted(lista, key = pisteet_ja_maalit, reverse=True)
                osa = parhaat[:luku]
                for alkio in osa:
                    print(alkio)
            
            #tulostaa annetun määrän verran pelaajia ensi käänteisesti maalien määrän ja toissijaisesti pelien määrän perusteella
            elif komento == 7:
                luku = int(input("kuinka monta: "))
                parhaat = sorted(lista, key=eniten_maaleja, reverse = True)
                uusi = sorted(parhaat, key=vahiten_peleja)
                uusi2 = sorted(uusi, key=eniten_maaleja, reverse=True)
            
                osa = uusi2[:luku]
                for o in osa:
                    print(o)


#aloittaa sovelluksen suorittamisen
aja = RekisteriSovellus()
aja.suorita()
