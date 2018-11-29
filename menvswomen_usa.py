import csv
import numpy as numpy
import matplotlib.pyplot as plt

categories = []
USA = []
world = []



with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        elif row[4] == "USA":
            USA.append([int(row[0]), row[5], row[6], row[7]])

         

    

gold_medals = []




for medal in USA:
    if medal[0] ==  medal[3] =="Gold":
        gold_medals.append(medal)



men = []
women = []

for medal in USA:
    if medal[1] == "Men":
       men.append(medal)

for medal in USA:
    if medal[1] == "Women":
       women.append(medal)


print('men won', len(men), 'gold medals ')
print('women won', len(women), 'gold medals ')

totalMedals = len(men) + len(women)

men_procentage = int(len(men) / totalMedals * 100)
women_procentage = int(len(women) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

labels = "Men", "Women", 
sizes = [men_procentage, women_procentage,]
colors = ['dodgerblue', 'lightpink']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title(" USA GOLD Medal wins")
plt.xlabel(" Total Medal Count men vs women")
plt.show()
