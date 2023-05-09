from app import app, db, logger
from app.models import Toilet, User
from app.forms import NeuesKloForm, KloLöschenForm, LoginForm
from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import current_user, login_user, login_required, logout_user
import random

# A chance to get rick rolled
def rick_roll():
    CHANCE_IN_PERCENT = 0
    if random.randint(1, 100) <= CHANCE_IN_PERCENT:
        logger.info("Someone just got rickrolled")
        return True
    
    return False

##### fully available to everyone
@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", authenticated=current_user.is_authenticated,)

@app.route("/") 
@app.route("/index") 
@app.route("/home")
def index():
    if rick_roll():
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    logger.info("GET " + url_for("index"))
    return render_template("index.html", title="HTL-Mödling kaputte klos", authenticated=current_user.is_authenticated, anzahl=len(Toilet.query.all()), 
                           number100_val=len(Toilet.query.all()) // 100,
                           number10_val=len(Toilet.query.all()) % 100 // 10,
                           number1_val=len(Toilet.query.all()) % 100 % 10)

@app.route("/index/refresh-counter")
def refresh_index():
    logger.info("GET " + url_for("refresh_index"))
    return jsonify(counter=len(Toilet.query.all()))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user already logged in
    if current_user.is_authenticated:
        flash("Bereits eingeloggt")
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # if submitted
        # get a user that matches the username
        user = User.query.filter_by(username=form.username.data).first()
        # if no user with that username or the password is incorrect, login failed
        if user is None or not user.compare_password(form.password.data):
            return render_template('login.html', title='Sign In', form=form, errorMessage='Ungültiger Benutzername oder Passwort', authenticated=current_user.is_authenticated,)
        # if login succeeded, login the user and return to index
        login_user(user, remember=form.remember_me.data)
        flash("login erfolgreich")

        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form, authenticated=current_user.is_authenticated,)


@app.route("/help")
def help():
    if rick_roll():
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
    logger.info("GET " + url_for("help"))
    return render_template("help.html", title="HTL-Mödling kaputte Klos", authenticated=current_user.is_authenticated,)


### API
@app.route("/API/get-counter")
def api_get_counter():
    return jsonify(counter = len(Toilet.query.all()))

####### Only partially
@app.route("/kloansicht", methods=["GET"])
def kloansicht():
    # Klos sortieren, um sie fallweise auszugeben
    sorted_girl_toilet_names = [toilet.__str__() for toilet in Toilet.query.filter_by(gender=True).all()]
    sorted_girl_toilet_names.sort()
    sorted_boy_toilet_names = [toilet.__str__() for toilet in Toilet.query.filter_by(gender=False).all()]
    sorted_boy_toilet_names.sort()

    logger.info("GET " + url_for("kloansicht"))
    return render_template("kloansicht.html", title="HTL-Mödling Kloansicht", broken_girl_toilets=sorted_girl_toilet_names,
                           broken_boy_toilets=sorted_boy_toilet_names, authenticated=current_user.is_authenticated)


####### Only available for administrators
@app.route("/kloansicht/<klo>", methods=["GET", "POST"])
def kloansicht_klo(klo):
    if not current_user.is_authenticated:
        flash("Dafür musst du angemeldet sein!")
        return redirect(url_for("index"))

    form = KloLöschenForm()
    if form.validate_on_submit():
        # Get all toilets with this name
        kloDb = [i for i in Toilet.query.all() if i.__str__() == klo]
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
        return render_template("klobearbeitung.html", title=f"HTL-Mödling {klo} bearbeiten", klo=klo, form=form, authenticated=current_user.is_authenticated,)
    else:
        flash("Fehlgeschlagen: Dieses Klo existiert nicht")
        return redirect(url_for("kloansicht"))


@app.route("/klo-anmelden", methods=["GET", "POST"])
def klo_anmelden():
    if not current_user.is_authenticated:
        flash("Dafür musst du angemeldet sein!")
        return redirect(url_for("index"))

    form = NeuesKloForm()
    if form.is_submitted():
        # didnt pass validation
        if not form.validate():
            logger.info("POST " + url_for("klo_anmelden") + " provided data declined")
            return render_template("klo_anmelden.html", title="HTL-Mödling Kloansicht", form=form, authenticated=current_user.is_authenticated)
        
        gender = True if form.gender.data == "female" else False
        # no pissoir in female toilets
        if gender == True and form.pissoir.data == True:
            return render_template("klo_anmelden.html", title="HTL-Mödling Kloansicht", form=form, 
                                   authenticated=current_user.is_authenticated, error_message="Mädchenklos verfügen über keine Pissoire")

        # add toilet
        added_toilet = Toilet(building=form.building.data, floor=form.floor.data, 
                            room=form.room.data, gender=gender, pissoir=form.pissoir.data, toilet=form.toilet.data)
        db.session.add(added_toilet)
        db.session.commit()
        
        logger.info("POST " + url_for("kloansicht") + " added: <" + added_toilet.__str__() + ">")
        flash("Klo erfolgreich hinzugefügt")
        return redirect(url_for("index"))

    return render_template("klo_anmelden.html", title="kaputtes Klo anmelden", form=form, authenticated=current_user.is_authenticated)

   
@app.route("/logout")
@login_required
def logout():
    flash("Logout erfolgreich")
    logout_user()
    return redirect(url_for('index'))
