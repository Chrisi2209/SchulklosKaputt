from app import app, db, logger
from app.models import Toilet
from app.forms import NeuesKloForm, KloLöschenForm
from flask import render_template, flash, redirect, url_for, jsonify

# Decorator to log request to this function as get request
def log_get_request(func):
    def wrapper():
        logger.info("GET " + url_for(func.__name__))
        print("decorator durchgeführt")
        func()

    return wrapper


@app.route("/") 
@app.route("/index") 
def index(): 
    logger.info("GET " + url_for("index"))
    return render_template("index.html", title="HTL-Mödling kaputte klos", anzahl=len(Toilet.query.all()))

@app.route("/index/refresh-counter")
def refresh_index():
    logger.info("GET " + url_for("refresh_index"))
    return jsonify(counter=len(Toilet.query.all()))

@app.route("/kloansicht", methods=["GET", "POST"])
def kloansicht():
    # Klos sortieren, um sie fallweise auszugeben
    sorted_toilet_names = [toilet.__str__() for toilet in Toilet.query.all()]
    sorted_toilet_names.sort()

    form = NeuesKloForm()
    if form.is_submitted():
        if not form.validate():
            logger.info("POST " + url_for("kloansicht") + " provided data declined")
            return render_template("kloansicht.html", title="HTL-Mödling Kloansicht", 
                        kaputte_klos=sorted_toilet_names, form=form, anchor="#addToiletForm")
        
        gender = True if form.gender.data == "female" else False
        # Klo hinzufügen
        added_toilet = Toilet(building=form.building.data, floor=form.floor.data, 
                            room=form.room.data, gender=gender, pissoir=form.pissoir.data, toilet=form.toilet.data)
        db.session.add(added_toilet)
        db.session.commit()
        
        logger.info("POST " + url_for("kloansicht") + " added: <" + added_toilet.__str__() + ">")
        flash("Klo erfolgreich hinzugefügt")
        return redirect(url_for("index"))

    logger.info("GET " + url_for("kloansicht"))
    return render_template("kloansicht.html", title="HTL-Mödling Kloansicht", 
                           kaputte_klos=sorted_toilet_names, form=form, anchor="")


@app.route("/kloansicht/<klo>", methods=["GET", "POST"])
def kloansicht_klo(klo):
    form = KloLöschenForm()
    if form.validate_on_submit():
        # Get all toilets with this name
        kloDb = [i for i in Toilet.query.all() if i.__str__() == klo]
        print(kloDb)
        if len(kloDb) == 0:  # if this toilet doesn't exist
            logger.info("POST " + url_for("kloansicht") + f"/{klo} <toilet already deleted>")
            flash("Fehlgeschlagen: Dieses Klo wurde bereits entfernt!")
            return redirect(url_for("index"))

        # delete toilet
        db.session.delete(kloDb[0])
        db.session.commit()
        logger.info("POST " + url_for("kloansicht") + f"/{klo} <toilet deleted>")
        flash(f'{klo} entfernt') 
        return redirect(url_for("index"))

    logger.info("GET " + url_for("kloansicht") + f"/{klo}")
    # Safetycheck the toilet exists
    if klo in [toilet.__str__() for toilet in Toilet.query.all()]:
        return render_template("klobearbeitung.html", title=f"HTL-Mödling {klo} bearbeiten", klo=klo, form=form)
    else:
        flash("Fehlgeschlagen: Dieses Klo existiert nicht")
        return redirect(url_for("kloansicht"))


@app.route("/help")
def help():
    logger.info("GET " + url_for("help"))
    return render_template("help.html", title="HTL-Mödling kaputte Klos")
