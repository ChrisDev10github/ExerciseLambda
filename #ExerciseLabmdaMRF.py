#ExerciseLabmdaMRF
import csv
from functools import reduce
#Part 1 open file


f=open ('911_Calls_For_Service_(Last_30_Days).csv', 'r') 
dictionaryObject = csv.DictReader(f)
listDictionaries = list(dictionaryObject)
f.close()

#Part 1

filtered = list(filter(lambda x: x["zip_code"] !="0" and x["neighborhood"] !='',listDictionaries))
filteredtrt = list(filter(lambda x: x["totalresponsetime"] !="0" and x["totalresponsetime"] !='',filtered))        

#Average Total Response Time
#totalDispatch = reduce(lambda time1, time2: time1 + float(time2["dispatchtime"]), filtered)
totalResponse= reduce(lambda t1, t2: t1 + float(t2["totalresponsetime"]), filtered, 0)
#totalTime = reduce(lambda time1, time2: time1 + float(time2["totaltime"]), filtered)
print(totalResponse)

