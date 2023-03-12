from tkinter import *
from datetime import datetime

#Hlavni okno
hlavni = Tk()
hlavni.minsize(500,200)
hlavni.title("Směnárna")

#Vedlejsi okno - kurzovni listek
kurzovniListekOkno = Toplevel(hlavni)
kurzovniListekOkno.title("Kurzovní lístek")
kurzovniListekOkno.minsize(300,100)

operace = StringVar(value="koupit")
mena = StringVar(value="USD")
vystupText = ""

napis1 = Label(hlavni,text="Vyberte akci:",font="12",)
napis1.grid(row=0,column=0,stick=W)
vyberKoupit = Radiobutton(hlavni,text="Koupit",variable=operace,value="koupit")
vyberProdat = Radiobutton(hlavni,text="Prodat",variable=operace,value="prodat")
vyberKoupit.grid(row=1,column=0,sticky=W+N)
vyberProdat.grid(row=1,column=1,sticky=E+N)

kurzy = {
    "USD": 22.21,
    "EUR": 23.67,
    "GBP": 26.73,
    "JPY": 0.160,
}

kurzovniListek = Text(kurzovniListekOkno,width=30,height=10)
kurzovniListek.pack()
for meny,kurz in kurzy.items():
    kurzovniListek.insert(END,f"1 {meny} = {kurz} CZK\n")
kurzovniListek.grid(row=0,column=2,rowspan=10)


napis2 = Label(text="Vyberte měnu:",font="12",)
napis2.grid(row=2,column=0,sticky=W)

vyberMena = OptionMenu(hlavni,mena,*kurzy)
vyberMena.grid(row=3,column=1,sticky=N,padx=50)

napis3 = Label(hlavni,text="Zadejte částku:",font="12",)
napis3.grid(row=4,column=0,sticky=W)

vstupCastka = Entry(hlavni)
vstupCastka.grid(row=5,column=1,padx=50)

def vypocet(mena,castka,operace):
    priplatek = 0.5 / 100
    if operace == "koupit":
        vystupniCena = castka * mena * (1 - priplatek)
        vystupniPoplatek = castka * mena * priplatek
        return (vystupniCena,vystupniPoplatek)

    elif operace == "prodat":
        vystupniCena = castka * mena * (1 + priplatek)
        vystupniPoplatek = castka * mena * priplatek
        return (vystupniCena,vystupniPoplatek)

def aktualizaceVystupu():
    castka = float(vstupCastka.get())
    mena2 = kurzy.get(mena.get())
    operace2 = operace.get()
    vystupniCena,vystupniPoplatek = vypocet(mena2,castka,operace2)
    vystup["text"] = "Celková částka je: {:.2f} Kč, základ je:{:.2f} a poplatek: {:.2f}".format(vystupniCena,castka,vystupniPoplatek)

def aktualizaceHodin():
    hodiny["text"]= datetime.now().strftime("%H:%M:%S")
    hlavni.after(1000, aktualizaceHodin)

hodiny = Label(hlavni)
hodiny.grid(row=0,column=3,sticky=E)

aktualizaceHodin()

vystup = Label(hlavni,text=vystupText)
vystup.grid(row=7,column=0,columnspan=5)

tlacitkoVypocet = Button(text="Vypočítat",command=aktualizaceVystupu)
tlacitkoVypocet.grid(row=6,column=1,sticky=N)

hlavni.mainloop()