# meteo-krig


<img width="1680" height="280" src="Plots/20180515/kfanl_caseI.gif">

This repository provides code and example visualizations of techniques used in the methodology of McNicholas and Mass (2020). 

Multi-resolution kriging (LatticeKrig; Nychka et al., 2015) is used to generate 5-km gridded analyses of sea level pressure (altimeter), every 5-minutes. These analyses are generated using [MADIS](https://madis.ncep.noaa.gov/madis_sfc.shtml) pressure observations, which include pressure observations from [METARs](https://madis.ncep.noaa.gov/madis_metar.shtml) and [Mesonets](https://madis.ncep.noaa.gov/madis_mesonet.shtml). To account for the temporal variability of MADIS observation density/frequency, Kalman smoothing is performed. Kalman smoothing transforms geo-spatial pressure analyses, generated with LatticeKrig, into spatio-temporal pressure analyses that are consistent in both space and time. 

The code provided in this repository demonstrates this methodology, wherein pressure observations are analysed using LatticeKrig, smoothed using a Kalman Smoother, and band pass filtered to extract mesoscale pressure perturbations. In McNicholas and Mass (2020) this approach to pressure analyses is extended from MADIS pressure observations to smartphone pressure observations.

### Setup

Please read the **SETUP.txt** file before attempting to run the jupyter notebooks provided in this repository. This file contains
instructions for setting up an R/Python conda environment containing the packages used in jupyter notebooks. In addition, please download the data.tar.gz available [here](https://drive.google.com/file/d/1q418t9YtHSTO01FbQH-eCprvaReaf2XU/view?usp=sharing). This archive contains MADIS pressure and radar analyses used in jupyter notebook examples.

### Notes about MADIS:
Additional observations, not available to the public, are provided to researchers by the Meteorological Data Assimilation Ingest System ([MADIS](https://madis.ncep.noaa.gov/)). In McNicholas and Mass (2020), MADIS Research observations were used to generate pressure analyses. The data archive contains pressure analyses generated with MADIS Research observations but not the raw data (i.e., point observations). MADIS Research observations cannot be redistributed since they contain Mesonet observations [prohibited](https://madis.ncep.noaa.gov/madis_restrictions.shtml) from redistribution. For this reason, point-observations in the data archive are limited to MADIS pressure observations approved for public release.

#### Notebooks

- *R_LatticeKrig_example.ipynb*
   - Demonstrates the use of the LatticeKrig R package for interpolating *in situ* pressure observations from MADIS onto a 5-km regular grid.

- *LatticeKrig_Analysis.ipynb*
   - Visualization of LatticeKrig analyses produced in R_LatticeKrig_example.ipynb. Includes comparison between analysis generated
   using MADIS Research observations and publicly available MADIS observations

- *LatticeKrig_Kalman_Smoothing.ipynb*
   - Shows how Kalman smoothing is used to transform 5-min pressure analyses, generated individually with LatticeKrig, into 
   spatio-temporal pressure analyses by smoothing windowed time-series at each grid point in the domain.
   A comparison to METAR observations is provided at three sites (one urban, one suburban, and one rural).
   Kalman Smoothing has a minimal impact on absolute accuracy, but greatly improves relative accuracy which is important for pressure perturbation analysis

- *LatticeKrig_KF_Analysis.ipynb*
   - Examples showing the end result of kriging and Kalman smoothing. 
      - Synoptic pressure analyses from 04/14/18 showing a low pressure system propagating across the Central U.S.
      - Pressure analyses and composite Reflectivity from Derecho event in the Mid-Atlantic (05/15/18).
      - Pressure perturbation analysis from the Derecho event.

#### References:
McNicholas, C., C. Mass, 2020: Bias Correction, Anonymization, and Analysis of Smartphone Pressure Observations with Machine Learning and Multi-Resolution Kriging. *Journal of Weather and Forecasting*, (submitted).

Nychka, D., Bandyopadhyay, S., Hammerling, D., Lindgren, F. and Sain, S. (2015). A multiresolution Gaussian process model for the analysis of large spatial datasets. *Journal of Computational and Graphical Statistics* 24 579–599. https://doi.org/10.1080/10618600.2014.914946.

Nychka, D., Hammerling, D., Sain, S., Lenssen, N., 2016. Latticekrig: Multiresolution kriging based on markov random fields, R package version 8.4. https://github.com/NCAR/LatticeKrig.
