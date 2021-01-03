import pandas as pd
import numpy as np
from pprint import pprint

#import the rows containing name, product, activity and time:
rows=[
    ('n1','p1','a1','t2'),
    ('n2','p2','a2','t2'),
    ('n1','p1','a2','t1')
]

#define the ruleset, which has activities a1 and a2 in this case:
ruleSet = ['a1', 'a2']

#define an empty dictionary:
d={}

#import the 1st row as name, 2nd as product, 3rd as activity and 4th as time:
for row in rows:
    n = row[0]
    p = row[1]
    a = row[2]
    t = row[3]
    #n,p,a,t
    
#if dictionary d already has values corresponding to the current key, append the new values to those values,
else add the value to the key of the dictionary:    
    if (n,p) in d.keys():
        d[(n,p)].append((a,t))
    else:
        d[(n,p)] = [(a,t)]

#print the dictionary d with all its keys and corresponding values:
pprint(d)
{('n1', 'p1'): [('a1', 't2'), ('a2', 't1')], ('n2', 'p2'): [('a2', 't2')]}

#Part-1 of the problem is over here. I have made dictionaries with the keys as a tuple of (name, product) and 
values as a list of tuples of (activity, product)

#define a function to check the workflow of the rukeset:

def find_workflows_adhering():
    '''
        Returns count of workflows which adhere
    '''
    count_workflows = 0
    
    for i, values in enumerate(d.values()):
        falseFlag = True
        
#create an empty list of timePeriods to add all the times corresponding to activities:        
        timePeriods = []
        for activity in ruleSet:
            valueNotFoundFlag = True
            for (a, t) in values:
                if (a == activity):
                    # t is my time
                    # add t to the time periods list
                    
                    timePeriods.append(t)
                else:
                    valueNotFoundFlag = False
            
            # Done with for loop, so continue
            # if valueNotFoundFlag
            
        # Done with TimePeriods
        # Check if time periods list has the same number of entries as the ruleset
        if (len(timePeriods) == len(ruleSet)):
            pass
        else:
            falseFlag = False
        
        # Check if the list of time periods is increasing
        # Method 1:
        for (index, t) in enumerate(timePeriods[:-1]):
            next_t = timePeriods[index + 1]
            if (t < next_t):
                continue
            else:
                falseFlag = False
                
        # Check if workflow adheres
        if falseFlag == True:
            count_workflows += 1
        
    return count_workflows;

print(find_workflows_adhering())
    
    # Method 2:
#     if (timePeriods == sorted(timePeriods))
#     value=d.get('(n,p)')
#     print(d.get('(n,p)'))
#     print(t)
