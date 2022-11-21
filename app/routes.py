from app import app
from app.forms import NeuesKloForm, KloLöschenForm
from flask import render_template, flash, redirect
 
kaputte_klos = ["a"]

@app.route("/") 
@app.route("/index") 
def index(): 
    return render_template("index.html", anzahl=len(kaputte_klos))

@app.route("/kloansicht", methods=["GET", "POST"])
def kloansicht():
    form = NeuesKloForm()
    if form.validate_on_submit():
        composed_name = (f"{form.gebäudenummer.data:02d}{form.stocknummer.data:02d}{form.zimmernummer.data:02d}:{form.klonummer.data:02d}:Pissoir" 
                        if form.pissoir.data else 
                         f"{form.gebäudenummer.data:02d}{form.stocknummer.data:02d}{form.zimmernummer.data:02d}:{form.klonummer.data:02d}:Klo")
        kaputte_klos.append(composed_name)
        return redirect('/index')

    return render_template("kloansicht.html", kaputte_klos=kaputte_klos, form=form)

@app.route("/kloansicht/<klo>", methods=["GET", "POST"])
def kloansicht_klo(klo):
    form = KloLöschenForm()
    if form.validate_on_submit(): 
        flash(f'deleted: {klo}') 
        kaputte_klos.remove(klo)
        return redirect('/index')

    if klo in kaputte_klos:
        return render_template("klobearbeitung.html", klo=klo, form=form)
    else:
        return redirect("/kloansicht")
