import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self._listaDizionari = {}
        #listaParole = d.Dictionary() --> crea oggetto dizionario

#--------------------------------------------------------------------------------------------------------------------------
    def printDic(self, language):

        #metodo 1:
        for element in self._listaDizionari[language]:
            print(element)

        #metodo 2:
        #se avessimo avuto nel costruttore una lista, allora avremmo dovuto tenere
        #conto che che loadDictionaty è un metodo definito nella classe Dictionary, devo usare
        #un oggetto dictionary (cioè una lista)

        # if language == 'Italian':
        #     self._listaParole.loadDictionary("Italian.txt")
        # elif language == 'English':
        #     self._listaParole.loadDictionary("English.txt")
        # elif language == 'Spanish':
        #     self._listaParole.loadDictionary("Spanish.txt")
        #
        # return self._listaParole.dict
        #restituisce la lista di parole caricate, utilizzando la property

#--------------------------------------------------------------------------------------------------------------------------
    def searchWord(self, words, language):

        listaRichWord=[]
        listaDizionario = self.getDizionario(language)

        for word in words:
            richword = rw.RichWord(word)
            if listaDizionario.__contains__(word.lower()):
                richword.corretta = True   #cosi funziona l'altra classe
            else:
                richword.corretta = False

            listaRichWord.append(richword)
        return listaRichWord

# --------------------------------------------------------------------------------------------------------------------------
    def addDizionario(self, path, language):
        dict = d.Dictionary()
        listaParole = dict.loadDictionary(path)
        self._listaDizionari[language] = listaParole

    def getDizionario(self, language):
        return self._listaDizionari[language] #self._listaDizionari.get(language)


# Esempio di utilizzo
#if __name__ == "__main__":
    #md = MultiDictionary()
    #parole_italiane = md.printDic('Italian')
    #print(parole_italiane)

#Controllo metodo searchWord()
# md = MultiDictionary()
# lista_parole = ["cane", "gatto", "tree"]
# risultati = md.searchWord(lista_parole, "Italian")
# for parola in risultati:
#     print(f"{parola} → Corretta: {parola.corretta}")








