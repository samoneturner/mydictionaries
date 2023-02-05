"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries
"""

import json

infile = open("eq_data.json", "r")
earthq = json.load(infile)


# 1) print out the number of earthquakes

print(len(earthq["features"]))


# 2) iterate through the dictionary and extract the location, magnitude,
# longitude and latitude of the location and put it in a new
# dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
# magnitude > 6. Print out the new dictionary.


list_eq_dict = []

for e in earthq["features"]:
    if e["properties"]["mag"] > 6:
        info = {
            "Location": e["properties"]["place"],
            "Magnitude": e["properties"]["mag"],
            "Longitude": e["geometry"]["coordinates"][0],
            "Latitude": e["geometry"]["coordinates"][1],
        }

        list_eq_dict.append(info)
        eq_dict = dict({"earthquakes": list_eq_dict})


print(eq_dict)


"""
3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""

for e in eq_dict["earthquakes"][0:3]:
    print(
        f"Location: {e['Location']}",
        "\n",
        f"Magnitude: {e['Magnitude']}",
        "\n",
        f"Longitude: {e['Longitude']}",
        "\n",
        f"Latitude: {e['Latitude']}",
    )
    print()
