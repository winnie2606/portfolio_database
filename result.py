from flask import Flask
from flask import render_template
from flask import request
import csv
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/save',methods=['POST','GET'])
def save():
    if request.method == 'POST':
        user = request.form['User']
        password = request.form['Password']
        return user +','+password
app.run(debug=True)







