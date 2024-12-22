players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
result = []

ranking={name:rank for rank,name in enumerate(players)}

for i in callings : 
    overtake = ranking[i]
    overtaken = overtake-1

    players[overtaken], players[overtake] = players[overtake], players[overtaken]
    ranking[i] = overtaken
    ranking[players[overtake]] = overtake

