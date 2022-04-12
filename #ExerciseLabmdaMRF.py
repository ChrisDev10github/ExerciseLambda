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
filteredtdt = list(filter(lambda x: x["dispatchtime"] !="0" and x["dispatchtime"] !='',filteredtrt))    
filteredlist = list(filter(lambda x: x["totaltime"] !="0" and x["totaltime"] !='',filteredtdt))   

#Average Total Response Time
totalDispatch = reduce(lambda time1, time2: time1 + float(time2["dispatchtime"]), filteredlist,0)
print(f"Average dispatch time: {totalDispatch / len(filteredlist)}")
totalResponse= reduce(lambda t1, t2: t1 + float(t2["totalresponsetime"]), filteredlist, 0)
print(f"Average response time: {totalResponse / len(filteredlist)}")
totalTime = reduce(lambda time1, time2: time1 + float(time2["totaltime"]), filteredlist,0)
print(f"Average total time: {totalTime / len(filteredlist)}")



#Part 2
neighborhoodnames = []
for i in filteredlist:
    if i["neighborhood"] not in neighborhoodnames:
        neighborhoodnames.append(i["neighborhood"])
print(neighborhoodnames)
nvalues = []

for n in neighborhoodnames:
    for i in filteredlist:
        if filteredlist[i] == n:
            #reduce function
            print("hello World")


#part 3
#f = open('911.json', "w")
#json.dump(cleanedList, f)
#f.close()