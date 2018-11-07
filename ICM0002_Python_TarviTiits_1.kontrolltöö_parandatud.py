#Kontrolltöö I
# VARIANT 1
# Tarvi Tiits, 182015TAF (distantsõppur, avatud ülikool) (NB! parandatud versioon)
# Ülesanne 1:

def list_sum(list):
    #funktsioon, mis võtab argumendiks listi ja tagastab elementide summa
    list_sum = 0
    for i in range (0,len(list)):
        list_sum = list_sum + float(list[i])
    return list_sum


# Ülesanne 2:
def liblikas(string):
    #funktsioon, mis võtab argumendiks lause ja kui sõna algab a tähega, asendab selle sõnega "liblikas"
    sõnad = list(string.split())
    i = 0
    uus_string = ""
    while i < len(sõnad):
        if sõnad[i].startswith("a") or sõnad[i].startswith("A"):
            viimanesõna = sõnad[i]
        i= i + 1
    i = 0
    while i < len(sõnad):
        if sõnad[i] == viimanesõna:
            viimanesõna = "liblikas"
            uus_string = uus_string + " " + viimanesõna 
        else:
            sõnad[i] = sõnad[i]
            uus_string = uus_string + " " + sõnad[i] 
        i = i +1
    print(uus_string)

#Ülesanne 3:
def common_symbols(string1, string2):
    # funktsioon, mis väljastab samade arvu, mitu korda on samad sümbolid samas asukohas ja mitu samasugust sümbolit on kummaski sõnes
    i = 0
    j = 0
    mitmel_korral_samas_kohas = 0
    mitu_samasugust_sümbolit = 0
    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            mitmel_korral_samas_kohas = mitmel_korral_samas_kohas + 1
        else:
            mitmel_korral_samas_kohas = mitmel_korral_samas_kohas
        i = i + 1
        j = j + 1
    i = 0
    uus_string1 = ""
    while i < len(string1):
        sorteeritud = sorted(string1)
        if sorteeritud[i] == sorteeritud[i-1]:
            uus_string1 = uus_string1
        else:
            uus_string1 = uus_string1 + sorteeritud[i]
        i = i + 1
    j = 0
    uus_string2 = ""
    while j < len(string2):
        sorteeritud = sorted(string2)
        if sorteeritud[j] == sorteeritud[j-1]:
            uus_string2 = uus_string2
        else:
            uus_string2 = uus_string2 + sorteeritud[j]
        j = j + 1
    i = 0
    j = 0
    while j < len(uus_string2):
        while i < len(uus_string1) and i < len(uus_string2) and j < len(uus_string1) and j < len(uus_string2):
            if uus_string1[j] == uus_string2[i]:
                mitu_samasugust_sümbolit = mitu_samasugust_sümbolit + 1  
            else:
                mitu_samasugust_sümbolit = mitu_samasugust_sümbolit
            i = i + 1
        i = 0
        j = j + 1
    print(str(mitmel_korral_samas_kohas) + "," + str(mitu_samasugust_sümbolit))
        