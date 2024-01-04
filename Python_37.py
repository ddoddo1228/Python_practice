class Parent:
    def __init__(self, school, major):
        self.school = school
        self.major = major

    def nameCard(self):
        print("학교: {}, 전공: {}".format(self.school, self.major))


class Child(Parent):
    def __init__(self, school, major, name, company, duty):
        super().__init__(school, major)
        self.name = name
        self.company = company
        self.duty = duty

    def nameCard(self):
        print("{}님은 {} {}를 졸업했습니다.".format(self.name, self.school, self.major))
        print("현재 {} '인터넷진흥원' {} 부서에 연구원으로 재직중입니다.".format(self.company, self.duty))


kids = Child("한국대학교", "전자공학과", "홍길동", "KISA", "개인정보침해대응부서")
kids.nameCard()
