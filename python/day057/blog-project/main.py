from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<id>')
def get_post(id):
    post = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391/{int(id) - 1}").json()
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
