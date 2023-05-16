import os
from extract_classes import *
import csv
import random

mypath = os.getcwd() + "/course_stats"

listofstuff = [2.00, 2.30, 2.70, 3.00, 3.30, 3.70, 4.00]
listofcourses = extract_class_data()
for courses in listofcourses:
    with open(os.path.join(mypath, f"{courses}.csv"), "a") as file:
        writer = csv.writer(file)
        writer.writerow(["grade", "workload"])
        for i in range(0, 30):
            writer.writerow([listofstuff[random.randint(0, 6)], random.randint(4,10)])
