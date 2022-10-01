from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.date.today().year
    return render_template('index.html', year=current_year)


@app.route('/guess/<name>')
def guess(name=None):
    data_gender = requests.get(f"https://api.genderize.io?name={name}").json()
    data_age = requests.get(f"https://api.agify.io?name={name}").json()
    return render_template('guess.html', name=name, gender=data_gender["gender"], years_old=data_age["age"])


@app.route('/blog')
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    posts = response.json()
    return render_template('blog.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
