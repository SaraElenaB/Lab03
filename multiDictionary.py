import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self._listaDizionari = {}
        #listaParole = d.Dictionary() --> crea oggetto dizionario

#--------------------------------------------------------------------------------------------------------------------------
    def printDic(self, language):

        #metodo 1: --> struttura dati: dizionario
        for element in self._listaDizionari[language]:
            print(element)

        #metodo 2: --> struttura dati: lista
        #se avessimo avuto nel costruttore una lista, allora avremmo dovuto tenere conto che che loadDictionaty è un
        #metodo definito nella classe Dictionary, devo usare un oggetto dictionary (cioè una lista)

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

#--------------------------------------------------------------------------------------------------------------------------
    def searchWordLinear(self, words, language):

        listaRichWordLinear=[]
        #_listaDizionario = self.getDizionario(language)

        for word in words:
            richword = rw.RichWord(word)
            if word in self._listaDizionari[language]:
                richword.corretta = True
            else:
                richword.corretta = False
            listaRichWordLinear.append(richword)
        return listaRichWordLinear

#--------------------------------------------------------------------------------------------------------------------------
    def searchWordDichotomic(self, words, language):

        listaRichWordDichotomic=[]
        listaDizionario = self.getDizionario(language)

        if len(listaDizionario) % 2 ==0: #divisibile
            indice = int(len(listaDizionario) / 2)
        else:
            indice = int(len(listaDizionario+1) / 2)

        for word in words:
            richword = rw.RichWord(word)

            if word == listaDizionario[indice]:
                #corretta = True
                richword.corretta = True
                listaRichWordDichotomic.append(richword)
                break
            elif word < listaDizionario[indice]:
                for i in range(0, indice):
                    if word == listaDizionario[i]:
                        #corretta = True
                        richword.corretta = True
                        listaRichWordDichotomic.append(richword)
                        break
            elif word > listaDizionario[indice]:
                for j in range(indice, len(listaDizionario)):
                    if word == listaDizionario[j]:
                        #corretta = True
                        richword.corretta = True
                        listaRichWordDichotomic.append(richword)
                        break
            return listaRichWordDichotomic

#--------------------------------------------------------------------------------------------------------------------------
    def addDizionario(self, path, language):
        dict = d.Dictionary()
        listaParole = dict.loadDictionary(path)
        self._listaDizionari[language] = listaParole

#--------------------------------------------------------------------------------------------------------------------------
    def getDizionario(self, language):
        return self._listaDizionari[language] #self._listaDizionari.get(language)

#--------------------------------------------------------------------------------------------------------------------------

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








