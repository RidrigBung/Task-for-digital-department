from flask import Flask, render_template, url_for
from functions import get_today_date, get_tomorrow_date
app = Flask(__name__)

title = "Simple flask app"
pages = {"index": "Main page", "today": "Today's data",
         "tomorrow": "Tomorrow's data"}


@app.route('/')
def index():
    return render_template("index.html", title=title, pages=pages)


@app.route('/today')
def today():
    date_today = get_today_date()
    return render_template("today.html", title=title, date_today=date_today)


@app.route('/tomorrow')
def tomorrow():
    date_tomorrow = get_tomorrow_date()
    return render_template("tomorrow.html", title=title, date_tomorrow=date_tomorrow)


if __name__ == '__main__':
    app.run(debug=True)
