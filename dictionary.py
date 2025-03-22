class Dictionary:

    def __init__(self):
        self.dict = []

    def loadDictionary(self,path): #path=file generico lingua
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                self.dict.append(line.strip()) #necessario per rimuovere \n
        return self.dict


    def printAll(self):
        for word in self.dict:
            print(word)

    @property
    def dict(self):  #getter
        return self._dict

    @dict.setter
    def dict(self, value): #setter
        self._dict = value