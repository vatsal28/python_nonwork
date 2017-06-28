import random
import pandas
import os
import csv

website_name = str(input("Enter the website/app name: "))
os.chdir('C:\\Users\\Vatsal\\Desktop')  

list_1 = []
list_2 = []

for i in range(1,4):
	{
		list_1.append(chr(random.randrange(97,122,1)))

	}

for i in range(1,9):
	{
		list_2.append(chr(random.randrange(97,122,1)))	
	}


list_11 = ''.join(list_1)
list_22 = ''.join(list_2)
as_string = (list_11)+"_"+(list_22) 
print((list_11))
print((list_22))
list_3 = [website_name,as_string]
print(list_3)
with open('test.csv','a',newline="") as f:
	writer = csv.writer(f)
	writer.writerow(list_3)	

