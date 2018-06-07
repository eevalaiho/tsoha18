from application import db
from application.models import Base
from application.ttarget.models import Ttarget

class Analysis(Base):
    __tablename__ = "analysis"

    companyid = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(2000), nullable=False)
    locked = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, companyid, name, keywords, locked):
        self.companyid = companyid
        self.name = name
        self.keywords = keywords
        self.locked = locked

    def get_ttargets(self):
        return Ttarget.query.filter(Ttarget.analysisid.__eq__(self.id)).all()







