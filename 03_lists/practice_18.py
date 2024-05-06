players = ["mohamed","sara","aly","mahmoud","ahmed"]
top_player = players.pop(0)
loser = players.pop()
winners = players[0:4]

print(f"Top player {top_player} .. Congrats")
print(f"try again next time {loser}")
print (f"{winners} you passed this level")