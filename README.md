##Problem:##

There is a list of 4 things: Name, Product, Activity, Time. Activity contains three activities: View, Add to cart (ATC) and Buy.
Name contains the names of the people involved with a particular product and Time contains the time corresponding to that activity,

The ideal flow of the activity is:
1, View
2. Add to Cart
3. Buy

The problem is to find out if the given list, for every person and product, if the ideal flow is followed or not.
I print 'True' if it follows, and 'False' if it does not follow.


##Solution:##

I am dividing this problem into three parts:

#1. Storing the given information in a dictionary:#

I have made a dictionary called d in which the 'key' is a tuple of name and product and 'value' is a list of a tuple of activity and time.
key: (name, product)
value: [(activity, time)]

In the if-else statement, I am checking if the dictionary already has values corresponding to the current key.
If it does, I append the current value to the already existing key, if not I add the value to the new key in the dictionary d.

#2. Make a class:#

I made a class called find_workflows_adhering() to find if the workflow is followed.



