import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/survey.csv')

col = df.columns

def getTally(name, column):

    tally = [0,0,0,0]
    for i in column:
        if i == "Strongly Agree":
            tally[0] += 1
        elif i == "Agree":
            tally[1] += 1
        elif i == "Disagree":
            tally[2] += 1
        elif i == "Strongly Disagree":
            tally[3] += 1
                   
    return tally, name

lbls = ["approachable", "engagingInHE", "knowledgeable", "answQs", "intrstInHelping"]

results = [0,0,0,0,0]
cnt = 0
for lbl in lbls:
    results[cnt], name = getTally(lbl, df[col[cnt]])
    cnt += 1

print(results)

plt.plot(results[1])
plt.show()


