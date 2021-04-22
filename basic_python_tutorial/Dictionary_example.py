'''list_examp = ["Robin van persie", "Nasri", "Arshavin"]

dict_player = {"striker" : "Robin van persie", "Left Wing" : "Arshavin", "Right Wing" : "Nasri"}

print(list_examp[2])
print(dict_player["Left Wing"])'''

player_dict = {"Striker-": "Robin Van Persie", "Left Wing-": "Arshavin", "Right Wing-": "Nasri"
               , "Attacking Mid-": "Fabregas", "Left DM-": "Alex Song", "Right DM-": "Jack Wilshere",
                "Left Back-" : "Clichy", "RCB-" : "Gallas", "LCB-" : "Djouru", "Right Back-" : "Sagna",
               "GK-" : "Almunia"}

'''for x in player_dict.keys():
    
    print(player_dict[x])'''

'''for x,y in player_dict.items():

    print(x,y)'''

player_dict.update({"sub-" : "Diaby"})

player_dict.pop("sub-")

player_dict.update({"subs -": ["Diaby", "Denilson", "Walcot", "Philipsendorous", "Fabianski"]})

for x,y in player_dict.items():

    print(x,y)
