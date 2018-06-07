from application import db
from application.models import Base

class Ttarget(Base):
    __tablename__ = "ttarget"

    analysisid = db.Column(db.Integer, db.ForeignKey('analysis.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    # The following data is to be gathered through crawling and analyzing the data
    title = db.Column(db.String(255))
    type = db.Column(db.Integer)

    def __init__(self, analysisid, url):
        self.analysisid = analysisid
        self.url = url





