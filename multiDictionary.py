import dictionary as d
import richWord as rw
import time

#rword = rw.RichWord
#DEVO USARE QUALCHE METODO DI DICTIONARY
class MultiDictionary:

    def __init__(self, language):
        self.language = language
        #self.parole = parole
        self.dictionary = d.Dictionary(language)


    def printDic(self):
        paroleDizionario = self.dictionary.loadDictionary(self.language)
        print(paroleDizionario) # non fa la stessa cosa di printAll() in dictionary?
                                # perche ne devo mettere due?

    def searchWord(self, words):
        # controllo correttezza parole da richWord
        paroleGiuste = []
        paroleSbagliate = []
        listaRW = []
        t1 = time.time()
        for parola in words: # dove words prende le parole da spellchecker
            if self.dictionary.loadDictionary(self.language).__contains__(parola):
                rword = rw.RichWord(parola)
                rword.corretta = True
                # print(rword.__str__())
                # print(f"{rword.corretta}\n") # è una prorprita! non devo mettere le parentesi per richiamrla
                paroleGiuste.append(parola)
                listaRW.append(rword)
            else:
                rword = rw.RichWord(parola)
                rword.corretta = False
                listaRW.append(rword)
                paroleSbagliate.append(parola)
        t2 = time.time()
        tempoImpiegato = t2-t1
        # for p in paroleSbagliate:
        #     print(f"{p}")
        # print(f"contains ha impiegato {t2-t1} secondi")
        return paroleSbagliate, tempoImpiegato
    def searchWordLinear(self, words):

        paroleGiuste2 = []
        paroleSbagliate2 = []
        tic2 = time.time()
        # flag = False
        # for input in words:
        #     for pa in self.dictionary.loadDictionary(self.language):
        #         if input == pa:
        #             flag = True
        #     if flag == True:
        #         rword1 = rw.RichWord(input)
        #         rword1.corretta = True
        #         paroleGiuste2.append(input)
        #     else:
        #         rword1 = rw.RichWord(input)
        #         rword1.corretta = False
        #         paroleSbagliate2.append(input)
        #     flag = False
        # COSI E' PIU VELOCE:
        for input in words:
            if input in self.dictionary.loadDictionary(self.language):
                rword1 = rw.RichWord(input)
                rword1.corretta = True
                paroleGiuste2.append(input)
            else:
                rword1 = rw.RichWord(input)
                rword1.corretta = False
                paroleSbagliate2.append(input)

        toc3 = time.time()
        tempo = toc3-tic2
        return paroleSbagliate2, tempo

    def searchWordDichotomic(self, words):
        dizionario = self.dictionary.loadDictionary(self.language)
        meta = len(dizionario)//2
        paroleGiuste3 = []
        paroleSbagliate3 = []
        tic4 = time.time()
        flag = False
        for p in words:
            if p == dizionario[meta]:
                print("Ciao")
                rword1 = rw.RichWord(p)
                rword1.corretta = True
                paroleGiuste3.append(p)
                flag = True

            elif dizionario[meta]>p:
                diz1 = [dizionario[i] for i in range(meta)]
                if  p in diz1:
                    print("Ciao1")
                    rword1 = rw.RichWord(p)
                    rword1.corretta = True
                    paroleGiuste3.append(p)
                    flag = True

            elif dizionario[meta]<p:
                diz2 = [dizionario[i] for i in range(meta, len(dizionario))]
                if p in diz2:
                    print("Ciao2")
                    rword1 = rw.RichWord(p)
                    rword1.corretta = True
                    paroleGiuste3.append(p)
                    flag = True

            if flag==False:
                rword1 = rw.RichWord(p)
                rword1.corretta = False
                paroleSbagliate3.append(p)

        toc5 = time.time()
        tempo3 = toc5-tic4
        return paroleSbagliate3, tempo3






