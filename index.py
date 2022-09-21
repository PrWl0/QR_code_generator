from os import link
import qrcode
link=input("Podaj link który chcesz zamienic na kod QR: ")
if link[0:8]=="https://":
    img = qrcode.make(link)
    name=input("Podaj nazwę pliku: ")
    img.save(name+".png")
else:
    link="https://"+link    
    name=link[8:len(link)]
    img = qrcode.make(link)
    img.save(name+".png")
