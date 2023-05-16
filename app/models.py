from __future__ import annotations
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Toilet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.Integer, index=True)
    floor = db.Column(db.Integer, index=True)
    room = db.Column(db.Integer, index=True)
    gender = db.Column(db.Boolean, index=True)  # true = girl, false = boy
    pissoir = db.Column(db.Boolean, index=True)
    toilet = db.Column(db.Integer, index=True)

    def __repr__(self):
        name = f"{self.building:02d}{self.floor:02d}{self.room:02d}:Pissoir:{self.toilet:02d}" \
               if self.pissoir else \
               f"{self.building:02d}{self.floor:02d}{self.room:02d}:Sitzklo:{self.toilet:02d}"
        return name
    
    __str__ = __repr__
    
    def __eq__(self, other: Toilet):
        return self.building == other.building and self.floor == other.floor and self.room == other.room and \
               self.gender == other.gender and self.pissoir == other.pissoir and self.toilet == other.toilet



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    password_hash = db.Column(db.String, index=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def compare_password(self, password):
        return check_password_hash(self.password_hash, password)

    # This is needed for the authentification system
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return f"<User {self.username}>"
    
    __str__ = __repr__
