class Apple:
    def __init__(self,color, flavor):
        self.color=color
        self.flavor=flavor

    def __str__(self):
        return "The Apple is {} and its flavor is {}".format(self.color,self.flavor)
fruit= Apple("red","Sweet")
print(fruit.color)
print(fruit)