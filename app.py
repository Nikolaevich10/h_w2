from flask import Flask
from faker import Faker
import requests
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/requirements/')
def req():
    with open('requirements.txt') as file:
        text = file.read()
    return f'{text}'


@app.route('/generate-users/')
def users():
    f = Faker()
    user = []
    for i in range(100):
        name = f.name()
        mail = "".join(name.split()) + "@mail.com"
        user_name = name + " : " + mail.lower()
        user.append(user_name)

    return f'{user}'


@app.route('/mean/')
def heiwei():
    pounds = 0.453592  # кг
    inches = 2.54  # см
    with open('templates/hw.csv') as csvfile:
        reader_object = csv.DictReader(csvfile, delimiter=",")
        height, weight = 0, 0
        for row in reader_object:
            height += float(row["Height(Inches)"])
            weight += float(row["Weight(Pounds)"])
        kol = int(row['Index'])

    return f'Средний рост: {(height/kol)*inches} см, Средний вес: {(weight/kol)/pounds} кг'


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    a = r.json()["number"]
    return f'<h3 style="margin:10% 10%">Космонавтов на орбите: {a} </h3>'


if __name__ == '__main__':
    app.run(debug=True)

