class Person:
    ''' Person class '''
    def __init__(self, name, age):
        # _name and _age are instance variable and _ convention is used for private variables
        self._name = name
        self._age = age

    @property
    def name(self):
       ''' This returns person's name ''' 
       return self._name
 
    @name.setter
    def name(self, name):
       if len(self.name.strip()) > 1 and isinstance(name,str):
           self._name = name
       else:
           raise ValueError("Name cannot be empty and must be of type str")
    
    @property
    def age(self):
       ''' This returns person's age ''' 
       return self._age

    @age.setter
    def age(self, age):
       if self.age > 0 and isinstance(age,int):
           self._age = age
       else:
           raise ValueError("Age must be postive value and must be of type int")

    def __repr__(self):
       return 'Person(name = {}, age = {})'.format(self.name,self.age)


p = Person("Guru",34)
print(p.name)

# Raises/throws ValueError exception of setter
#p.name = 1
#print(p.name)
#p.age = "str"

p.age = 25
print(p)

print("Person instance p __dict__ property {} ".format(p.__dict__))
print('Person class __dict__ property {}'.format(Person.__dict__))
