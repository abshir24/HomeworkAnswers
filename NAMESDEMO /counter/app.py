from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'sec'


@app.route('/')

def index():
    if "counter" not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1

    counter = session['counter']

    return render_template("index.html",counter = counter)


@app.route('/addtwo')

def addTwo():
    if "counter" not in session:
    
        session['counter'] += 2

    counter = session['counter']

    return render_template("index.html",counter = counter)

@app.route("/reset")

def reset():
    session['counter'] = 0

    counter = session['counter']

    return render_template("index.html",counter = counter)

app.run(debug = True)