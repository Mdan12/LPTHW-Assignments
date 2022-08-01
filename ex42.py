## Animal is-a object
class Animal(object):
    #pass is just a placeholder for functionality to be added later.
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name of some kind
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name of some kind
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name of some kind
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## This is how your run the __init__ method of a parent class reliably.
        super(Employee, self).__init__(name)
        ## Employee has-a salary of some kind
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary's pet is satan
mary.pet = satan

## Frank is-a Employee, his salary is 120000
frank = Employee("Frank", 120000)

## Frank's pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
