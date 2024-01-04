class Dog:
    def dogBarking(self, howling):
        print("내 개는", howling, "하고 짖어요.")

class MyDog(Dog):
    def dogBarking(self, howling):
        print("내 강아지는", howling, "하고 짖어요.")
        super().dogBarking(howling)

my_dog = MyDog()

my_dog.dogBarking("컹컹!")
