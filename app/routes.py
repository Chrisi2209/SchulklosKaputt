from app import app
from app.forms import NeuesKloForm, KloLöschenForm
from flask import render_template, flash, redirect, url_for
 
kaputte_klos = []

@app.route("/") 
@app.route("/index") 
def index(): 
    return render_template("index.html", title="HTL-Mödling kaputte klos", anzahl=len(kaputte_klos))

@app.route("/kloansicht", methods=["GET", "POST"])
def kloansicht():
    form = NeuesKloForm()
    if form.validate_on_submit():
        composed_name = (f"{form.gebäudenummer.data:02d}{form.stocknummer.data:02d}{form.zimmernummer.data:02d}:Pissoir:{form.klonummer.data:02d}" 
                        if form.pissoir.data else 
                         f"{form.gebäudenummer.data:02d}{form.stocknummer.data:02d}{form.zimmernummer.data:02d}:Klo:{form.klonummer.data:02d}")
        kaputte_klos.append(composed_name)
        return redirect(url_for("index"))

    return render_template("kloansicht.html", title="HTL-Mödling Kloansicht", kaputte_klos=kaputte_klos, form=form)

@app.route("/kloansicht/<klo>", methods=["GET", "POST"])
def kloansicht_klo(klo):
    form = KloLöschenForm()
    if form.validate_on_submit(): 
        flash(f'deleted: {klo}') 
        kaputte_klos.remove(klo)
        return redirect(url_for("index"))

    if klo in kaputte_klos:
        return render_template("klobearbeitung.html", title=f"HTL-Mödling {klo} bearbeiten", klo=klo, form=form)
    else:
        return redirect(url_for("kloansicht"))
