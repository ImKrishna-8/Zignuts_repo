import csv
with open("sample_data.csv") as f:
    data = csv.reader(f)
    for line in data:
        print(line)