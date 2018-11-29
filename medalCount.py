import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0


    for row in reader:
        if line_count is 0:
            print('stripping out categories')
            categories.append(row)
            line_count += 1

        else:
            if row[7] == "Gold":
                print('gold')
                golds.append(row[7])
            elif row[7] == "Silver":
                print('silver')
                silvers.append(row[7])
            elif row[7] == "Bronze":
                bronzes.append(row[7])
            line_count += 1

print(len(golds), 'gold medals wire won since \'24')
print(len(silvers), 'silver medals have been won since \'28')
print(len(bronzes), 'bronze medals have been won since \'28')

totalMedals = len(golds) + len(silvers) + len(bronzes)

# procentege of all medals
gold_procentage = int(len(golds) / totalMedals * 100)
silver_procentage = int(len(silvers) / totalMedals * 100)
bronze_procentage = int(len(bronzes) / totalMedals * 100) 

print(gold_procentage, silver_procentage, bronze_procentage)

print('procedded', line_count, 'lines of data. Total medals:', totalMedals )
 
 #do the pie chart


labels = "Gold", "Silver", "Bronze"
sizes = [gold_procentage, silver_procentage, bronze_procentage]
colors = ['yellowgreen', 'lightgreen', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title(" Medal Number")
plt.xlabel("Medal Count since 1924")
plt.show()

