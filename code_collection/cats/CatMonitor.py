# file: CatMonitor.py

from Cat import Cat

class CatMonitor:

    # create object
    def __init__(self, catList=[]):
        # create a dictionary to hold the record of the cats
        self.record = {}
        # create a list to hold the age of the cats
        self.ageList = []
        # create a list to hold the id of the cats
        self.idList = []
        # add cat to our list, individually
        for cat in catList:
            self.addCatRecord(cat)
        return
    
    # create function to get the oldest cat
    def getOldestCat(self):
        oldestAgeValue = max(self.ageList) # find the oldest age
        oldestAgeIndex = self.ageList.index(oldestAgeValue) # find the position of the oldest cat
        oldestAgeId = self.idList[oldestAgeIndex] # find the id of the oldest cat
        oldestCat = self.record[oldestAgeId] # find the record for the oldest cat
        return oldestCat
    
    # create function to calculate average age
    def getAverageAge(self):
        average = sum(self.ageList)/len(self.ageList) # average is total divides by count
        return average
    
    # create function to allow user to add a new record
    def addCatRecord(self, cat):
        self.record[cat.id] = cat # add the cat to the dictionary
        self.ageList.append(cat.age) # add the age of the cat to the age list
        self.idList.append(cat.id) # add the id of the cat to the id list
        return
    
# --- end of file --- #
