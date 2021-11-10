from operator import ne
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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


class DailyReports(db.Model):
    date_recorded = db.Column(db.String(200), primary_key=True)
    ProvinceState = db.Column(db.String(200), primary_key=True)
    CountryRegion = db.Column(db.String(200), primary_key=True)
    CombinedKeys = db.Column(db.String(200))
    Confirmed = db.Column(db.Integer)
    Deaths = db.Column(db.Integer)
    Recovered = db.Column(db.Integer)
    Active = db.Column(db.Integer)


@app.route("/time_series/<type>", methods=["POST", "GET"])
def addTimeSeries(type):
    if request.method == "POST":
        keys = (
                    'Province/State',
                    'Country/Region',
                    'Lat',
                    'Long',
                )
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
                for key in keys:
                    if key not in time_entry:
                        return "Incorrect formatting for uploaded csv file"

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


@app.route("/daily_reports/<date>", methods=["POST", "GET"])
def addDailyReports(date):
    try:
      to_date = datetime.strptime(date, '%m-%d-%y')
    except (ValueError, TypeError):
      return "Incorrect date format"
    
        
    format_date = to_date.strftime('%m/%d/%y')
    if request.method == "POST":
        keys = (
                    'FIPS',
                    'Admin2',
                    'Province_State',
                    'Country_Region',
                    'Last_Update',
                    'Lat',
                    'Long_',
                    'Confirmed',
                    'Deaths',
                    'Recovered',
                    'Active',
                    'Combined_Key',
                    'Incident_Rate',
                    'Case_Fatality_Ratio'
                )
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
            db.session.query(DailyReports).delete()
            db.session.commit()
            for time_entry in csv_dicts:
                for key in keys:
                    if key not in time_entry:
                        return "Incorrect formatting for uploaded csv file"
                    
                new_entry = DailyReports(
                    date_recorded=format_date, ProvinceState=time_entry[
                        'Province_State'], CountryRegion=time_entry['Country_Region'],
                    CombinedKeys=time_entry['Combined_Key'], Confirmed=time_entry['Confirmed'], Deaths=time_entry['Deaths'],
                    Recovered=time_entry['Recovered'], Active=time_entry['Active'])
                db.session.add(new_entry)

            db.session.commit()
            entries = DailyReports.query.order_by(
                DailyReports.CountryRegion).all()
            return render_template("daily_reports.html", date=date, entries=entries)
        except:
            return "There was an issue with the uploaded file"
    else:
        #entries = TimeSeries.query.order_by(TimeSeries.CountryRegion).all()
        return render_template("daily_reports.html", date=date)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/time_series", methods=["POST", "GET"])
def time_series_home():
    return render_template("time_series.html")


@app.route("/daily_reports", methods=["POST", "GET"])
def daily_reports_home():
    if request.method == "POST":
        entry_date = request.form["date"]
        return redirect(f"/daily_reports/{entry_date}")
    else:
        return redirect("/")

@app.route("/daily_reports/", methods=["POST", "GET"])
def no_date():
    return "Please enter a date"


if __name__ == "__main__":
    app.run(debug=True)
