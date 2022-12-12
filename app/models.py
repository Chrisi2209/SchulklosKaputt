from app import db

class Toilet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.Integer, index=True)
    floor = db.Column(db.Integer, index=True)
    room = db.Column(db.Integer, index=True)
    gender = db.Column(db.Boolean, index=True)  # true = girl, false = boy
    pissoir = db.Column(db.Boolean, index=True)
    toilet = db.Column(db.Integer, index=True)

    def __repr__(self):
        genderStr = "M" if self.gender else "K"
        name = f"{genderStr}{self.building:02d}{self.floor:02d}{self.room:02d}:Pissoir:{self.toilet:02d}" \
               if self.pissoir else \
               f"{genderStr}{self.building:02d}{self.floor:02d}{self.room:02d}:Sitzklo:{self.toilet:02d}"
        return name

    __str__ = __repr__