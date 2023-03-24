
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

@app.route('/Pakistan')
def Pakistan():
    return render_template('pakistan.html')

@app.route('/Punjab')
def Punjab():
    return render_template('punjab.html')

@app.route('/Sindh')
def Sindh():
    return render_template('sindh.html')

@app.route('/KPK')
def KPK():
    return render_template('kpk.html')

@app.route('/Balochistan')
def Balochistan():
    return render_template('balochistan.html')

@app.route('/Gilgit')
def Gilgit():
    return render_template('gilgit.html')

@app.route('/Kashmir')
def Kashmir():
    return render_template('kashmir.html')

@app.route('/Punjab/Attock')
def Attock():
    return render_template('attock.html')



if __name__ == '__main__':
    app.debug = True
    app.run()

