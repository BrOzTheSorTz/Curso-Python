
#Inheritance and Composition practice

class Animal:
    name =""
    category=""
    def __init__(self,name):
        self.name = name

    def set_category(self,category):
        self.category=category

#Turtles and Snakes are animals

class Turtle(Animal):
    category="reptile"

class Snake(Animal):
    category="reptile"

#A zoo has animals

class Zoo:
    def __init__(self):
        #We create a dictionary which store 
        # all the animals
        
        self.current_animals={}
    def add_animal(self,animal):
        #We use the name of the animals as the keys
        # and the categories as values

        self.current_animals[animal.name]=animal.category
    def total_of_category(self,category):
        result = 0
        for animals in self.current_animals.values():
            if animals == category:
                result += 1
        return result
    
    
zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category