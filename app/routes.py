from app import app, db
from app.models import Toilet
from app.forms import NeuesKloForm, KloLöschenForm
from flask import render_template, flash, redirect, url_for, jsonify
 
kaputte_klos = []

@app.route("/") 
@app.route("/index") 
def index(): 
    return render_template("index.html", title="HTL-Mödling kaputte klos", anzahl=len(Toilet.query.all()))

@app.route("/index/refresh-counter")
def refresh_index():
    return jsonify(counter=len(Toilet.query.all()))


@app.route("/kloansicht", methods=["GET", "POST"])
def kloansicht():
    form = NeuesKloForm()
    if form.validate_on_submit():
        db.session.add(Toilet(building=form.building.data, floor=form.floor.data, 
                              room=form.room.data, pissoir=form.pissoir.data, toilet=form.toilet.data))
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("kloansicht.html", title="HTL-Mödling Kloansicht", 
                           kaputte_klos=[toilet.__str__() for toilet in Toilet.query.all()], form=form)

@app.route("/kloansicht/<klo>", methods=["GET", "POST"])
def kloansicht_klo(klo):
    form = KloLöschenForm()
    if form.validate_on_submit():
        flash(f'deleted: {klo}') 
        kloDb = [i for i in Toilet.query.all() if i.__str__() == klo][0]
        db.session.delete(kloDb)
        db.session.commit()
        return redirect(url_for("index"))

    if klo in [toilet.__str__() for toilet in Toilet.query.all()]:
        return render_template("klobearbeitung.html", title=f"HTL-Mödling {klo} bearbeiten", klo=klo, form=form)
    else:
        return redirect(url_for("kloansicht"))


@app.route("/help")
def help():
    return render_template("help.html", title="HTL-Mödling kaputte Klos")
