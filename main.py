
from flask import Flask, render_template ,request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test')
def Test():
    return render_template("test.html")

@app.route('/result', methods = ['GET', 'POST'])
def result():
    return render_template("results.html")

@app.route('/soil')
def soil():
    return render_template('soil.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

