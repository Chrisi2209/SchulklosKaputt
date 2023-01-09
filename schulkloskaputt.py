from app import app, db
from app.models import Toilet, User

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Toilet": Toilet, "User": User}
