from flask import Flask,render_template,redirect,request

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

db = SQLAlchemy(app)

class Name(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(200), nullable = False)
    lname = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return "NEW OBJECT ID: " + str(self.id)

@app.route("/")

def index():
    return render_template("index.html" )


@app.route("/set-data", methods = ['POST'])

def setData():
    firstname = request.form['fname']
    lastname = request.form['lname']

    new_name = Name(fname=firstname,lname=lastname)

    try:
        db.session.add(new_name)

        db.session.commit()
    except:
        return "NAME WAS NOT ADDED TO THE DB PROPERLY"

    names = Name.query.order_by(Name.date_created).all()

    
    return render_template("test.html", names = names)

if __name__ == '__main__':
    app.run(debug=True)
