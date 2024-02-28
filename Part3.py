from flask import Flask, render_template, request, json
import webbrowser
from myPredict import*

app = Flask(__name__, static_folder="static")


@app.route('/get_proba', methods=['GET', 'POST'])
def get_len():
    region = request.form.get('region') # запрос к данным формы
    opf = request.form.get('opf')
    okved = request.form.get('okved')
    addOkved = request.form.get('addOkved')
    age = request.form.get('age')
    proba = func_predict(region, opf, okved, addOkved, age)  
    
    return json.dumps({'proba': proba})

  
@app.route('/predict', methods=['GET','POST'])
def predict():                
    return render_template('predict.html') 


if __name__ == "__main__":       
    webbrowser.open_new("http://127.0.0.1:5000/predict")
    app.run() 