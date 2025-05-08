def asal():
 sayi = int(input("bir sayi giriniz:"))
 if sayi < 2:
    return print( "sayi asal degil")
 else:
    if sayi == 2:
      return print( "sayi asal")
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                print("sayi asal degil")
                return
        print( "sayi asal")
            

    


