from flask import Flask, render_template, request
import smtplib
import requests

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"
app = Flask(__name__)

app = Flask(__name__)

posts = []


@app.route('/')
def home():
    global posts
    data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    posts = data
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        return render_template('contact.html', message="Successfully sent message")
    else:
        return render_template('contact.html', message="Contact Me")


@app.route('/post/<int:index>')
def get_blog_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
