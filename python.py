from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/", methods =["POST", "GET"])

def funkce():
   
    pozadavek = request.form.get("element1")
    
    return render_template("html.html", zadane = pozadavek)

def anketa():
    poleot = []
    polemoz = []
    print("Vytvoř anketu")
    pocetotazek = input("Kolik chceš, aby měla anketa otázek? :")
    pocetnavyber = input("Kolik bude mít každá otázka na výběr odpovědí? : ")
    pocetotazek = int(pocetotazek)
    pocetnavyber = int(pocetnavyber)

    for i in range(pocetotazek):
        otazka = input("Zadej otázku : ")
        poleot.append(otazka)
        for i in range(pocetnavyber):
            moznost = input("Zadej možnost : ")
            polemoz.append(moznost)

    print("Otázky : ",poleot)
    print("Možnosti : ",polemoz)
anketa()
if __name__ =="__main__":
    app.run(debug=True)