from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get("form_type") == "anketa":
            return redirect(url_for("tvorba_anket"))
            
        elif request.form.get("form_type") == "prihlaseni":
            jmeno = request.form.get("element3")
            prijmeni = request.form.get("element4")
            return redirect(url_for("prihlaseni", jmeno = jmeno, prijmeni = prijmeni ))
    return render_template("html.html")


@app.route("/tvorba_anket", methods=["GET"])
def tvorba_anket():
    ot = request.args.get("ot")
    moz = request.args.get("moz")
    return render_template("tvorba_anket.html", ot=ot, moz=moz)

@app.route("/prihlaseni", methods=["GET"])
def prihlaseni():
    jmeno = request.args.get("jmeno")
    prijmeni = request.args.get("prijmeni")
    return render_template("prihlaseni.html", jmeno=jmeno, prijmeni=prijmeni)

if __name__ == "__main__":
    app.run(debug=True)