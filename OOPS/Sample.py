class Piglet:
    name="piglet"

    def speak(self):
        print("Oink ! I'm {} ! Oink".format(self.name))

hamlet=Piglet()
hamlet.name="Hamlet"
hamlet.speak()