import tkinter as tk
from tkinter import messagebox
from turtle import window_height
from funktsioonid import *

kontaktid = loe_failist()

def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def kuva_nimi_telefon():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']}\n")
def kuva_emailid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['email']}\n")

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

def sorteeriza_gui():
    kontaktid_sorted=sorteeri_za(kontaktid, "nimi")
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def sorteeri_num():
    kontaktid_sorted=sorteeri_kontaktid(kontaktid, "telefon")
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def sorteeri_email():
    kontaktid_sorted=sorteeri_kontaktid(kontaktid, "email")
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
aken.title("kontaktandmed")
aken.iconbitmap("book.ico")
aken.configure(bg="orange")
otsingu_viide=tk.StringVar() #IntVar() #Muudame StringVar-iks, et saaksime salvestada algse nime
otsingu_viide.set("")
tk.Label(aken, text="Nimi: ",font=("Calibri",10),fg="green").place(x=-0, y=0 )
nimi_entry=tk.Entry(aken)
nimi_entry.place(x=38, y=0 )
tk.Label(aken, text="E-mail: ",font=("Calibri",10),fg="green").place(x=-0, y=25 )
email_entry=tk.Entry(aken)
email_entry.place(x=47, y=25 )
tk.Label(aken, text="Telefon: ",font=("Calibri",10),fg="green").place(x=-0, y=50 )
telefon_entry=tk.Entry(aken)
telefon_entry.place(x=52, y=50 )

nupude_rida=tk.Frame(aken)
nupude_rida.pack(pady=0)
nupude_rida0=tk.Frame(aken)
nupude_rida0.pack(pady=0)
nupude_rida1=tk.Frame(aken)
nupude_rida1.pack(pady=0)
nupude_rida2=tk.Frame(aken)
nupude_rida2.pack(pady=0)
nupude_rida3=tk.Frame(aken)
nupude_rida3.pack(pady=0)
nupude_rida4=tk.Frame(aken)
nupude_rida4.pack(pady=0)
nupude_rida5=tk.Frame(aken)
nupude_rida5.pack(pady=0)
nupude_rida6=tk.Frame(aken)
nupude_rida6.pack(pady=0)
nupude_rida7=tk.Frame(aken)
nupude_rida7.pack(pady=0)
nupude_rida8=tk.Frame(aken)
nupude_rida8.pack(pady=0)

tk.Button(nupude_rida, text="Kuva kontaktid", command=kuva_kontaktid,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida0, text="Kuva kontakti email", command=kuva_emailid,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida1, text="Kuva telefon_nimi", command=kuva_nimi_telefon,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida2, text="Lisa kontakt", command=lisa_kontakt_gui,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida3, text="Otsi kontakt", command=otsi_kontakt_gui,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida4, text="Muuda kontakt", command=muuda_kontakt_gui,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida5, text="Kustuta kontakt", command=kustuta_kontakt_gui,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida6, text="Sorteeri_kontakt", command=sorteeri_gui,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida7, text="Sorteeri kontakt telefoni jargi", command=sorteeri_num,font=("Goudy Stout",8),fg="green").pack()
tk.Button(nupude_rida8, text="Sorteeri kontakt emaili jargi", command=sorteeri_email,font=("Goudy Stout",8),fg="green").pack(side="right",pady=0)
tk.Button(nupude_rida8, text="Sorteeri kontakt Z-A", command=sorteeri_za,font=("Goudy Stout",8),fg="green").pack(side="right",pady=0)

tekstikast = tk.Text(aken, height=13, width=65)
tekstikast.pack(pady=5, side="left")

aken.mainloop()



