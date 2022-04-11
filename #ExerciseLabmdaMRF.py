#ExerciseLabmdaMRF
import csv
from functools import reduce
#Part 1 open file


f=open ('911_Calls_For_Service.csv', 'r') 
dictionaryObject = csv.DictReader(f)
listOfDictionaries = list(dictionaryObject)
f.close()
print(listOfDictionaries)