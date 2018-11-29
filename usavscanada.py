import csv
import matplotlib.pyplot as plt

categories = []
USA = []
Canada = []


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0


    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        else:
            if row[4] == "USA":
                print('total medals for USA:', len(USA))
                USA.append([int(row[0]), row[5], row[6], row[7]])
            elif row[4] == "CAN":
                print('total medals for Canada:', len(Canada))
                Canada.append([int(row[0]), row[5], row[6], row[7]])
                line_count += 1

totalMedals = len(USA) + len(Canada)

USA_procentage = int(len(USA) / totalMedals * 100)
Canada_procentage = int(len(Canada) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

labels = "USA", "Canada", 
sizes = [USA_procentage, Canada_procentage,]
colors = ['teal', 'deepskyblue']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=2)
plt.title("Canada VS USA")
plt.xlabel("Total Medal Procentage")
plt.show()
