distances_from_sofia = [
    ('Bansko', 97),
    ('Brussels', 1701),
    ('Alexandria', 1403),
    ('Nice', 1307),
    ('Szeged', 469),
    ('Dublin', 2479),
    ('Palermo', 987),
    ('Oslo', 2098),
    ('Moscow', 1779),
    ('Madrid', 2259),
    ('London', 2019)
]

# variable to store the filtered list of distance tuples:
selected_distances = []

# filter each distance tuple:
for item in distances_from_sofia:
    # each item is a tuple, and we check its second value:
    if(item[1] < 1500):
        selected_distances.append(item)

# print the filtered list of distance tuples:
print("Distances bellow 1500 km from Sofia are:")
for item in selected_distances:
    print("{} - {}".format(item[0], item[1]))
