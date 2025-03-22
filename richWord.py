class RichWord:
    def __init__(self, parola):
        self._parola = parola #str: parola da controllare
        self._corretta = None #bool: True se corretta

    @property #interfaccia + pulita di corretta
    def corretta(self):
        #x=r.corretta --> usa il getter
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        #r.corretta = True --> usa il setter
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        #stampa str dell'oggetto rw
        return self._parola
