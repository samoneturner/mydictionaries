# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


"""
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

"""

import csv


datastore = {
    "medical": [
        {"room-number": 100, "use": "reception", "sq-ft": 50, "price": 75},
        {"room-number": 101, "use": "waiting", "sq-ft": 250, "price": 75},
        {"room-number": 102, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 103, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 104, "use": "office", "sq-ft": 150, "price": 100},
    ]
}
"""
retail = open("retail_space.csv", "a")
retail_space = csv.reader(retail, delimiter=",")

for k, v in datastore.items():
    lines = ({k}, {v})
    retail_space.writelines(lines)

retail_space.close()

print(retail_space) 

"""
outfile = open("retail_space.csv", "w")

outfile.write("room-number,use,sq-ft,price\n")

list = datastore["medical"]

y = ""

for l in list:
    for x in l:
        y += x + ","
    rn = l["room-number"]
    use = l["use"]
    sq = l["sq-ft"]
    price = l["price"]

outfile.write(str(rn) + "," + use + "," + str(sq) + "," + str(price) + "\n")

outfile.close()

# alternatively (more efficient)
for l in list:
    for x in l:
        y += x + ","
    outfile.write(
        str(l["room-number"])
        + ","
        + l["use"]
        + ","
        + str(l["sq-ft"])
        + ","
        + str(l["price"])
        + "\n"
    )

outfile.close()
