# file: main.py

from Cat import Cat
from CatMonitor import CatMonitor

# create instances of Cat
cat1 = Cat('C1', 'Tabby', 3)
cat2 = Cat('C2', 'Kitty', 1)
cat3 = Cat('C3', 'Tommy', 2)
cat4 = Cat('C4', 'Tikki', 6)
cat5 = Cat('C5', 'Tammy', 7)

# create the list of all cats
allCats = [ cat1, cat2, cat3, cat4, cat5 ]

# create the cat monitor
monitor = CatMonitor(catList=allCats)

# calcuate the average age of the cat and find the oldest cat
averageAge = monitor.getAverageAge()
oldestCat = monitor.getOldestCat()

# display the average age of the cats
message = "Average age of cats is {:.1f} years old" # display flot to 1 decimal point
print(message.format(averageAge))
print()

# display the attributes of the oldest cats
print("Oldest cat is:")
oldestCat.displayFeature() # call function from Cat to display the cat attributes

# allow user to enter a new cat record
catId = input("Please enter new cat ID: ")
catName = input("Please enter new cat name: ")
catAge = input("Please enter new cat age: ")
catAge = int(catAge)
newCat = Cat(catId, catName, catAge)
monitor.addCatRecord(newCat)
print()

# calculate and display the new average age
averageAge = monitor.getAverageAge()
message = "New average age of cats is {:.1f} years old"
print(message.format(averageAge))

# ----------- code below are for testing purpose ---------- #

# function for us to test the cats
def cat_test_01():
    # get all the cats to say meow
    for cat in allCats:
        cat.sayMeow()

    print()

    # display the attributes of all cats
    for cat in allCats:
        cat.displayFeature()

    return

#cat_test_01()

# --- end of file --- #
