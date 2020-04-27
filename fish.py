# Base class
class Fish:
    def __init__(self, first_name, last_name='Fish',
                 skeleton='bone', eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print('The fish is swimming')

    def swim_backwards(self):
        print('The fish can swim backwards')


# Subclass 1
class Trout(Fish):
    def __init__(self, water='Freshwater'):
        self.water = water
        super().__init__(self)


terry = Trout()

# Initialize the first name
terry.first_name = 'Terry'

# Use parent __init__() through super()
print(terry.first_name + ' ' + terry.last_name)
print(terry.eyelids)

# Use child __init__() override
print(terry.water)

# Use parent swim() method
terry.swim()


# Subclass 2
class Clownfish(Fish):

    def live_with_anemone(self):
        print('The clownfish is coexisting with sea anemone')


casey = Clownfish('Casey')
print(casey.first_name + ' ' + casey.last_name)
casey.swim()
casey.live_with_anemone()

# Overriding Parent Method
class Shark(Fish):
    def __init__(self, first_name, last_name='Shark',
                 skeleton='cartilage', eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print('The shark cannot swim backwards, but can sink backwards.')


sammy = Shark('Sammy')
print(sammy.first_name + ' ' + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)


# super() keyword

