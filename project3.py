class kulliyat():

    def __init__(self):
        
        self.dosya_oku=open("Rıfat_Miser__Toplum_Kalkınması.txt","r",encoding='utf8').read()
        self.dosya_oku = self.dosya_oku.replace(u'İ',u'i')
        self.dosya_oku = self.dosya_oku.replace(u'I',u'ı')

    def kulliyat_yap(self):        

        self.dosya_oku = self.dosya_oku.lower().split()
        self.kulliyat = []

        for i in self.dosya_oku:
            i=''.join(filter(lambda karakter: karakter.isalpha(),i))

            if i not in self.kulliyat:

                if (len(i) > 1):
                    self.kulliyat.append(i)
        return self.kulliyat   

k = kulliyat()

class denetim():

    def __init__(self):

        self.veri = open("deneme.txt","r").read()
        self.veri = self.veri.lower().split()
        self.yaz = open('deneme_duzeltilmis.txt','w')

    def denetleme_duzeltme(self):

        self.sozluk = k.kulliyat_yap()
        self.duzeltilmis=[]

        for kelime in self.veri:
            
            if kelime not in self.sozluk:

                self.oneriler=[]
                for kelimeler in self.sozluk:

                    if(len(kelime)==len(kelimeler)):
                
                        if(len(set(kelime).union(kelimeler)-set(kelimeler).intersection(kelime))==0):
                            # yer değiştirmiş kelime

                            self.oneriler.append(kelimeler)

                        else:
                            self.tek=0

                            for h1 , h2 in zip(kelime,kelimeler):#tek harf hatası

                                if (h1 != h2):

                                    self.tek +=1

                            if self.tek == 1:
                                self.oneriler.append(kelimeler)
                if(len(self.oneriler)==0):
                    print("\n**Yeni kelime bulundu**  ==>*"+kelime+"*")
                    self.secim = input("\nOlduğu gibi bırakmak için: 1\nDeğiştirmek için: 2\n:")
                    if (self.secim == '1'):
                        self.sozluk.append(kelime)
                        print("\nDeğiştirmedi ve -->'"+kelime+"' **külliyata eklendi**\n")
                    elif(self.secim == '2'):
                        self.yeni=input("Lütfen düzeltin\n: ")
                        kelime = self.yeni
                        self.sozluk.append(kelime)
                        print("\nDeğiştirildi ve -->'"+kelime+"' **külliyata eklendi**\n")
                    else:
                        print("\nHatalı Giriş")
                        break
                else:
                            
                    print("\nHata Bulundu ==>"+" *"+kelime+"*")
                    print("\nÖnerilen\n" + str(self.oneriler))
                    self.secim = input("\nOlduğu gibi bırakmak için: 1\nÖneriler için: 2\nDeğiştirmek için: 3\n:")

                    if (self.secim == '1'):

                        self.sozluk.append(kelime)
                        print("\nDeğiştirmedi ve -->'"+kelime+"' **külliyata eklendi**\n")

                    elif(self.secim == '2'):

                        self.sayi=1
                        print("\nÖnerilenden\n")
                        for m in self.oneriler:

                            print(m + "  İçin: "+str(self.sayi))
                            self.sayi +=1

                        self.deger=int(input(":"))
                        kelime = self.oneriler[self.deger-1]
                        print(kelime+ " diye düzeltildi\n")
                    
                    elif(self.secim == '3'):

                        self.yeni=input("\nLütfen düzeltin\n: ")
                        kelime = self.yeni
                        self.sozluk.append(kelime)
                        print("\nDeğiştirildi ve -->'"+kelime+"' **külliyata eklendi**\n")

                    else:
                        print("\nHatalı Giriş")
                        break

            self.duzeltilmis.append(kelime)

        self.yaz.write(" ".join(self.duzeltilmis))
        self.yaz.close()

d = denetim()
d.denetleme_duzeltme()
