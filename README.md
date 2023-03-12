# Směnárna

**Zadání**:
Vytvořte aplikaci pro obsluhu směnárny s výběrem zahraničních měn se zadáním nákupu či prodeje ze strany směnárny se zobrazením kurzovního lístku. 

**Pokyny ke zpracování:**   
1. Pro výběr nákupu nebo prodeje zvolte vhodnou výběrovou komponentu (přepínač).
2. Pro výběr měny volíme nejlépe rozbalovací seznam (OptionMenu).
3. V případě nákupu se zadává vstupní částka ve vybrané měně a program počítá částku v Kč, kterou má směnárna vyplatit klientovi  (od částky se odečítá poplatek 0,5%).
4. V případě prodeje se zadává vstupní částka ve vybrané měně a program počítá částku v Kč, kterou má klient zaplatit směnárně (k částce se připočte poplatek 0,5%).
5. V obou případech se zobrazí **celková částka, základ i částka, kterou činí poplatek** v korunách zaokrouhlených na desetiny Kč se zobrazením dvou desetinných míst (např. 125,20 Kč).
6. U celkové částky by se měl objevit výrazný text, zda částka **má být vyplacena nebo vybrána**.
7. Všechny vstupy je třeba ošetřit proti chybnému zadání, případně nevybrání hodnot (v případě měny a nákupu x prodeje).
8. Aplikace bude obsahovat rovněž kurzovní lístek s minimálně 4 měnami, který obsahuje:
    - Zkratku měny 	(př. HUF)
    - Stát 		(př. Maďarsko)
    - Množství 		(př. 100)
    - Střední cenu 	(př. 20,063)
9.  Částky, které jsou uvedeny v kurzovním lístku, musí být použity pro výpočet!
10. Kurzovní lístek musí být umístěn ve vedlejším okně pomocí komponenty Text. Toto okno musí jít otevřít pouze jedno!
11. Aplikace na vhodném místě v hlavním okně zobrazuje aktuální čas – hodiny, minuty a sekundy.
