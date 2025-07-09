from flask import Flask, render_template, request, redirect 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/upload', method=['POST'])
def file():
    pass

if __name__ =='__main__':
    app.run(debug=True)

