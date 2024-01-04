class Parent:
    city = "부산"

    def dadHome(self):
        print("아버님 고향은", self.city, "이시다.")

class Child(Parent):
    city = "서울"

    def dadHome(self):
        print("내 고향은", self.city, "이지만")
        super().dadHome()

child = Child()

child.dadHome()
