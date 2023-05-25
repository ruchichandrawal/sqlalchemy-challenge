# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
             
            f"Available Routes:<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/start<br/>"
            f"/api/v1.0/start/end"
        
    )
# define precipitation method
 #route("/api/v1.0/prec
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    # get precipitation data
    precipitaion_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_prev_year()).all()          
    session.close()

    # create list
    precipitaion_list = []
    for date, prcp in precipitaion_data:
        precipitaion_dict = {}
        precipitaion_dict["date"] = date
        precipitaion_dict["prcp"] = prcp
        precipitaion_list.append(precipitaion_dict)

    # Return a list of jsonified precipitation data for the previous 12 months 
    return jsonify(precipitaion_list)
        

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # get station data
    station_data = session.query(Station.station).all()
                 
    session.close()

    
    station_list = list(np.ravel(station_data))

    # return json data
    return jsonify(station_list)

        
@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)

    # get tobs data 
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= date_prev_year()).all()

                   
    session.close()

   
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    # return json data
    return jsonify(tobs_list)

   
if __name__ == '__main__':
    app.run(debug=True) 



