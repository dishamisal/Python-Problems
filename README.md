### Problem:

There is a list of 4 things given: Name, Product, Activity, Time. Activity contains three activities: View, Add to cart (ATC) and Buy.
Name contains the names of the people with a particular product and Time contains the time corresponding to every activity.

The ideal workflow is the following:
1. View
2. Add to Cart
3. Buy

The problem is to find out if the given list, for every person and product, follows the ideal workflow or not.
I print 'True' if it follows, and 'False' if it does not follow.


### Solution:

I am dividing this problem into three parts:

###### 1. Storing the given information in a dictionary:

I have made a dictionary called d in which the 'key' is a tuple of name and product and 'value' is a list of a tuple of activity and time.
key: (name, product)
value: [(activity, time)]

In the if-else statement, I am checking if the dictionary already has values corresponding to the current key.
If it does, I append the current value to the already existing key, if not I add the value to the new key in the dictionary d.


###### 2. Make a list of time:

I made a class called find_workflows_adhering() to find if the workflow is followed. If my Activity resembles the activity in the ruleset, for a given Name and Product, I add the corresponding time to the list of time that I entend to make. At the end of this step I will have the times corresponding to every Activity in order.


###### 3. Comparing time:

From the list of times of activities, I compare every element with the next element. Every element must be less than the element next to it, implying that the current Activity has occured before the Activity right after it. As long as this follows, the print will give 'True', else I print 'False'.

Another method of doing this is checking if the list of Time called timePeriods in this case is equal to the sorted(timePeriods), since sorted() gives the increasing order of the numerical or alphabetical data.



