import random 
import plotly.express as px
import plotly.figure_factory as ff 


count =[]
result = []

for i in range(1,101):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)
    count.append(i)

fig= ff.create_distplot([result],['Label'])
fig.show()


