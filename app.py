from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/about.html')
def about():  # put application's code here
    return render_template("about.html")

@app.route('/contact.html')
def contact():  # put application's code here
    return render_template("contact.html")

@app.route('/services.html')
def services():  # put application's code here
    return render_template("services.html")

@app.route('/gallery.html')
def gallery():  # put application's code here
    return render_template("gallery.html")

@app.route('/qgfx.html')
def qgfx():  # put application's code here
    return render_template("qgfx.html")

@app.route('/snet.html')
def snet():  # put application's code here
    return render_template("snet.html")

@app.route('/bar-gradient.html')
def bar():  # put application's code here
    return render_template("bar-gradient.html")

if __name__ == '__main__':
    app.run()




