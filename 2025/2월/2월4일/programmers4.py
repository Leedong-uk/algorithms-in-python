players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
dic = {}

for index,player in enumerate(players) :
    dic[player] = index


for i in callings : 
    overtake_index = dic[i] # kai의 index
    overtaken_index = overtake_index-1 #poe의 index

    overtake_value = i #kai
    overtaken_value = players[overtaken_index] #poe

    players[overtaken_index] = overtake_value
    players[overtake_index] = overtaken_value

    dic[overtake_value] = overtaken_index
    dic[overtaken_value] = overtake_index

print(players)

