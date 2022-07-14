squares = { x : x ** 2 for x in range(1,11)}
print(squares)

players = {
    'sachin' : {290,350,460,401,380},
    'rahul' : {230,410,185,275,370},
    'sehwag' : {340,430,485,390,350},
    'sourav' : {140,190,385,430,320},
    'yuvraj' : {160,230,380,120,185},
}
print(players)

print("-" *  40)

print(sum(players['sachin']))

print("-" *  40)

scores = {k: sum(v) for k, v in players.items()}
print(scores)

print("-" *  40)

scores  = {k: (lambda scores: sum(scores) / len(scores))(v) for k, v in players.items()}
print(scores)

print("*" *  40)

def avgScores():

        return  {k: (lambda scores: sum(scores) / len(scores))(v) for k, v in players.items()}

print(avgScores())

print("*" *  40)


def avgScores(score):
    sum(score) / len(score)
scores =  {k: avgScores(v) for k, v in players.items()}


print((scores))


"""basic = [{x: (lambda par: "Mr." + par)("sachin {}".formate(x))}
for x in range(1,6)]
print(basic)
"""

print("**" *  40)

players = {
    'sachin' : [290,350,460,401,380],
    'rahul' : [230,410,185,275,370],
    'sehwag' : [340,430,485,390,350],
    'sourav' : [140,190,385,430,320],
    'yuvraj' : [160,230,380,120,185],
}
pl1 = [pl1_score for pl1_score in players]
print(pl1)

pl2 = [pl2_score for pl2_score in players.values()]
print(pl2)
print("**" *  40)

pl1 = [x for pl1_score in players.values() for x in pl1_score]
print(pl1)

pl1 = [x for pl1_score in players.values() for x in pl1_score if x > 200]
print(pl1)

print("**" *  40)

runs200 = {name: [scr for scr in score if scr > 250 ]
           for name,score in players.items()}
print(runs200)

print("**" *  40)
l = [1,2,3,4,5,6]
itrObj = l.__iter__()
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())

print("**" *  40)

for i in l:
    print(i)







