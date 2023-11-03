from flask import Flask, render_template, request, redirect, url_for 
from contextlib import contextmanager
from flask import template_rendered
from concurrent.futures import ThreadPoolExecutor
import webbrowser
from myPredict import*

app = Flask(__name__, static_folder="static")
  
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':            
        region = request.form.get('region')
        opf = request.form.get('opf')
        okved = request.form.get('okved')
        addOkved = request.form.get('addOkved')
        age = request.form.get('age')
        pr = func_predict(region, opf, okved, addOkved, age)      
        print(pr)  
        
        return render_template('predict.html') 
    else:
        return render_template('predict.html')

if __name__ == "__main__":       
    webbrowser.open_new("http://127.0.0.1:5000/predict")
    app.run() 