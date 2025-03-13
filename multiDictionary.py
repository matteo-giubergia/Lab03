import dictionary as d
import richWord as rw

dictionary = d.Dictionary()
rword = rw.RichWord
class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        # controllo correttezza parole da richWord
        for parola in words: # dove words prende le parole da spellchecker
            rword(parola)
        paroleDizionario = dictionary.loadDictionary(language)
        pass


