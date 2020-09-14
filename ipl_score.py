import numpy as np
import pickle
from flask import Flask, render_template, request

model = pickle.load(open('cricket_score_prediction.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method=='POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array+ [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array+ [0,1,0,0,0,0,0,0]
        elif batting_team =='Kings XI Punjab':
            temp_array = temp_array+[0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array+[0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
        bowling_team = request.form['bowling-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array+ [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array+ [0,1,0,0,0,0,0,0]
        elif batting_team =='Kings XI Punjab':
            temp_array = temp_array+[0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array+[0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['overs'])
        runs =  int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5=int(request.form['wickets_in_prev_5'])
        
        temp_array = [overs,runs,wickets,runs_in_prev_5,wickets_in_prev_5]+temp_array
        data = np.array([temp_array])
        predictions = int(model.predict(data)[0])
        
        return render_template('result.html',lower_limit=predictions-10,upper_limit=predictions+5)
    
if __name__ == 'main':
    app.run(debug=True)
        
        
        

