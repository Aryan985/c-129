import csv
data1 = []
with open("dataset_1.csv","r")as f:
    reader = csv.reader(f)
    for i in reader:
        data1.append(i)    
headers1 = data1[0]
plinfo1 = data1[1:]

data2 = []
with open("dataset_sorted.csv","r")as f:
    reader = csv.reader(f)
    for i in reader:
        data2.append(i)    
headers2 = data2[0]
plinfo2 = data2[1:]

headers = headers1+headers2
plinfo = []
for i,v in enumerate(plinfo1):
    plinfo.append(plinfo1[i]+plinfo2[i])

with open("final.csv","a+")as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(plinfo)