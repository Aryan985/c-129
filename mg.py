import csv
data = []
with open("dataset_2.csv","r")as f:
    reader = csv.reader(f)
    for i in reader:
        data.append(i)    
headers = data[0]
plinfo = data[1:]
for i in plinfo:
    i[2] = i[2].upper()

plinfo.sort(key = lambda plinfo:plinfo[2])

with open("dataset_sorted.csv","a+")as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(plinfo)