
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pprint import pprint

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, Column, Integer, String, Float
from sqlalchemy.types import Date
import datetime as dt

from pprint import pprint
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found

Base.classes.keys()

# Save references to each table

measurement=Base.classes.measurement

station=Base.classes.station

# Design a query to retrieve the last 12 months of precipitation data and plot the results
# Calculate the date 1 year ago from the last data point in the database

max_date=session.query(func.max(measurement.date)).all()[0]
for row in max_date:
    pprint(row)
    
one_year = dt.timedelta(days=365)

min_date = dt.date(2017, 8, 23) - one_year

min_date

# Perform a query to retrieve the data and precipitation scores

lasy_year_prcp=session.query(measurement.date, measurement.prcp).filter(measurement.date >= min_date).all()

# Save the query results as a Pandas DataFrame and set the index to the date column

prcp_df=pd.DataFrame(lasy_year_prcp)
prcp_df=prcp_df.set_index("date").sort_values("date")
prcp_df
# Sort the dataframe by date

# Use Pandas Plotting with Matplotlib to plot the data
prcp_df.plot(rot=90, figsize=(10,5))
plt.ylabel("inches")
plt.xlabel("date")
plt.show()

# Use Pandas to calcualte the summary statistics for the precipitation data
prcp_df.describe()

# Design a query to show how many stations are available in this dataset?
session.query(func.count(station.station)).all()[0]


# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.

results_stations=session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
for row in results_stations:
    print(row)


# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature of the most active station?

# Select max(temp), min(temp), avg(temp) from measurement_df WHERE station == USC00519281

'SELECT max(tobs), min(tobs), avg(tobs) FROM measurement WHERE station == USC00519281'

data=session.query(func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station == 'USC00519281').all()
data


# Choose the station with the highest number of temperature observations.

# Query the last 12 months of temperature observation data for this station and plot the results as a histogram

temp_data = session.query((measurement.tobs)).filter(measurement.station == 'USC00519281').filter(measurement.date >= min_date).all()

temp_data=pd.DataFrame(temp_data)

temp_data.plot.hist(bins=12)