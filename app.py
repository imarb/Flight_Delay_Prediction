import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load("Flight_Delay_Prediction.save")
ss = load("scale.save")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    fl_num = request.form['fl_num']
    origin_airport = request.form['origin_airport']
    if(origin_airport == "ATL"):
        oa_1, oa_2, oa_3, oa_4, oa_5 = 1, 0, 0, 0, 0
    if(origin_airport == "DTW"):
        oa_1, oa_2, oa_3, oa_4, oa_5 = 0, 1, 0, 0, 0
    if(origin_airport == "JFK"):
         oa_1, oa_2, oa_3, oa_4, oa_5 = 0, 0, 1, 0, 0
    if(origin_airport == "MSP"):
         oa_1, oa_2, oa_3, oa_4, oa_5 = 0, 0, 0, 1, 0  
    if(origin_airport == "SEA"):
         oa_1, oa_2, oa_3, oa_4, oa_5 = 0, 0, 0, 0, 1
    month = request.form['month']
    day_of_month = request.form['day_of_month']
    day_of_week = request.form['day_of_week']
    crs_dep_time = request.form['crs_dep_time']
    dep_time = request.form['dep_time']
    dest_airport = request.form['dest_airport']
    if(dest_airport == "ATL"):
        da_1, da_2, da_3, da_4, da_5 = 1, 0, 0, 0, 0
    if(dest_airport == "DTW"):
        da_1, da_2, da_3, da_4, da_5 = 0, 1, 0, 0, 0
    if(dest_airport == "JFK"):
         da_1, da_2, da_3, da_4, da_5 = 0, 0, 1, 0, 0
    if(dest_airport == "MSP"):
         da_1, da_2, da_3, da_4, da_5 = 0, 0, 0, 1, 0  
    if(dest_airport == "SEA"):
         da_1, da_2, da_3, da_4, da_5 = 0, 0, 0, 0, 1
    crs_arr_time = request.form['crs_arr_time']
    
    total = [[oa_1, oa_2, oa_3, oa_4, oa_5, da_1, da_2, da_3, da_4, da_5, month, day_of_month, day_of_week, fl_num, crs_dep_time, dep_time, crs_arr_time]]
    prediction = model.predict(ss.transform(total))
    
    if (prediction == 0):
        output = "The Flight will be on time"
    else:
        output = "The Flight will be delayed"
    
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
