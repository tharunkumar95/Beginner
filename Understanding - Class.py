class Shark:
    # Constructor Method
    def __init__(self, name):
        self.name = name
        # self.age = age

    # Reference the same
    def swim(self):
        print(self.name + ' is swimming!')

    # Reference the same
    def be_awesome(self):
        print(self.name + ' is being awesome!')


def main():
    # Set the name of 'Shark' object
    sammy = Shark('Sammy')
    sammy.swim()
    stevie = Shark('Stevie')
    stevie.be_awesome()


# main method
if __name__ == '__main__':
    main()