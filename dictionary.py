#legge il file e raccoglie le informazioni in una lista locale
# dando anche modo alle altre classi di consultare il dizionario
class Dictionary:
    def __init__(self, dict ):
        self._dict = dict

    def loadDictionary(self,path):
        paroleDizionario = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    paroleDizionario.append(line.strip())
        except FileNotFoundError:
            print("file non trovato")
        return paroleDizionario

    def printAll(self):
        for parola in self._dict:
            print(parola)


    @property # per accedere al metodo come fosse un attributo della classe; dovuto al fatto che l'ho dichiarato privato
    def dict(self):
        return self._dict