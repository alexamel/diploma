# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from models import User
import diploma

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
    	login = request.form['login']
	password = request.form['password']

	try:
	    u = User.get(login=login, password=password)
	except:
	    return render_template("message.html", message=u"Неправильный логин или пароль")
	return render_template("message.html", message=u"Авторизация прошла успешно")
    else:
        wsdl = diploma.web_generate()
        return render_template('login.html', wsdl=wsdl)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
	f = request.files['file']
	f.save('uploads/elements.csv')
	return redirect(url_for('auth'))
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
