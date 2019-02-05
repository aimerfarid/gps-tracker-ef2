# GPS Vehicle Tracker (CSV file)

Implementing mathematical formulas in python through manipulating data from CSV files.

CSV file contains following data:
1. Time: the timestamp in fractional seconds of the GPS coordinate, where the trip starts at 0.0 s. (Consider all values incl. doubles)
2. Latitude: the geographic latitude in signed decimal degrees. The latitude is preceded by a minus sign (–) if it is south of the equator (a positive number implies north)
3. Longitude: the geographic longitude in signed decimal degrees. The longitude is preceded by a minus sign if it is west of the prime meridian (a positive number implies east).

Convert coordinate points with timestamps into three of the following data output in three respective columns:
1. Overall distance: the entire length of the trip (sum of distances between the measurement points). You should print this information in miles using one decimal place precision.
2. Average speed: the ratio of overall distance and overall time of the trip in miles per hour (mph) rounded to the closest integer.
3. Maximum speed: the maximum speed observed between consecutive GPS track points in miles per hour (mph) rounded to the closest integer.

Materials used for reference:
http://www.learner.org/jnorth/tm/LongitudeIntro.html

### P.s. Data are fictional values
