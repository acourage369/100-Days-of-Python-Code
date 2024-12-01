people = {
    "kofi": "tiles",
    "airly": "afcons",
    "brainy": "coding"
}
# print(people["kofi"])
# people["loop"] = "gffgxhfyuhtgbghgyh"
# print(people)
#
# empty_dictionary = {}
#
# people["kofi"] = "i love u"
# print(people)

for key in people:
    print(key)
    # print(people[key])







# nesting
capital = {
    "france": "paris",
    "germani": "berlin"
}

# nesting a list in a dict
travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["berlin", "hamburg", "stuttgart"]
}

# nesting a dictionary a dictionary
travel_log= [
    {"country": "france",
     "cities_visited": ["paris", "lille", "dijon"],
     "total_visits": 12
     },
    {"country": "germany",
     "cities_visited": ["berlin", "hamburg", "stuttgart"],
     "total_visits": 5
     }
]

# nesting a dictionary a list
