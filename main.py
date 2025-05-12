import tkinter as tk
from tkinter import messagebox
from funktsioonid import *




kontaktid = loe_failist()

def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt_gui():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        lisa_kontakt(kontaktid, nimi,telefon,email)
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Edu","kontakt lisatud.")
        nimi_entry.delete(0,'end')
        telefon_entry.delete(0,'end')
        email_entry.delete(0,'end')
        kuva_kontaktid()
    else:
        messagebox.showwarning("Tühjad väljad","Täida kõik väljad")

def otsi_kontakt_gui():
    nimi = nimi_entry.get()
    tulemused=otsi_kontakt(kontaktid, nimi)
    if tulemused:
        kontakt=tulemused[0]
        otsingu_viide.set(kontakt["nimi"])
        nimi_entry.delete(0,'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0,'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0,'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0",'end')
        tekstikast.insert("end", f"Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")


def kustuta_kontakt_gui():
    nimi=nimi_entry.get()
    if kustuta_kontakt(kontaktid, nimi):
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("kustutatud", f"'{nimi}' kustutati.")
        kuva_kontaktid()
    else:
        messagebox.showwarning("Ei leitud", "Kontakti ei leitud.")

def sorteeri_gui():
    kontaktid_sorted=sorteeri_kontaktid(kontaktid, "nimi")
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")


def muuda_kontakt_gui():
    vana_nimi=otsingu_viide.get()
    uus_nimi=nimi_entry.get()
    uus_telefon=telefon_entry.get()
    uus_email=email_entry.get()

    if vana_nimi and uus_nimi and uus_telefon and uus_email:
        õnnestus=muuda_kontakt(kontaktid,vana_nimi, uus_nimi, uus_telefon, uus_email)
        if õnnestus:
            salvesta_kontaktid(kontaktid)
            messagebox.showinfo("Muudetud", f"'{vana_nimi}' andmed on muudetud.")
            kuva_kontaktid()
        else:
            messagebox.showwarning("Tõrge", "Kontakti ei leitud muudatuseks")
    else:
        messagebox.showwarning("Puuduvad andmed","Palun täida kõik muudatuseks.")







aken = tk.Tk()
aken.title("Telefoniraamat")
aken.iconbitmap("book.ico")
aken.configure(bg="orange")
otsingu_viide=tk.StringVar() #IntVar() #Muudame StringVar-iks, et saaksime salvestada algse nime
otsingu_viide.set("")
tk.Label(aken, text="Nimi: ",font=("Calibri",10),fg="grey").pack()
nimi_entry=tk.Entry(aken)
nimi_entry.pack()
tk.Label(aken, text="E-mail: ",font=("Calibri",10),fg="black").pack()
email_entry=tk.Entry(aken)
email_entry.pack()
tk.Label(aken, text="Telefon: ",font=("Calibri",10),fg="green").pack()
telefon_entry=tk.Entry(aken)
telefon_entry.pack()

nupude_rida=tk.Frame(aken)
nupude_rida.pack(pady=10)



tk.Button(nupude_rida, text="Kuva kontaktid", command=kuva_kontaktid,font=("Goudy Stout",8),fg="pink").pack(side="right",pady=0)
tk.Button(nupude_rida, text="Lisa kontakt", command=lisa_kontakt_gui,font=("Goudy Stout",7),fg="blue").pack(side="left")
tk.Button(nupude_rida, text="Otsi kontakt", command=otsi_kontakt_gui,font=("Goudy Stout",4),fg="purple").pack(side="right")
tk.Button(nupude_rida, text="Muuda kontakt", command=muuda_kontakt_gui,font=("Goudy Stout",5),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Kustuta kontakt", command=kustuta_kontakt_gui,font=("Goudy Stout",10),fg="green").pack(side="left")
tk.Button(nupude_rida, text="Sorteeri_kontakt", command=sorteeri_gui,font=("Goudy Stout",6),fg="red").pack(side="left")

tekstikast = tk.Text(aken, height=10, width=40)
tekstikast.pack(pady=15)


aken.mainloop()