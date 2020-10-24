

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
    
   

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    # Calculate the date 1 year ago from the last data point in the database

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

  

    return jsonify(lasy_year_prcp)
    

    
@app.route("/api/v1.0/stations")
def stations():
    return "test"

@app.route("/api/v1.0/tobs")
def tobs():
    return "test"

@app.route("/api/v1.0/<start>")
def api():
    return "test"

@app.route("/api/v1.0/<start>/<end>")
def end():
    return"test"



if __name__ == "__main__":
    app.run(debug=True)
