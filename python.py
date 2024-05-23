from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/", methods =["POST", "GET"])

def funkce():
   
    pozadavek = request.form.get("element1")
    
    return render_template("html.html", zadane = pozadavek)

if __name__ =="__main__":
    app.run(debug=True)