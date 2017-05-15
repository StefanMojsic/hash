import hashlib
sadrzaj = ""
while(True):
    print("------------------------------------------------")
    print("1)Unesite poruku koju želite da hešujete: ")
    print("------------------------------------------------")
    print("2)Izracunajte HASH Algoritme : MD5,SHA-1,SHA-256")
    print("------------------------------------------------")
    print("3)Izađite iz programa...")
    print("------------------------------------------------")

    unos = int(input("Izbor : "))
    nazivFajla = "test.txt"
    if(unos == 1):
        
        fajl = open(nazivFajla,"w")

        while(True):
            tekst = input("Upisite neki tekst u fajl.Da napustite stisnite 2 puta ENTER . ")
            if(tekst == ""):
                fajl.close()
                break
            
            else:
                fajl.write(tekst)
                
            
           

        ucitanF = open(nazivFajla,"rb")

        sadrzaj = ucitanF.read()
        ucitanF.close()
        

    if(unos == 2):
        if(sadrzaj == ""):
            print("Nema sadržaja za heširanje.. ")
            fajl_1 = open(nazivFajla,"w")
            ponovoUnesi = input("Morate uneti neku poruku: ")
            if (ponovoUnesi == None):
                fajl_1.close()
                break
            else:
                fajl_1.write(ponovoUnesi)
                
        ucitanF = open(nazivFajla,"rb")
        sadrzaj = ucitanF.read()
        ucitanF.close()

        print("____Sadrzaj____Fajla_____")
        print("\n")
        print(sadrzaj)
        
        md5Hash = hashlib.md5(sadrzaj).hexdigest()
        sha1Hash = hashlib.sha1(sadrzaj).hexdigest()
        sha256Hash = hashlib.sha256(sadrzaj).hexdigest()
        print("\n")
        print("MD5 je :  ",md5Hash)
        print("\n")
        print("SHA-1 je :  ",sha1Hash)
        print("\n")
        print("SHA-256 je :  ",sha256Hash)
        print("\n")

        
    if(unos == 3):
        break
           
    
    
