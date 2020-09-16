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
