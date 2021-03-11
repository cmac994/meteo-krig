#!/usr/bin/env python
#Selection of functions used throughout this repository

#Import relevant python libraries
import os
from datetime import datetime,timedelta
from collections import defaultdict
import colorsys
import numpy as np

#Convert list of dates to list of datetime objects
def to_dt(dtlist,fmt):
	dts = [datetime.strptime(dt,fmt) for dt in dtlist]
	return dts

#Define function to subset netcdf file by bounding box
def subset(ds,minLat,maxLat,minLng,maxLng):
	ds = ds.where(ds.latitude<=maxLat,drop=True)
	ds = ds.where(ds.latitude>=minLat,drop=True)
	ds = ds.where(ds.longitude>=minLng,drop=True)
	ds = ds.where(ds.longitude<=maxLng,drop=True)
	return ds

#Define function to compute unix time from UTC time
def unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

#Retrieve list of dates between two dates
def date_list(start_date,end_date,step,format_str):

	#Get time and date-time at start/end dates of retrieval
	dt_start = datetime.strptime(start_date,format_str)
	dt_end = datetime.strptime(end_date,format_str)

	#Generate list of dates
	d00 = dt_start
	dt_list = []
	while (d00 <= dt_end):
		dt_list.append(d00.strftime(format_str))
		d00 += timedelta(0,step)

	return dt_list

R = 6371.
def haversine(lat1, lng1, lat2, lng2):
        """
        Use Haversine formula to estimate distances from all
        gridpoints to a given location (lat, lng)
        """

        lat1 = np.radians(lat1); lat2 = np.radians(lat2)
        lng1 = np.radians(lng1); lng2 = np.radians(lng2)

        R = 6371. # Radius of earth in km
        dlat = lat2 - lat1
        dlng = lng2 - lng1
        a = np.sin(dlat/2)**2 + np.cos(lat2) * np.cos(lat1) * \
                np.sin(dlng/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1.0-a))
        return R*c

def get_pos(brng,d,lon1,lat1):
        R = 6371.
        lat1 = np.radians(lat1) #Current lat point converted to radians
        lon1 = np.radians(lon1) #Current long point converted to radians

        lat2 = np.arcsin( np.sin(lat1)*np.cos(d/R) +
         np.cos(lat1)*np.sin(d/R)*np.cos(brng))

        lon2 = lon1 + np.arctan2(np.sin(brng)*np.sin(d/R)*np.cos(lat1),
                 np.cos(d/R)-np.sin(lat1)*np.sin(lat2))

        lat2 = np.degrees(lat2)
        lon2 = np.degrees(lon2)

        return lon2,lat2
