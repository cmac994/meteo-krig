## meteo-krig

This repository provides code and example visualizations of techniques used in the methodology of McNicholas and Mass (2020; in Prep). 

Multi-resolution kriging (LatticeKrig; Nytcha, 2015) is used to generate 5-km gridded analyses of sea level pressure (altimeter), every 5-minutes. These analyses are generated using MADIS pressure observations. To account for the temporal variability of observation density/frequency of MADIS, Kalman smoothing is performed. Kalman smoothing transforms geo-spatial pressure analyses, generate with LatticeKrig (Nychka et al., 2015), into spatio-temporal pressure analyses that are consistent in both space and time. 

The code provided in this repository demonstrates this methodology, wherein pressure observations are analysed using LatticeKrig, smoothed using a Kalman Smoother, and band pass filtered to extract mesoscale pressure perturbations. In McNicholas and Mass (2020; in Prep) this approach to pressure analyses is extended from MADIS pressure observations to smartphone pressure observations.

### Setup

Please read the **SETUP.txt** file before attempting to run the jupyter notebooks provided in this repository. This file contains
instructinos for setting up an R/Python conda environment containing the packages used in jupyter notebooks. In addition, please download the data.tar.gz avaialble here: https://drive.google.com/file/d/1_fmKZLU2xQNMwt6SENJBL8bWs3OoSXic/view?usp=sharing. This archive contains MADIS pressure observations and analyses used in notebook examples.

### Notes about MADIS:
Additional observations, not available to the public, are provided to researchers under MADIS Research. In McNicholas and Mass (2020; in Prep) MADIS Research observations were used to generate pressure analyses. While the data archive contains pressure analyses generated with MADIS Research observations the raw data (i.e., point observations) are NOT provided. MADIS Research observations cannot be redistributed since they contain Mesonet observations prohibited from redistribution (https://madis.ncep.noaa.gov/madis_restrictions.shtml). For this reason, the data archive, and by extension kriging examples, are limited to MADIS pressure observations approved for public redistribution.

#### Notebooks

- *R_LatticeKrig_example.ipynb*
   - Demonstrates use of LatticeKrig R package for interpolating in situ pressure observations from MADIS to a 5-km grid.

- *LatticeKrig_Analysis.ipynb*
   - Visualization of LatticeKrig analyses produced in R_LatticeKrig_example.ipynb. Includes comparison between analysis generated
   using MADIS Research observations (used in paper) and publicly available MADIS observations (included in the repository)

- *LatticeKrig_Kalman_Smoothing.ipynb*
   - Shows how Kalman smoothing is used to transform 5-min pressure analyses, generated individually with LatticeKrig, into 
   spatio-temporal pressure analyses by smoothing windowed time-series at each grid point in the domain.
   Comparison to METAR observations is provided for a selection of three sites (one urban, one suburban, and one rural).
   Kalman Smoothing has a minimal impact on absolute accuracy, but greatly improves relative accuracy which is important for pressure perturbation analysis

- *LatticeKrig_KF_Analysis.ipynb*
   - Examples showing the end result of kriging and Kalman smoothing. 
      - Synoptic pressure analyses from 04/14/18 showing a low pressure system propagating across the Central U.S.
      - Pressure analyses and Composite Reflectivity from Derecho event in the Mid-Atlantic (05/15/18).
      - Pressure perturbation analysis from the Derecho event.

#### References:
Nychka, D., Bandyopadhyay, S., Hammerling, D., Lindgren, F. and Sain, S. (2015). A multiresolution Gaussian process model for the analysis of large spatial datasets. Journal of Computational and Graphical Statistics 24 579–599. https://doi.org/10.1080/10618600.2014.914946.
Nychka, D., Hammerling, D., Sain, S., Lenssen, N., 2016. Latticekrig: Multiresolution kriging based on markov random fields, R package version 8.4. https://github.com/NCAR/LatticeKrig.
