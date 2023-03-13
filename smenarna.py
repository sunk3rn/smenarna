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

kurzy = {
    "USD": [22.21,"USA",1500],
    "EUR": [23.67,"EU",235],
    "GBP": [26.73,"Velká Británie",340],
    "JPY": [0.160,"Japonsko",150_000],
    "PXN": [1.2,"Mexiko",25000]
}


# Hlavni komponenta vedlejisho okna - pomoci Text()
kurzovniListek = Text(kurzovniListekOkno,width=60,height=10) 
kurzovniListek.pack(fill=BOTH, expand=1)
for meny,klic in kurzy.items():
    kurzovniListek.insert(END,f"{klic[1]} - Množství : {klic[2]} - 1 {meny} = {klic[0]} CZK\n")
kurzovniListek.grid(row=0,column=2,rowspan=10)

operace = StringVar(value="koupit") # Promena pro vyber operace
mena = StringVar(value="USD") # Promena pro vyber meny
vystupText = "" # Promena pro konecny vystup

# Cast 1 - Vyber operace
napis1 = Label(hlavni,text="Vyberte akci:",font="12",)
napis1.grid(row=0,column=0,stick=W)
vyberKoupit = Radiobutton(hlavni,text="Koupit",variable=operace,value="koupit")
vyberProdat = Radiobutton(hlavni,text="Prodat",variable=operace,value="prodat")
vyberKoupit.grid(row=1,column=0,sticky=W+N)
vyberProdat.grid(row=1,column=1,sticky=E+N)

# Cast 2 - Vyber meny
napis2 = Label(text="Vyberte měnu:",font="12",)
napis2.grid(row=2,column=0,sticky=W)

vyberMena = OptionMenu(hlavni,mena,*kurzy)
vyberMena.grid(row=3,column=1,sticky=N,padx=50)

#Cast 3 - Zadavani vstupni castky
napis3 = Label(hlavni,text="Zadejte částku:",font="12",)
napis3.grid(row=4,column=0,sticky=W)

vstupCastka = Entry(hlavni)
vstupCastka.grid(row=5,column=1,padx=50)

def vypocet(mena,castka,operace): # Hlavni vypocet, vstupem je zvolena mena, zadana castka a zvolena operace
    priplatek = 0.5 / 100
    if operace == "koupit":
        vystupniCena = castka * mena * (1 - priplatek)
        vystupniPoplatek = castka * mena * priplatek
        pocatecniText = "Vyplácená částka je:"
        return (pocatecniText,vystupniCena,vystupniPoplatek)

    elif operace == "prodat":
        vystupniCena = castka * mena * (1 + priplatek)
        vystupniPoplatek = castka * mena * priplatek
        pocatecniText = "Vybíraná částka je:"
        return (pocatecniText,vystupniCena,vystupniPoplatek)

def aktualizaceVystupu(): # Aktualizuje text v Labelu vystup na 7 radku
    castka = float(vstupCastka.get())
    mena2 = kurzy.get(mena.get())
    mena2 = mena2[0]
    operace2 = operace.get()
    pocatecniText,vystupniCena,vystupniPoplatek = vypocet(mena2,castka,operace2)
    vystup["text"] = "{} {:.2f} Kč, základ je:{:.2f} a poplatek: {:.2f}".format(pocatecniText,vystupniCena,castka,vystupniPoplatek)

def aktualizaceHodin(): # Aktualizuje hodiny
    hodiny["text"]= datetime.now().strftime("%H:%M:%S")
    hlavni.after(1000, aktualizaceHodin)

hodiny = Label(hlavni)
hodiny.grid(row=0,column=3,sticky=E)

aktualizaceHodin()

vystup = Label(hlavni,text=vystupText,font='bold',foreground="red")
vystup.grid(row=7,column=0,columnspan=5)

tlacitkoVypocet = Button(text="Vypočítat",command=aktualizaceVystupu)
tlacitkoVypocet.grid(row=6,column=1,sticky=N)

hlavni.mainloop()