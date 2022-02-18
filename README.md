# Python-Projects
 
## INTRODUCTION

Social media is one of the most attractive marketing platform nowadays. We are spending
more time on social media than ever which is estimated to be 15% of our waking lives.
Australians are spending one-third of the their online time on social media and over 1 in
3 users turn to social media to gather information about brands they are interested in.
Therefore, the advertisements need to be more relevant and interesting to the audience.
Many different factors are considered to adapt the advertisements for each and every user

## File contents

The input arguments are:
• inputFile is the name of the CSV file containing the information and record about
the location points which need to be analysed for this project. The first row of the
CSV file contains the following headers:
o LocId: The ID of a location point.
o Latitude: The latitude of location point.
o Longitude: the longitude of location point.
o Category: Location Types which can be of only one of the five types: Parking
(P), Hospital (H), Restaurant (R ), Chemist Shop (C) and Super Market (S).
• queryLocId is a location id for which we are analysing the record. This input argument
will accept a string.
• d1 and d2 are the input arguments that provide the dimension of rectangular boundary
around the input argument queryLocId. d1 will extend the rectangular region in the
East-West direction, whereas, d2 will extend the rectangular region in North-South
with respect to queryLocId. The rectangular region created by the parameters d1
and d2 will be considered as the search space. For example, if the latitude and
longitude of a location point L10 are given as (x,y), and the value of input parameters
are d1 and d2. In this case, the search space will create a rectangle region where the
coordinate of the North-East (NE), North-West (NW), South-West (SW), and SouthEast (SE) corners will be NE = (x+d1, y+d2), NW = (x-d1, y+d2), SW = (x-d1, y-d2),
SE = (x+d1, y-d2) respectively. Both of these input arguments (d1,d2) will be
numeric data


## Task

In this project we need to  read the data from a CSV (comma-separated values) file provided  and return different interesting
analytical results.
