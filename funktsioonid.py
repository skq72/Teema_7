import smtplib,ssl
from email.message import EmailMessage

def loefailist(fail:str):
    telefoniraamat=[]
    with open(fail,'r',encoding="utf-8-sig") as f:
        for rida in f:
            nimi,email,telefon=rida.strip().split(",")
            telefoniraamat.append({'nimi':nimi,'email':email,'telefon':telefon})
    return telefoniraamat

def Kirjutafailisse(fail:str,järjend:list):
    with open(fail,'w',encoding="utf-8-sig") as f:
        for k in järjend:
            f.write(f"{k['nimi']},{k['email']},{k['telefon']}\n")

def lisa_kontakt(telefoniraamat):
    """Добавление нового контакта в телефонную книгу
    """
    print("Lisame uue kontakti!") 
    uus_nimi = input("Sisesta nimi: ").strip().capitalize()
    uus_email = input("Sisesta e-mail: ").strip().lower()
    uus_telefon = input("Sisesta telefoninumber: ").strip()
    telefoniraamat.append({'nimi': uus_nimi, 'email': uus_email, 'telefon': uus_telefon}) 
    print("Uus kontakt on lisatud!")

def kuva_kontaktid(telefoniraamat):
    """Показывает все контакты в телефонной книге
    """
    if telefoniraamat:
        for k in telefoniraamat:
            print(k)

def otsi_kontakt(telefoniraamat):
    """Ищет слово во всех значениях словаря и возвращает его запись
    """
    nimi=input("Sisesta nimi: ").strip().lower()
    for kontakt in telefoniraamat:  
        if nimi in kontakt['nimi'].lower():  
            print(f"Leitud: {kontakt}") 
            return kontakt  
    return None  

def paranda_kontakt(telefoniraamat):
    """Исправление контакта
    """
    nimi=input("Sisesta nimi: ").strip().lower()
    for kontakt in telefoniraamat:  
        if nimi in kontakt['nimi'].lower():  
            print(f"Leitud: {kontakt}") 
            net['nimi']=input("Uus nimi: ")  
            kirje['email']=input("Uus email: ")  
            kirje['telefon']=input("Uus telefon: ")  
        print("Parandatud!")       
    return None  




def kustuta_kontakt(telefoniraamat):
    """ Удалить контакт
    """
    nimi=input("Sisesta nimi: ").strip().lower()
    for kontakt in telefoniraamat:  
        if nimi in kontakt['nimi'].lower():  
            print(f"Leitud: {kontakt}") 
            return kontakt  
    return None   
    if kirje:
        telefoniraamat.remove(kirje)
        print("Kontakt kustutatud!")


def sorteeri_kontakt(telefoniraamat):
    print("Sorteerimise valikud: nimi / email / telefon")
    by=input("Sisesta valik: ").lower()
    if by in ["nimi", "telefon", "email"]:
        n=len(telefoniraamat)
        for i in range(n):
            for j in range(i+1,n):
                if telefoniraamat[i][by].lower()>telefoniraamat[j][by].lower():
                    telefoniraamat[i],telefoniraamat[j]=telefoniraamat[j],telefoniraamat[i]
        print("Kontaktid on sorditud.")
    else:
        print("Tundmatu sorterimisviis.")

def saada_kiri():
    kellele=input("Kellele: ")
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="kirillgorshkov264@gmail.com"
    parool=input("Rakenduste parool") #gjfk fbvi nfjk hoyu
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg['Subject']="LOGITpv24"
    msg['From']=kellelt
    msg['To']=kellele
    msg.set_content("ZDAROVA")
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print('Kiri saadetud')
    except Exception as e:
        print("Viga: ", e)
