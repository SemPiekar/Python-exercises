from itertools import count

from Opdrachten.Uitwerkingen.Les4_Source1 import index_of_heartstone

games = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
         "Fortnite Battle Royale 39 Million 2017",
         "Apex Legends 50 Million (1 Month) 2019",
         "Leauge of Legends (LOL) 27 Million 2009",
         "Counter Strike; Global Offensive 32 Million 2014",
         "Heartstone 29 Million 20120",
         "Minecraft 91 Million 2011",
         "DOTA 2 5 million 2015",
         "The Division 2 N/A 2019",
         "The Splatoon 2"]

print(games)
print(f"5] {games[4]} \n")

print(games)
print(f"The game {games[7]} has {len(games[7])} characters \n")

print(games)
print(f"There are {len(games)} games in the list \n")

index_of_splatoon = games[9]
del(games[9])
print(games)
print(f"Unfortunately, the game {index_of_splatoon} did not manage to stay in the top 10. We bid a worthy farewell to {index_of_splatoon}.\n")

index_of_heartstone = games.index("Heartstone 29 Million 20120")
games[index_of_heartstone] = "Heartstone 29 Million 2012"
print(games)
