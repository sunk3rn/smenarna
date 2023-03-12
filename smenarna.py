from tkinter import *
from datetime import datetime

hlavni = Tk()
hlavni.minsize(400,300)
hlavni.title("Směnárna")
vyber = 0
mena = StringVar()
kurzovniListekOkno = Toplevel()
kurzovniListekOkno.title("Kurzovní lístek")
kurzovniListekOkno.minsize(300,100)

napis1 = Label(hlavni,text="Vyberte akci:",font="12",)
napis1.grid(row=0,column=0,stick=W)
vyberKoupit = Radiobutton(hlavni,text="Koupit",variable=vyber,value=1)
vyberProdat = Radiobutton(hlavni,text="Prodat",variable=vyber,value=2)
vyberKoupit.grid(row=1,column=0,sticky=W)
vyberProdat.grid(row=1,column=1,sticky=W)

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
vyberMena.grid(row=3,column=0)

napis3 = Label(hlavni,text="Zadejte castku:",font="12",)
napis3.grid(row=4,column=0,sticky=W)

vstupCastka = Entry(hlavni)
vstupCastka.grid(row=5,column=0)

tlacitkoVypocet = Button(text="Vypočítat")
tlacitkoVypocet.grid(row=6,column=0,sticky=W)


hlavni.mainloop()