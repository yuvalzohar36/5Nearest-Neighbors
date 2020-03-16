import json
from pprint import pprint

def setup():
    top_k = 5
    top5 = {}
    titles = []
    top5_SumSquars = {}
    top5_sorted = []
    size(600,600)
    background(255)
    fill(0)
    textSize(33);
    with open('movies.json') as f:
        data = json.load(f)
        users = {}                   # Declare users var
    person1 = "KhanStan"

    for i in range(len(data['users'])):
        name = data['users'][i]['name']
        users[name] = data['users'][i]     # organize the data {name , [ratings]
   
    
    for key, value in users[person1].items():
        if (key != "name" and key != "timestamp"):   # Sorting "timestamp && name" 
            titles.append(key)
    
    
    for key, value in users.items():
        sumSquares = 0 
        for j in range(len(titles)):
            title = titles[j];
            rating1 = users[key][title]
            rating2 = users[person1][title]
            if (rating1 != None and rating2 != None):
                        diff = rating1 - rating2
                        sumSquares += diff * diff
        top5_SumSquars[key] = sumSquares
        top5_sorted.append(sumSquares)
                    
    top5_sorted.sort(reverse = True)  
    count = 0
    for r in range(5):
        for key, value in top5_SumSquars.items():
            if (value == top5_sorted[r] and count <5):
                count+=1
                top5[key] = value    
    for key, value in top5.items():
        top5[key] = sqrt(value)
    where = 1;
    textSize(20)
    text("The 5 Nearest neighbor to " + person1 +" are:" ,0,50)
    for key, value in top5.items():
        text(str(where) +": name :" + key + "  ||  Similarity : " + str(float(value)),0,100*where)
        where+=1
    
