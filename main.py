
from flask import Flask, render_template, request, redirect, url_for
import ee
import collections
import pickle
import pandas as pd
from pickle import load
import math
app = Flask(__name__)
with open(f'regression_90_r2.pkl','rb') as f: 
    model = load(f)
with open(f'classes_acc_63.pkl','rb') as f1:
    model1 = load(f1)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test',methods = ["POST","GET"])
def test():
    if request.method == "POST":
        latitude = float(request.form["latitude"])
        longitude  = float(request.form["longitude"])
        start_date  = request.form["start_date"]
        end_date  = request.form["end_date"]
        collections.Callable = collections.abc.Callable
        service_account = 'muhammad402ali123@ee-afzal.iam.gserviceaccount.com'
        key = 'key.json'
        credentials = ee.ServiceAccountCredentials(service_account, key)
        ee.Initialize(credentials)
        p = ee.Geometry.Point([longitude,latitude])
        # start = '2022-01-01'
        # end = '2022-12-31'
        # imageCollection = ee.ImageCollection('MODIS/061/MOD09A1').filterDate(start, end).filterBounds(p)
        imageCollection = ee.ImageCollection('MODIS/061/MOD09A1').filterDate(start_date, end_date).filterBounds(p)
        im1 = imageCollection.sort('CLOUD_COVER', True).first()
        # Bands Values
        data_b1 = im1.select("sur_refl_b01").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b01")
        b1 = (data_b1.getInfo())
        data_b1 = im1.select("sur_refl_b02").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b02")
        b2 = (data_b1.getInfo())
        data_b1 = im1.select("sur_refl_b03").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b03")
        b3 = (data_b1.getInfo())
        data_b1 = im1.select("sur_refl_b04").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b04")
        b4 = (data_b1.getInfo())
        data_b1 = im1.select("sur_refl_b05").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b05")
        b5 = (data_b1.getInfo())
        data_b1 = im1.select("sur_refl_b06").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b06")
        b6 = (data_b1.getInfo())
        data_b1 = im1.select("sur_refl_b07").reduceRegion(ee.Reducer.mean(),p,10).get("sur_refl_b07")
        b7 = (data_b1.getInfo())
        ## Bands DN values
        Red = b1*0.0001
        NIR = b2*0.0001
        Blue = b3*0.0001
        Green = b4*0.0001
        SWIR1 = b5*0.0001
        SWIR2 = b6*0.0001
        SWIR3 = b7*0.0001
         #Vegetation Indices 
    
        ndvi = (NIR - Red)/(NIR + Red)
        dvi = (NIR - Red)
        evi  = 2.5 * ((NIR - Red) / (NIR + 6 * Red - 7.5 * Blue + 1))
        savi = ((NIR - Red) / (NIR + Red + 0.5)) * (1 + 0.5)
        osavi = (1 + 1.16) * ((NIR - Red) / (Red + NIR + 0.16))
        # Salinity Indices
        ndsi = (Red - NIR)/(Red + NIR)
        vssi = 2.5 * Green - 5 * (Red + NIR)
        si = (Red*Green)/Blue
        si1 = math.sqrt(Green*Red)
        si2 = math.sqrt(Red*NIR)
        si3 = math.sqrt((Green * Green) + (Red * Red) + (NIR * NIR))
        si4 = math.sqrt((Green * Green) + (Red * Red))
        si5 = (Blue / Red)
        salinity = model.predict([[Red,NIR,Blue,Green,SWIR1,SWIR2,SWIR3,ndvi,ndsi,vssi,si,si1,si2,si3,si4,si5]])
        texture = model1.predict([[Red,NIR,Blue,Green,SWIR1,SWIR2,SWIR3,ndvi,dvi,evi,savi]])
        Salinity = salinity.max()
        Texture = texture.max()
        if Texture == "building" or Texture == "water":
            return render_template("result1.html",Salinity = Salinity,Texture = Texture)
        else:
            return render_template("results.html",Salinity = Salinity,Texture = Texture)
    else:
        return render_template("test.html")

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
