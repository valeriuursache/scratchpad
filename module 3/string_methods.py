if __name__ == "__main__":  

    jar_jar = "Jar Jar Binks" 
    print(jar_jar)  
    print(jar_jar.lower())
    print(jar_jar.upper())

    test_string = "this is a really long string, Probably from a really long File and representa line"
    print('really' in test_string.lower())


    Vaders_Cry = "              NOOOOOOOOO       NOOOOO  OOOO!!!"
    print("'" + Vaders_Cry +"'")
    print(Vaders_Cry.lstrip())


    who_talks = "Who talkd first? You talk first? I talk first."
    talk_location = who_talks.find ('talk')
    print(talk_location)
    print(who_talks[talk_location + len('talk'):])

    sith_lords = 'Sidius, Duku'
    sith_lords = sith_lords.replace('Duku', 'Vader')
    print(sith_lords)

    troubled_anakin = "Not just the man, but the women and children too!"
    print(troubled_anakin.replace('women', '').replace('men', '').replace('children', ''))

    