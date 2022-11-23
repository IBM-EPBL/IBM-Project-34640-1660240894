from flask import Flask , render_template

app= Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/facts")
def facts():
    return render_template('facts.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/newuser")
def newuser():
    return render_template('newuser.html')

@app.route("/compatibility")
def compatibility():
    return render_template('compatibility.html')

@app.route("/eligibility")
def eligibility():
    return render_template('eligibility.html')

@app.route("/register")
def register():
    return render_template('registration.html')





if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5500 ,debug=True)