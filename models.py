from sqlalchemy import desc, asc
from app import db

class Wildfire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text)
    name = db.Column(db.Text, nullable=False)
    acres_burned = db.Column(db.Text)
    admin_unit = db.Column(db.Text)
    archive_year = db.Column(db.Text)
    control_statement = db.Column(db.Text)
    counties = db.Column(db.Text)
    latitude = db.Column(db.Text)
    longitude = db.Column(db.Text)
    location = db.Column(db.Text)
    major_incident = db.Column(db.Text)
    search_description = db.Column(db.Text)
    start_date = db.Column(db.Text)
    start_time = db.Column(db.Text)
    extinguish_date = db.Column(db.Text)
    extinguish_time = db.Column(db.Text)
    updated_date = db.Column(db.Text)
    updated_time = db.Column(db.Text)
    
    @staticmethod
    def newest(num):
        return Wildfire.query.order_by(desc(Wildfire.name)).limit(num)
    
    @staticmethod
    def display(num):
        return Wildfire.query.order_by(asc(Wildfire.name)).limit(num)
    
    @staticmethod
    def search_results():
        return Wildfire.query.order_by(asc(Wildfire.name)).all()
    
    def __Repr__(self):
        return "<Wildfire '{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}''{}'>".format(self.id, self.image_url, self.name, self.acres_burned, self.admin_unit, self.archive_year, self.condition_statement, self.control_statement, self.counties, self.latitude, self.longitude, self.location, self.major_incident, self.search_description, self.start_date, self.start_time, self.extinguish_date, self.extinguish_time, self.updated_time)