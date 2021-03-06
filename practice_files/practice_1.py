class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False

    # instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

jethro = Dog('Jethro', '6 months', 'Australian Shepherd')
luna = Dog('Luna', '4 months', 'Labrador Retreiver')

# both will be 4 because it is a shared class attribute
print("----Number of Legs----")
print(jethro.num_of_legs)
print(luna.num_of_legs)

# now these will be different because they are instance attributes
# each instance will have to set these
print("----Dog Names----")
print(jethro.name)
print(luna.name)

# let's change a class attribute
print("----Class Attribute Changing----")
jethro.can_fly = True
print(jethro.can_fly)
print(luna.can_fly)

# let's change an instance attribute
print("----Instance Attribute Changing----")
print(jethro.age)
jethro.age = '7 months'
print(jethro.age)