
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test')
def Test():
    return render_template("test.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("results.html")


@app.route('/soil')
def soil():
    return render_template('soil.html')


@app.route('/soil/<loc>')
def soil_Location(loc):
    return render_template(loc+'.html')


def get(ele):
    if ele.empty:
        return 'Not Updated'
    return ele.to_string(index=False)


@app.route('/soil/<loc>/<cityname>')
def customCity(loc, cityname):
    soil = pd.read_csv('static/assets/soilTexture.csv')
    city = soil[soil.Loc == loc+'-'+cityname]
    pd.set_option('display.max_colwidth', None)
    # if city.empty:
    #     return render_template('404.html')
    # print(city)
    print('\n\n\n\n\n\n', city.crop, '\n\n\n\n\n\n')
    return render_template('citySoil.html', 
                           city=get(city.district), 
                           lat=get(city.lat), 
                           long=get(city.long), 
                           soil=get(city.texture), 
                           crop=get(city.crop), 
                           reference=get(city.reference),
                           mapImg=get(city.Map))


if __name__ == '__main__':
    app.debug = True
    app.run()
