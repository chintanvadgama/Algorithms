class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        print 'Dog name (%s) breed (%s)' % (self.name,self.breed)


dog1 = Dog(name='tommy',breed='bulldog')
dog2 = Dog(name='chintu',breed='germanshepherd')

dog1.__repr__()
dog2.__repr__()