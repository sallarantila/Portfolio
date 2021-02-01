# tee ratkaisusi tänne
import json
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
    
    def __str__(self):
        return f"{self.nimi:21}{self.joukkue:1}  {self.maalit:2} + {self.syotot:2} = {self.pisteet:>3}"


class Joukkue:
    def __init__(self, lyhenne):
        self.lyhenne = lyhenne
        self.__pelaajat = []
    def lisaa_pelaaja(self, Pelaaja):
        self.__pelaajat.append(Pelaaja)
    def hae_pelaaja(self, nimi):
        lista = []
        for pelaaja in self.__pelaajat:
            lista.append(pelaaja.nimi)
            if pelaaja.nimi == nimi:
                return pelaaja
        if nimi not in lista:
            return None
    def anna_joukkue(self):
        return self.__pelaajat

        
            


class JoukkueRekisteri:
    def __init__(self):
        self.__rekisteri = []

    def lisaa_joukkue(self, Joukkue):
        self.__rekisteri.append(Joukkue)
    def hae_pelaaja(self, nimi):
        for joukkue in self.__rekisteri:
            if joukkue.hae_pelaaja(nimi) == None:
                continue
            else:
                return joukkue.hae_pelaaja(nimi)
    def hae_joukkue(self, lyhenne):
        for alkio in self.__rekisteri:
            if lyhenne == alkio.lyhenne:
                return alkio
    
    def anna_joukkue(self, lyhenne):
        for joukkue in self.__rekisteri:
            if joukkue.lyhenne == lyhenne:
                return joukkue.anna_joukkue()

    



class RekisteriSovellus:
    def __init__(self):
        self.__rekisteri = JoukkueRekisteri()
    
    def lisaa_joukkue(self, joukkue):
        self.__rekisteri.lisaa_joukkue(joukkue)
    
    def hae_pelaaja(self, nimi):
        return self.__rekisteri.hae_pelaaja(nimi)
    def hae_joukkue(self, lyhenne):
        return self.__rekisteri.hae_joukkue(lyhenne)
    
    def anna_joukkue(self, lyhenne):
        return self.__rekisteri.anna_joukkue(lyhenne)
    
    def suorita(self):
        lista = []
        joukkueet = []
        maat = []
        maa_pelaajat = {}
        tieto = input("tiedosto: ")
        with open(tieto) as tiedosto:
            data = tiedosto.read()
            tiedot = json.loads(data)
        for alkio in tiedot:
            pelaaja = Pelaaja(alkio["name"], alkio["nationality"], alkio["assists"], alkio["goals"], alkio["penalties"], alkio["team"], alkio["games"])
            lista.append(pelaaja)
        
        for pelaaja in lista:
            if pelaaja.joukkue not in joukkueet:
                joukkueet.append(pelaaja.joukkue)
            if pelaaja.kansallisuus not in maat:
                maat.append(pelaaja.kansallisuus)

        for alkio in joukkueet:
            joukkue = Joukkue(alkio)
            self.__rekisteri.lisaa_joukkue(joukkue)
            for pelaaja in lista:
                if pelaaja.joukkue == alkio:
                    joukkue.lisaa_pelaaja(pelaaja)
        
        for maa in maat:
            maa_pelaajat[maa] = []
        
        
        for pelaaja in lista:
            for alkio in maat:
                if pelaaja.kansallisuus == alkio:
                    maa_pelaajat[alkio].append(pelaaja)

        def jarjesta(alkio):
            return alkio
        
        def pisteiden_mukaan(olio):
            return olio.pisteet
        
        def pisteet_ja_maalit(olio):
            return (olio.pisteet, olio.maalit)
        
        def eniten_maaleja(olio):
            return olio.maalit
        def vahiten_peleja(olio):
            return olio.pelit
        

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
        while True:
            komento = int(input("komento: "))
            if komento == 0:
                break
            elif komento == 1:
                nimi = input("nimi: ")
                print(self.hae_pelaaja(nimi))
            
            elif komento == 2:
                j = sorted(joukkueet, key=jarjesta)
                for alkio in j:
                    print(alkio)
            
            elif komento == 3:
                m = sorted(maat, key=jarjesta)
                for alkio in m:
                    print(alkio)
            
            elif komento == 4:
                j = input("joukkue: ")
                joukkue = self.anna_joukkue(j)
                for alkio in sorted(joukkue, key=pisteiden_mukaan, reverse=True):
                    print(alkio)
            
            elif komento == 5:
                maa = input("maa: ")
                for alkio in sorted(maa_pelaajat[maa], key=pisteiden_mukaan, reverse = True):
                    print(alkio)

            elif komento == 6:
                luku = int(input("kuinka monta: "))
                parhaat = sorted(lista, key = pisteet_ja_maalit, reverse=True)
                osa = parhaat[:luku]
                for alkio in osa:
                    print(alkio)
            
            elif komento == 7:
                luku = int(input("kuinka monta: "))
                parhaat = sorted(lista, key=eniten_maaleja, reverse = True)
                uusi = sorted(parhaat, key=vahiten_peleja)
                uusi2 = sorted(uusi, key=eniten_maaleja, reverse=True)
            
                osa = uusi2[:luku]
                for o in osa:
                    print(o)



aja = RekisteriSovellus()
aja.suorita()
