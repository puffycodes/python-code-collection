# file: Cat.py

class Cat:

    # create an instance of Cat
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        return
    
    # function to say meow
    def sayMeow(self):
        message = "{} says meow"
        print(message.format(self.name))
        return
    
    # function to display cat attributes
    def displayFeature(self):
        message = '''Cat Id = {}
Cat Name = {}
Cat Age = {}
'''
        print(message.format(self.id, self.name, self.age))
        return

# --- end of file --- #
