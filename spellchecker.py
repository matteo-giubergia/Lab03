
import multiDictionary as md


class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        # altro modo senza cambiare la lettera iniziale della lingua nel main:
        # language = f"{language.0].upper()}{1:len(language)}"
        lingua = f"./resources/{language}.txt"
        testoDaControllare = replaceChars(txtIn)
        testoDaControllare = testoDaControllare.lower() #input minuscolo
        parole = [p for p in testoDaControllare.strip().split(" ")]
        multidizionario = md.MultiDictionary(lingua)
        print("***ricerca usando contains***")
        risultato = multidizionario.searchWord(parole)
        for e in risultato[0]:
            print(e)
        print(f"contains ha impiegato {risultato[1]} secondi")
        print("\n ***RICERCA LINEARE***")
        risultato2 = multidizionario.searchWordLinear(parole)
        for el in risultato2[0]:
            print(el)
        print(f"la ricerca lineare ha impiegato {risultato2[1]} secondi")
        print("\n ***RICERCA DICOTOMICA***")
        risultato3 = multidizionario.searchWordDichotomic(parole)
        for elem in risultato3[0]:
            print(elem)
        print(f"la ricerca dicotomica ha impiegato {risultato3[1]} secondi")





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