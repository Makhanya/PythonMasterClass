class Animal:
    def make_sound(self, sound):
        print(f"this animal says {sound}")

    cool = True


class Cat(Animal):
    pass


gandalf = Cat()
gandalf.make_sound("meow")
gandalf.cool
