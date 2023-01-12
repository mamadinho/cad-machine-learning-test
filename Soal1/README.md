# Faulty Chiller Pump Classifier

This program can be used to predict whether a chiller pump is indicated as faulty or not by using two temperatures and two vibration sensors. This app utilizes a simple web application served using Flask and a trained LightGBM model. 

## Model Training

![Temperature Plot](readme/degree.png?raw=true)
![Vibration Plot](readme/vibrate.png?raw=true)

After seeing from the plot above, we can see that the second pump (third and fourth image) has more separable data compared to the first pump (first and second image). Hence, these four variables are used for training. Also another calculated variable, called CHP2VibAvg and CHP2TempAvg is used to store the average of two sensors of the second pump. 

![Average Plot](readme/avg.png?raw=true)

A [LightGBM](https://lightgbm.readthedocs.io/en/v3.3.2/) model is used for the classification model as it is a very famous model right now for classification task and is lightweight compared to other gradient boosted models. The training process takes almost instantly in a free session google colab using CPU-only training. No hyperparameter tuning involved in this training. The dataset is split into a 80:20 for training and testing data.

## Model Performance

The model achieves 1.00 accuracy in the test dataset

## How to use the website

The website (flask project) can be easily run just by running the command `python app.py` and go into the url given in the terminal (usually http://127.0.0.1:5000) and enter the data on the forms. After pressing the button, the result will appear below the form.

## Suggestions

Maybe try to predict the future whether a pump may be faulty or not based on the previous data (like 15-30 seconds earlier) for early warning system, as this model does not consider the timestamp of the data.