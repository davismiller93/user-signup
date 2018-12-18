from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def DisplaySignup():
    return render_template('user_signup.html')

@app.route("/signup", methods= ['POST'])
def ValidateSignup():
    username = cgi.escape(
        request.form['username'])
    password = cgi.escape(
        request.form['password'])
    Confirmpassword = cgi.escape(
        request.form['verify'])
    email = cgi.escape(
        request.form['email'])

    usernamex = ""
    passwordx = ""
    Confirmpasswordx = ""
    emailx = ""

    if username == "":
        usernamex = "That's not a valid username"
    elif len(username) > 20 or len(username) < 3:
        usernamex = "That's not a valid username"

    if password == "":
        passwordx = "That's not a valid password"
    elif len(password) > 20 or len(password) < 3:
        passwordx = "That's not a valid password"
    
    if Confirmpassword == "":
        Confirmpasswordx = "The passwords don't match"
    elif not password == Confirmpassword:
        Confirmpasswordx = "The passwords don't match"

    if email == "":
        emailx = "That's not a valid email"
    elif email.count("@") < 1:
        emailx = "That's not a valid email"
    elif email.count(".") < 1:
        emailx = "That's not a valid email"
    elif email.count(" ") > 0:
        emailx = "That's not a valid email"
    elif len(email) > 30 or len(email) < 3:
        emailx = "That's not a valid email"
    
    if not usernamex and not passwordx and not Confirmpasswordx and not emailx:
        return redirect('/success?username= {0}'.format(username))
    else:
        return render_template('user_signup.html', 
            username= username, usernamex= usernamex, 
            passwordx= passwordx, Confirmpasswordx= Confirmpasswordx,
            email= email, emailx= emailx)

@app.route('/success')
def success():
    username = request.args.get('username')
    return render_template('success.html', username= username)

app.run()
