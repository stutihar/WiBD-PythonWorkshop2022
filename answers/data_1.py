import csv

arr = []
with open("data/wine.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        arr.append(int(row["Proline"]))

sns.distplot(arr)
plt.show()