## creating corpus
class kulliyat():

    def __init__(self):
        
        self.dosya_oku=open("Rıfat_Miser__Toplum_Kalkınması.txt","r",encoding='utf8').read()
        
        ## Required for Turkish character change
        self.dosya_oku = self.dosya_oku.replace(u'İ',u'i')
        self.dosya_oku = self.dosya_oku.replace(u'I',u'ı')

    def kulliyat_yap(self):        

        self.dosya_oku = self.dosya_oku.lower().split()
        self.kulliyat = []

        for i in self.dosya_oku:
            i=''.join(filter(lambda karakter: karakter.isalpha(),i))

            if i not in self.kulliyat:
                
                if (len(i) > 2):
                    self.kulliyat.append(i)
        return self.kulliyat   

## checker
class denetim():
    
    def __init__(self):
        ## reading the testing file
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
                        
                        ## The characters of the transposed
                        if(len(set(kelime).union(kelimeler)-set(kelimeler).intersection(kelime))==0):
                            ## add to suggestions
                            self.oneriler.append(kelimeler)
                        else:
                            
                            self.tek=0
                            ## single character error
                            for h1 , h2 in zip(kelime,kelimeler):

                                if (h1 != h2):

                                    self.tek +=1

                            if self.tek == 1:
                                ## add to suggestions
                                self.oneriler.append(kelimeler)
                
                ## if word is not in corpus             
                if(len(self.oneriler)==0):
                    
                    print("\n**Yeni kelime bulundu**  ==>*"+kelime+"*")
                    self.secim = input("\nOlduğu gibi bırakmak için: 1\nDeğiştirmek için: 2\n:")
                    
                    ## options for adding new word
                    ## do not change
                    if (self.secim == '1'):
                        self.sozluk.append(kelime)
                        print("\nDeğiştirmedi ve -->'"+kelime+"' **külliyata eklendi**\n")
                    ## correct the word
                    elif(self.secim == '2'):
                        self.yeni=input("Lütfen düzeltin\n: ")
                        kelime = self.yeni
                        self.sozluk.append(kelime)
                        print("\nDeğiştirildi ve -->'"+kelime+"' **külliyata eklendi**\n")
                    else:
                        print("\nHatalı Giriş")
                        break
                ## suspicion of an incorrect word entered
                else:
                            
                    print("\nHata Bulundu ==>"+" *"+kelime+"*")
                    print("\nÖnerilen\n" + str(self.oneriler))
                    
                    self.secim = input("\nOlduğu gibi bırakmak için: 1\nÖneriler için: 2\nDeğiştirmek için: 3\n:")
                    
                    ## options for suspiction word
                    ## to add as is
                    if (self.secim == '1'):

                        self.sozluk.append(kelime)
                        print("\nDeğiştirmedi ve -->'"+kelime+"' **külliyata eklendi**\n")
                     
                    ## choose from suggestions
                    elif(self.secim == '2'):

                        self.sayi=1
                        print("\nÖnerilenden\n")
                        for m in self.oneriler:

                            print(m + "  İçin: "+str(self.sayi))
                            self.sayi +=1

                        self.deger=int(input(":"))
                        kelime = self.oneriler[self.deger-1]
                        print(kelime+ " diye düzeltildi\n")
                    
                    ## correct entered word
                    elif(self.secim == '3'):

                        self.yeni=input("\nLütfen düzeltin\n: ")
                        kelime = self.yeni
                        self.sozluk.append(kelime)
                        print("\nDeğiştirildi ve -->'"+kelime+"' **külliyata eklendi**\n")
                    
                    ## incorrect entry
                    else:
                        print("\nHatalı Giriş")
                        break

            self.duzeltilmis.append(kelime)

        self.yaz.write(" ".join(self.duzeltilmis))
        self.yaz.close()


def main():
    k = kulliyat()
    d = denetim()
    d.denetleme_duzeltme()
    
    
if __name__ == '__main__':
    main()

