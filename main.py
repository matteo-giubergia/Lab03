import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    flag = False
    while flag == False:
        if 1 <= int(txtIn) <= 4:
            flag = True
        else:
            txtIn = input()

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input() #si puo controllare che siano solo lettere
        sc.handleSentence(txtIn,"Italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"English")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(txtIn) == 4:
        break


