import gamelogic

b = gamelogic.Bot()
i = b.choose_shot_random()
j = b.choose_shot_random()
s = {i,j}
print(b.options.issuperset(s))

