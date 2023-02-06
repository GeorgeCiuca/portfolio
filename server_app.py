from flask import Flask, render_template, request
from datetime import datetime
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_txt(data)
            write_to_csv(data)
            return render_template("thankyou.html")
        except:
            return "did not save to database"
    else:
        return "something went wrong"


def write_to_txt(data):
    with open("portfolio_form.txt", mode="a", encoding="utf-8") as my_file:
        my_file.write(f"{datetime.now()}\n")
        for item in data:
            my_file.write(f"{item}:{data.get(item)}\n")
        my_file.write("\n")


def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

