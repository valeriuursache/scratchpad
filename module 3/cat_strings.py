if __name__ == "__main__":

    #Concatenation

    #You can concatenate two strings together using +
    leia = "I love you."
    han = "I know."

    print(leia + ' ' + han)

    ship = "Millinium Falcon"
    # Python starts at 0, slices TO the end index (not included)
    print("'" + ship[10:] + "'")

    bold_statement = ship + "is the fastest in the galaxy"
    print (bold_statement)
    print(ship)
    ship = 'S' + ship[1:]
    print(ship)


    jedi_masters = "Obi-Wan Kenobi, Qui-Gon Gin"
    print('Anakin' in jedi_masters)

    council_mermbers = ("Anakin, Obi-Wan Kenobi, Yoda, Qui-Gon Gin")
    print('Anakin' in council_mermbers)
    