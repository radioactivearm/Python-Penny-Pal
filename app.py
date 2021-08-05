# Andy McRae
# Flask Server

#======================
# Import the functions
from flask import Flask
from flask import render_template
from flask import jsonify

# get connection variables
from config import password, username, localhost, port


# Import the functions from sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
#=====================================

db = 'expenses'
conn_str = f'postgresql://{username}:{password}@{localhost}:{port}/{db}'

# Connecting to database
engine = create_engine(conn_str)
base = automap_base()
base.prepare(engine, reflect=True)

grocery = base.classes.grocery

# Start the Flask app
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # disables page caching

@app.route("/")
def IndexRoute():
    return render_template("index.html")

@app.route('/grocery')
def groceryRoute():

    session = Session(engine)
    query = session.query(grocery.date, grocery.amount, grocery.location).all()
    session.close()

    grocery_list = []
    for date, amount, location in query:
        dic = {}
        dic['date'] = date
        dic['amount'] = amount
        dic['location'] = location
        grocery_list.append(dic)

    return jsonify(grocery_list)

if __name__ == '__main__':
    app.run(debug=True)