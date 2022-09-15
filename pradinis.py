from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/<name>")
def antra(name):
    return render_template("antra_uzduotis.html", content=name)


@app.route("/trecia_uzduotis.html")
def trecia():
    return render_template("trecia_uzduotis.html")


@app.route("/ketvirta_uzduotis.html", methods=['GET', 'POST'])
def ketvirta():
    if request.method == "POST":
        year = request.form['metai']
        ivest_met = int(year)
        if (ivest_met % 400 == 0) or (ivest_met % 100 != 0 and ivest_met % 4 == 0):
            r = f"{ivest_met} yra keliamieji"
            return render_template("metai_keliamieji.html", Metai=r)
        else:
            r = f"{ivest_met} yra nekeliamieji"
            return render_template("metai_nekeliamieji.html", Metai=r)
    else:
        return render_template("ketvirta_uzduotis.html")


@app.route("/metai_keliamieji.html")
def keliamieji():
    return render_template("metai_keliamieji.html")


@app.route("/metai_nekeliamieji.html")
def nekeliamieji():
    return render_template("metai_nekeliamieji.html")


if __name__ == "__main__":
    app.run()
