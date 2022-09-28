from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
from pandas_profiling import ProfileReport 

app= Flask(__name__)

@app.route('/', methods=['POST','GET']) 
@cross_origin()

def report():
    df=pd.read_csv("data.csv")

    profile=ProfileReport(df)

    profile.to_file(output_file='housing.html')

    return render_template('housing.html')


if __name__ == "__main__":
	app.run(debug=True)

