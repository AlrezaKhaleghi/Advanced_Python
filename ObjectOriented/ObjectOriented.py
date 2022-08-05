class Person:
    count = 0 
    def __init__(self, name, age):
        self.age = age
        self.name = name 
        Person.count = Person.count +1 



    #define new method
    def get_name(self):
        print("person name is %s "  % self.name)
    
    def get_age(self):
        print("person age is %s "  % self.age)
    
    def get_info(self):
        print("person name is %s and person age is %i !"  % (self.name, self.age))

    def birthday(self):
        self.age = self.age + 1
        print ("happy birthday %s" % self.name)

    
    #class variable 
    def persons_count(self):
        return Person.count 



Alireza = Person('Alireza' , 26)
Alireza.get_name()
Alireza.get_age()
Alireza.get_info()
Alireza.birthday()

print ( "number of persons:  %s " % Alireza.persons_count) 


Eti = Person('Arthur' , 2)
Eti.get_name()
Eti.get_age()
Eti.birthday()
Eti.get_age()



print ( "number of persons:  %s " % Alireza.persons_count()) 



