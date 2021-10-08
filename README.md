# meteo-krig

<img width="1680" height="320" src="Plots/Analysis/pressure_tracks.gif">

This repository provides code and example visualizations of techniques and results from [McNicholas and Mass (2021a)](https://doi.org/10.1175/WAF-D-20-0222.1) and McNicholas and Mass (2021b; submitted). 

In [McNicholas and Mass (2021a)](https://doi.org/10.1175/WAF-D-20-0222.1) multi-resolution kriging (LatticeKrig; Nychka et al., 2015) is used to generate 5-km gridded analyses of sea level pressure (altimeter), every 5-minutes. These analyses are generated using [MADIS](https://madis.ncep.noaa.gov/madis_sfc.shtml) pressure observations, which include pressure observations from [METARs](https://madis.ncep.noaa.gov/madis_metar.shtml) and [Mesonets](https://madis.ncep.noaa.gov/madis_mesonet.shtml). To account for the temporal variability of MADIS observation density/frequency, Kalman smoothing is performed. Kalman smoothing transforms geo-spatial pressure analyses, generated with LatticeKrig, into spatio-temporal pressure analyses that are consistent in both space and time. 

The code provided in this repository demonstrates this methodology, wherein pressure observations are analysed using LatticeKrig, smoothed using a Kalman Smoother, and band pass filtered to extract mesoscale pressure perturbations. In [McNicholas and Mass (2021a)](https://doi.org/10.1175/WAF-D-20-0222.1) this approach to pressure analyses is utilized for both MADIS and smartphone pressure observations. In McNicholas and Mass (2021b; submitted), this methodology is extended to MADIS temperature, moisture, and wind observations facilliting the analysis, tracking, and comparison of a climatology of mesoscale pressure features observed with smartphones and conventional (MADIS) observations.

### Setup
Please read the **SETUP.txt** file before attempting to run the jupyter notebooks provided in this repository. This file contains
instructions for setting up an R/Python conda environment containing the packages used in jupyter notebooks. In addition, please download the data.tar.gz available [here](https://drive.google.com/file/d/1q418t9YtHSTO01FbQH-eCprvaReaf2XU/view?usp=sharing). This archive contains data and analyses used in jupyter notebook examples.

### Notes about MADIS:
Additional observations, not available to the public, are provided to researchers by the Meteorological Data Assimilation Ingest System ([MADIS](https://madis.ncep.noaa.gov/)). In McNicholas and Mass (2021a; 2021b), MADIS Research observations were used to generate pressure analyses. The data archive contains pressure analyses generated with MADIS Research observations but not the raw data (i.e., point observations). MADIS Research observations cannot be redistributed since they contain Mesonet observations [prohibited](https://madis.ncep.noaa.gov/madis_restrictions.shtml) from redistribution. For this reason, point-observations in the data archive are limited to MADIS pressure observations approved for public release.

#### [Notebooks](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/)

- [*Methodology*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/Methodology)

   #### *Paper I: McNicholas and Mass (2021a)*

   - [*Surface Analysis*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/Methodology/SurfaceAnalysis/)
      - [Kriging](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/Methodology/SurfaceAnalysis/Kriging/)   
         - Demonstrates the use of the LatticeKrig R package for interpolating *in situ* surface observations from MADIS onto a 5-km regular grid.

      - [RTS_Analysis](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/Methodology/SurfaceAnalysis/RTS_Analysis/)
         - Shows how Kalman smoothing is used to transform 5-min pressure analyses, generated individually with LatticeKrig, into 
         spatio-temporal pressure analyses by smoothing windowed time-series at each grid point in the domain.
         A comparison to METAR observations is provided at three sites (one urban, one suburban, and one rural).
         Kalman Smoothing has a minimal impact on absolute accuracy, but greatly improves relative accuracy which is important for pressure perturbation analysis
         - Provides examples for pressure, temperature, moisture, and wind which show the end result of kriging and Kalman smoothing. A comparison between surface analyses   
         generated using MADIS Research observations and publicly available MADIS observations is also performed.

      - [*SurfaceAnalysis.ipynb*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/blob/master/notebooks/Methodology/SurfaceAnalysis/Surface_Analysis.ipynb)
         -  Combines smarpthone pressure analyses with composite reflectivity and MADIS analyses of temperature, mositure, and wind to create gridded objective analyses.
         -  Demonstrates how mesoscale temperature, moisture, and wind perturbations are extracted from MADIS analyses using band-pass filtering. 
         -  Produces animations depicting the evolution of mesoscale perturbations associated with two high-impact weather events in the Mid-Atlantic region between 14-15 May 2018.

   - [*Feature Tracking*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/Methodology/Feature_Tracking/)
      - [*Pressure_Perturbation_Analysis.ipynb*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/blob/master/notebooks/Methodology/Feature_Tracking/Pressure_Perturbation_Analysis.ipynb)
         - Reveals how mesoscale pressure perturbations are extracted from smartphone pressure analyses using band-pass filtering. Composite reflectivity is shown beside 
         altimeter analysis and band-pass filtered (mesoscale) pressure perturbations to show how smartphone analyses captured convective phenomena during the 14-15 May derecho 
         event.

      - [*Perturbation_Tracking.ipynb*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/blob/master/notebooks/Methodology/Feature_Tracking/Perturbation_Tracking.ipynb)   
         - Perform feature tracking of mesoscale pressure perturbations using [scikit-image](https://github.com/scikit-image/scikit-image), [hagelsag]
         (https://github.com/djgagne/hagelslag), and [trackpy](https://github.com/soft-matter/trackpy).
         - Illustrates feature tracking by animating feature tracks overlaid atop mesoscale pressure perturbations during the 14-15 May derecho event.
        
   #### *Paper II: McNicholas and Mass (2021b)*
   
   - [*Analysis*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/FeatureTracking/)
      - [*Bandpass_Filtering.ipynb*](https://nbviewer.org/github/cmac994/meteo-krig/blob/master/notebooks/Methodology/Analysis/Bandpass_Filtering.ipynb)
         - Utilizes a case-study of a squall line in May 2018, from McNicholas and Mass (2021b), to demonstrate the creation of surface analyses and mesoscale perturbation analyses using smartphone and MADIS observations. Pressure feature identification and tracking is also examplified for the squall line case. A comparison is made between the mesoscale pressure feature observed by smartphones and MADIS
      - [*Composite_Analysis.ipynb*](https://nbviewer.org/github/cmac994/meteo-krig/blob/master/notebooks/Methodology/Analysis/Composite_Analysis.ipynb)   
         - The compositing of a mesoscale pressure feature is demonstrated for the squall-line case of McNicholas and Mass (2021b). Cross-correlation lag-analysis and beamsteering techniques are examined to estimate the phase propagation of pressure features and to calculate the feature normal wind ([Nappo, 2013](https://ebookcentral.proquest.com/lib/washington/detail.action?docID=1042788)). Lastly, cross-spectral analysis is performed to estimate to examine the relationship between perturbation pressure and feature normal wind. 

#### *Paper II: McNicholas and Mass (2021b)*  

- [*Results*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/tree/master/notebooks/CaseStudies/)
  
   - [*Feature Climatology*](https://nbviewer.org/github/cmac994/meteo-krig/blob/master/notebooks/Results/FeatureClimatology.ipynb)
      - A comparison between smartphone and madis pressure feature climatologies is explored through stastical analysis of a 1-year pressure feature climatology spanning the central and eastern U.S.
      - The seasonal, diurnal, and geographic variation of surface pressure features is examined. Furthermore, their environment (with respect to precipitation/convection) and (phase and propagation) velocity is examined. 

   - [*Composite and Wavelet Analysis*](https://nbviewer.jupyter.org/github/cmac994/meteo-krig/blob/master/notebooks/CaseStudies/CaseI/CaseI_MCS_Composite_and_Wavelet_Analysis.ipynb)
      - An analysis of the temporal and spatial composites of smartphone pressure features is performed for both positive and negative features.
      - Phase relationships between mesoscale surface pressure perturbations and other surface variables (e.g. temperature, dew point, wind) are examined.

#### References:

McNicholas, C., & Mass, C. F. (2021a). Bias Correction, Anonymization, and Analysis of Smartphone Pressure Observations Using Machine Learning and Multiresolution Kriging, Weather and Forecasting, 36(5), 1867-1889. Retrieved Oct 8, 2021, doi: https://doi.org/10.1175/WAF-D-20-0222.1

McNicholas, C., & Mass, C. F. (2021b): A Comparison of Mesoscale Pressure Features Observed with Smartphones and Conventional Observations. *Journal of Weather and Forecasting*, (submitted).

Nappo, C. J. 2013: An Introduction to Atmospheric Gravity Waves: Introduction to Atmospheric Gravity Waves, Elsevier Science & Technology, 2012. ProQuest Ebook Central, https://ebookcentral.proquest.com/lib/washington/detail.action?docID=1042788

Nychka, D., Bandyopadhyay, S., Hammerling, D., Lindgren, F. and Sain, S. (2015). A multiresolution Gaussian process model for the analysis of large spatial datasets. *Journal of Computational and Graphical Statistics* 24 579–599. https://doi.org/10.1080/10618600.2014.914946.

Nychka, D., Hammerling, D., Sain, S., Lenssen, N., 2016. Latticekrig: Multiresolution kriging based on markov random fields, R package version 8.4. https://github.com/NCAR/LatticeKrig.
