#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GPS tracking

Created by: Emir Rodzi
"""

from math import sin, cos, sqrt, atan2, radians, asin
import csv


def distance(p1, p2):
    """Calculate the distance between two points on a sphere given their longitudes and latitudes.

    Based on the haversine formula: https://en.wikipedia.org/wiki/Haversine_formula

    Args: p1, p2: tuples of (latitude, longitude) for the 'from' and 'to' points, respectively

    Latitude and longitude coordinates are represented as decimal numbers.
    The latitude is preceded by a minus sign (–) if it is south of the equator (a positive number implies north),
    and the longitude is preceded by a minus sign if it is west of the prime meridian (a positive number implies east).
    E.g.  p1 = (36.144698, -86.803177), p2 = (36.144871, -86.793150) -> distance: ~900m

    """

    # TODO: implement this helper function
    lat1, long1, lat2, long2 = map(radians, [p1[0], p1[1], p2[0], p2[1]])

    dlat = lat2 - lat1
    dlong = long2 - long1
    # conversion factor
    conv_fac = 0.621371
    R = 6371000
    miles = R / 1000 * conv_fac
    a = pow((sin(dlat / 2)), 2) + cos(p1[0]) * cos(p2[0]) * pow((sin(dlong / 2)), 2)
    A = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
    C = 2 * asin(sqrt(A))
    c = 2 * atan2(sqrt(A), sqrt(1 - A))

    return c * miles


def main():
    # TODO: open 'gpslog.csv' and iterate over the records

    with open('gpslog.csv') as gps_file:
        """Reads the files and process each line"""
        gps_records = csv.DictReader(gps_file)
        total_Dist = 0.0
        list_gps = []
        # Takes first line of the Excelbook
        first_gps = next(gps_records)
        point1 = (float(first_gps['Latitude']), float(first_gps['Longitude']))
        start_time = first_gps['Time']

        # Runs for-loop to run the 2nd line of the sheet
        for gps_record in gps_records:
            curr_time = gps_record['Time']
            lat1 = gps_record['Latitude']
            long1 = gps_record['Longitude']
            point2 = (float(lat1), float(long1))
            diff_time = (float(curr_time) - float(start_time)) / 3600
            result = distance(point1, point2)
            list_gps.append(result / diff_time)
            total_Dist += result
            point1 = point2
            start_time = curr_time

    print(list_gps)
    print('-' * 60)

    # TODO: calculate overall distance (sum of distances between consecutive points)
    # TODO: calculate max speed (maximum distance/time value between consecutive points)
    # TODO: calculate average speed (overall distance / time between last and first point)

    # TODO: print results in miles (one decimal precision) and mph (no decimals)
    print("Distance: ", round(total_Dist, 2), " miles")
    print("Average speed:", round((total_Dist / (float(start_time) / 3600))), " mph")
    print("Maximum speed: ", round(max(list_gps)), " mph")


if __name__ == '__main__':
    main()
