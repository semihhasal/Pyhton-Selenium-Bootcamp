


print("*****************************")
print("OGRENCI SISTEMI")
print("*****************************")



ogrenciler= []


def ogrenci_ekle(isim,soyisim):
   yeni_ogrenci = {"İsim": isim ,"soyisim": soyisim}
   ogrenciler.append(yeni_ogrenci)


def ogrenci_cıkar(isim,soyisim):

    for ogrenci in ogrenciler:
     if ogrenci["İsim"] == isim and ogrenci["soyisim"] == soyisim:
        ogrenciler.remove(ogrenci)


def birden_cok_ogrenci_ekle(mutliple_students):
    tempList=[]
    for i in range(len(mutliple_students)):
     yeni_ogrenci = {"İsim": mutliple_students[i][0], "soyisim": mutliple_students[i][1]}
     tempList.append(yeni_ogrenci)

    ogrenciler.extend(tempList)



def ogrencileri_listele():

    for i in range(len(ogrenciler)):

     ogrenciler[i]["ogrenci_numara"] = i

    for i in ogrenciler:
        print(f"{i['ogrenci_numara']}: {i['İsim']} {i['soyisim']}")






def birden_cok_ogrenci_sil(multiple_students):

    j=-1

    while (j < len(ogrenciler)+j):
        ogrenci = ogrenciler[j]
        if ogrenci["İsim"] == multiple_students[j][0] and ogrenci["soyisim"] == multiple_students[j][1]:
            ogrenciler.remove(ogrenci)
            j += 1




ogrenci_ekle("Semih","Hasal")
#ogrencileri_listele()
multiple_students =(["Ali","Koşar"],["Yasin", "Sefa"])

birden_cok_ogrenci_ekle(multiple_students)
ogrencileri_listele()
ogrenci_cıkar("Semih","Hasal")
print("******")
ogrencileri_listele()
print("*************")
birden_cok_ogrenci_sil(multiple_students)
ogrenci_ekle("Semih","Hasal")
ogrencileri_listele()






