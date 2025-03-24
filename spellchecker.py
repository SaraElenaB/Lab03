import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multi= md.MultiDictionary()

# --------------------------------------------------------------------------------------------------------------------------
    def handleSentence(self, txtIn, language):

        start_time = time.time()           # inizia a misurare il tempo
        parole = txtIn.split(" ")
        text_corretto = [replaceChars(word) for word in parole ] #replace si aspetta una stringa, non una lista di stringhe

        listaRichWord = self._multi.searchWord(text_corretto, language)
        listaErrori = [word for word in listaRichWord if word.corretta is False]
        #stampa risultati
        if len(listaErrori) > 0:
            for error in listaErrori:
                print(error)
        end_time = time.time()
        durata = end_time-start_time
        print(f"Time elapsed {durata} seconds")

        return listaErrori, len(listaErrori), durata

#--------------------------------------------------------------------------------------------------------------------------
    def handleSentenceLinear(self, txtIn, language):

        start_time = time.time()
        parole = txtIn.split(" ")
        text_corretto = [replaceChars(word) for word in parole ]

        listaRichWordLinear = self._multi.searchWordLinear(text_corretto, language)
        listaErrori = [ word for word in listaRichWordLinear if word.corretta is False]
        if len(listaErrori) > 0:
            for error in listaErrori:
                print(error)
        end_time = time.time()
        durata = end_time-start_time
        print(f"Time elapsed {durata} seconds")

#--------------------------------------------------------------------------------------------------------------------------
    def handleSentenceDichotomic(self, txtIn, language):

        start_time = time.time()
        parole = txtIn.split(" ")
        text_corretto = [replaceChars(word) for word in parole]

        listaRichWordDichotomic = self._multi.searchWordDichotomic(text_corretto, language)
        listaErrori = [word for word in listaRichWordDichotomic if word.corretta is False]
        if len(listaErrori) > 0:
            for error in listaErrori:
                print(error)
        end_time = time.time()
        durata = end_time-start_time
        print(f"Time elapsed {durata} seconds")

#--------------------------------------------------------------------------------------------------------------------------

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")
#--------------------------------------------------------------------------------------------------------------------------
    def creaDizionario(self, path, language):
        self._multi.addDizionario(path, language)

    ###
#--------------------------------------------------------------------------------------------------------------------------
def replaceChars(text):
    chars = "\\'*_{}[]()<>#+-.!?£$%/&^,;="
    for c in chars:
        text = text.replace(c, "")
    return text