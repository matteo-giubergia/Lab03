class Dictionary:
    def __init__(self, dict ):
        self._dict = dict

    def loadDictionary(self,path):
        paroleDizionario = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    paroleDizionario.append(line)
        except FileNotFoundError:
            print("file non trovato")
        return paroleDizionario

    def printAll(self):
        pass


    @property # per accedere al metodo come fosse un attributo della classe; dovuto al fatto che l'ho dichiarato privato
    def dict(self):
        return self._dict