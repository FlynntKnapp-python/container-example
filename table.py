# container = "Seth's container"
# print("Seth's container")
# # Seth's container
# print(container)
# # Seth's container
# print(type(container))
# # <class 'str'>
# print(type(print))
# # <class 'builtin_function_or_method'>
# print(type(print()))
# # <class 'NoneType'>


class Container:
    def __init__(self, name):
        print("we are building the container object")
        self.name = name
        self.volume = 0
        print("we are done building the container object")
        pass

    def __str__(self):
        return f'{self.name}: {self.volume}'
    
box = Container('jack in the box')

bag = Container('carry on bag')

print(box)
print(bag)

class Box(Container):
    pass

class Bag(Container):
    pass

