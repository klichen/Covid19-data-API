from operator import ne
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time
import csv
import sys
import pickle
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class TimeSeries(db.Model):
    ProvinceState = db.Column(db.String(200), primary_key=True)
    CountryRegion = db.Column(db.String(200), primary_key=True)
    date_recorded = db.Column(db.String(200), primary_key=True)
    quantity = db.Column(db.Integer)
    case_type = db.Column(db.String(200), primary_key=True)

    def __rep__(self):
        return "<Entry %r>" % self.firstname

    # TO TEST
    def __init__(self):
        self.ProvinceState = ""
        self.CountryRegion = "Mitski"
        self.date_recorded = "01-01-2000"
        self.quantity = 100
        self.case_type = "time_series"


@app.route("/time_series/<type>", methods=["POST", "GET"])
def addTimeSeries(type):
    if request.method == "POST":
        try:
            f = request.files['fileupload']

            # store the file contents as a string
            fstring = f.read()
            print(fstring.decode("utf-8"), file=sys.stderr)
            # create list of dictionaries keyed by header row
            data = fstring.decode("utf-8")
            csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(
                data.splitlines(), skipinitialspace=True)]
            print(csv_dicts, file=sys.stderr)
            db.session.query(TimeSeries).delete()
            db.session.commit()
            for time_entry in csv_dicts:
                for date, number in list(time_entry.items())[4:]:
                    to_date = datetime.strptime(
                        date, '%m/%d/%y').strftime('%m/%d/%y')
                    new_entry = TimeSeries(
                        ProvinceState=time_entry['Province/State'], CountryRegion=time_entry['Country/Region'],
                        date_recorded=to_date, quantity=number, case_type=type)
                    db.session.add(new_entry)

            db.session.commit()
            entries = TimeSeries.query.order_by(TimeSeries.CountryRegion).all()
            return render_template("data.html", type=type, entries=entries)
        except:
            return "There was an issue with the uploaded file"

    else:
        entries = TimeSeries.query.order_by(TimeSeries.CountryRegion).all()
        return render_template("data.html", type=type, entries=entries)

@app.route("/", methods=["POST", "GET"])
def index():
        return render_template("index.html")

@app.route("/time_series", methods=["POST", "GET"])
def time_series_home():
        return render_template("time_series.html")

@app.route("/time_series/<type>/query", methods=["POST", "GET"])
def ts_query(type):
    if request.method == "POST":
        column = request.form['column']
        places = request.form['places']
        dates = request.form['dates']
        data = [type]
        # data = request.form['data'] (for daily report)

        # now that we have all the input, return the requested data 
        places_lst = places.split(",")
        dates_lst = dates.split(",")
        # data_lst = data.split(",") (for daily report)

        #if csv
        result = print_csv(column, places_lst, dates_lst, data)

        if result == "ERROR":
            return "There was an issue with the parameters used"
            #redirect('/time_series/<type>/query')

        #elif JSON:

        return render_template('displayquery.html', result=result)
    else:
        # delete this ?
        column = ""
        places_lst = ["aa"]
        dates_lst = []
        return render_template('tsquery.html', type=type)
""" 
@app.route("/time_series/query/csv", methods=["POST", "GET"])
def ts_csv():
 """

def print_csv(column, places_lst, dates_lst, data):
    header=""
    result = ""
    if column == "ProvinceState":
        header += "ProvinceState"
            
    elif column == "CountryRegion":
        header += "CountryRegion"
        #for place in places_lst:
        #    TimeSeries.query.

        curr = TimeSeries.query.filter_by(CountryRegion='Afghanistan').first()
        return header + curr.CountryRegion + curr.case_type + curr.quantity

    else:
        return "ERROR"



    return result


if __name__ == "__main__":
    app.run(debug=True)