from application import db

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(255), nullable=False)
    agreementlevel = db.Column(db.Integer, default=1, nullable=False) # Default agreement level is 1=Basic

    def __init__(self, name):
        self.name = name
        self.done = False