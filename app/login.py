from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for


app = Flask(__name__)

@app.route('/')

def html():
	return render_template('login2.html')

@app.route('/checkPerson', methods=['POST'])
def checkPerson():
	idPass = dict(request.form.items())
	getID = idPass.get('id', None)
	if getID[0:5] == '59340':
		who = 'student'
	else:
		who = 'teacherofficer'
	person = str(who) + '.html'
	return redirect(url_for('static', filename=person))

app.run(debug=True)

#PopTest