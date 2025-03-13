import time

import multiDictionary as md
multidizionario = md.MultiDictionary()

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language): # e deve anche calcolare il tempo !!
        # a cosa mi serve che abbia in input il linguaggio
        testoDaControllare = replaceChars(txtIn).lower()
        parole = [p for p in testoDaControllare.strip().split()]
        multidizionario.printDic(language)
        multidizionario.searchWord(parole, language)
        # if language == "italian":
        #     pass # richiedo di usare il dizionario italiano e cosi via
        # if language == "english":
        #     pass
        # if language == "spanish":
        #     pass
        return parole, language

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


def replaceChars(text):
    chars = "\\`*_{}[]()>+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text