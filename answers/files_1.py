with open("data/iris.csv") as fin, open("data/iris.json", "w") as fout:
    reader = csv.DictReader(fin)
    data = [row for row in reader]
    json.dump(data, fout, indent=2)