def getTotalPopulation(cities):
    t = 0
    for i in range(len(cities)):
        t = t+cities[i][2]
    return t
cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]
print(getTotalPopulation(cities))                   
