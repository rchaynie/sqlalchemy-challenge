

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import pandas as pd

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Base.classes.keys()

# Save references to each table

measurement=Base.classes.measurement

station=Base.classes.station




#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def home(): 
    """ The following routes are available  """
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>")

 # Design a query to retrieve the last 12 months of precipitation data and plot the results
# Calculate the date 1 year ago from the last data point in the database
   

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)



    max_date=session.query(func.max(measurement.date)).all()[0]
    
    
    one_year = dt.timedelta(days=365)

    min_date = dt.date(2017, 8, 23) - one_year

    min_date

    # Perform a query to retrieve the data and precipitation scores

    lasy_year_prcp=session.query(measurement.date, measurement.prcp).filter(measurement.date >= min_date).all()

    session.close()

    # Save the query results as a Pandas DataFrame and set the index to the date column

    # prcp_df=pd.DataFrame(lasy_year_prcp)
    # prcp_df=prcp_df.set_index("date").sort_values("date")
    # prcp_df

    # results = dict.fromkeys( {
    #     "date": lasy_year_prcp['date'],
    #     "precip" : lasy_year_prcp['prcp']
    # } )
  

    return jsonify(lasy_year_prcp)


# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.

    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    results_stations=session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    
    stations_all = (row for row in results_stations)
    
    session.close()

    return jsonify(results_stations)


# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature of the most active station?

@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)
    # data=session.query(func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station == 'USC00519281').all()
    
    

    temps = {
        "max_temp_from_station_USC00519281" : session.query(func.max(measurement.tobs)).filter(measurement.station == 'USC00519281').first(),
        "min_temp_from_station_USC00519281" : session.query(func.min(measurement.tobs)).filter(measurement.station == 'USC00519281').first(),
        "mean_temp_from_station_USC00519281" : session.query(func.avg(measurement.tobs)).filter(measurement.station == 'USC00519281').first()
    }

    session.close()

    return jsonify(temps)


# bonus portion

@app.route("/api/v1.0/<start>")
def api():
    return "test"

@app.route("/api/v1.0/<start>/<end>")
def end():
    return"test"



if __name__ == "__main__":
    app.run(debug=True)
