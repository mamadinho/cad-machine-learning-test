from flask import Flask, request, render_template
import pandas as pd
import joblib


# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        height = request.form.get("height")
        weight = request.form.get("weight")

        c2v1 = float(request.form.get("c2v1"))
        c2v2 = float(request.form.get("c2v2"))
        c2t1 = float(request.form.get("c2t1"))
        c2t2 = float(request.form.get("c2t2"))
        c2v_avg = (c2v1 + c2v2) / 2
        c2t_avg = (c2t1 + c2t2) / 2
        
        # Put inputs to dataframe
        X = pd.DataFrame([[c2v1, c2v2, c2t1, c2t2, c2v_avg, c2t_avg]])
        
        # Get prediction
        prediction = clf.predict(X)[0]
        
    else:
        prediction = ""
        
    return render_template("web.html", output = prediction)

# Running the app
if __name__ == '__main__':
    app.run(debug = True)