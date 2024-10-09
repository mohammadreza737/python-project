import csv
from statistics import mean
with open (r"grad.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
       
    
        mylist = list()
        for grade in row[1:]:
            mylist.append(int(grade))
            
        print('the toatal of %s is %f'%(name,mean(mylist)))



    