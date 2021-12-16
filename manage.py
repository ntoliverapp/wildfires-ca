from app import db
from models import Wildfire

def init_wildfire_db(filename):
    db.create_all()
    print('Initialized Wildfire Database')
    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.strip().split(",")
            # print(data)
            print(data[1])

            data = Wildfire(image_url=data[0], name=data[1], acres_burned=data[2], admin_unit=data[3],archive_year=data[4], control_statement=data[5], counties=data[6],latitude=data[7], longitude=data[8], location=data[9],major_incident=data[10], search_description=data[11], start_date=data[12], start_time=data[13],extinguish_date=data[14], extinguish_time=data[15], updated_date=data[16],updated_time=data[17])
            
            db.session.add(data)
            db.session.commit()
    print('Wildfire Database Successfully Imported')


if __name__ == '__main__':
    init_wildfire_db("/Users/appleadmin2/Desktop/Wildfire.csv")