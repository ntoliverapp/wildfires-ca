from flask import Blueprint, Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from wildfires_ca.extensions import db
from wildfires_ca.models import Wildfire

main = Blueprint('main',__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
    
# app = Flask(__name__)
# config_file='config.py'
# app.config.from_pyfile(config_file)


# db = SQLAlchemy(app)
# import models


@main.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@main.route("/index/<int:id>")
def expanded(id):
    expanded = models.Wildfire.query.get_or_404(id)
    return render_template('expanded.html', expanded=expanded)

@main.route ("/search_result", methods=["GET", "POST"])
def search_result():
    name = request.form.get("name").capitalize()
    archive_year = request.form.get("archive_year")
    counties = request.form.get("counties").capitalize()

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    results = models.Wildfire.search_results() 

    for i in results:
        if (name in i.name) and (archive_year in i.archive_year) and (counties in i.counties):
            list1.append(i.name)
            list2.append(i.archive_year)
            list3.append(i.counties)
            list4.append(i.admin_unit)
            list5.append(i.search_description)
            list6.append(i.start_date)
            list7.append(i.extinguish_date)
            list8.append(i.image_url)

    return render_template("search_result.html", count=len(list1), result1=list1, result2 = list2, result3=list3, result4=list4, result5=list5, result6=list6, result7=list7, result8=list8)

@main.route("/database", methods=["POST", "GET"])
def database():
    return render_template("database.html", wildfires=models.Wildfire.display(30))

@main.route("/info", methods=["POST", "GET"])
def info():
    return render_template("info.html")

# if __name__ == "__main__":
#     app.run(debug=True)
    