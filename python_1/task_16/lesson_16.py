class Animal:
    def __init__(self, age: int = 10):
        self.name = "Pearch"
        self.age = 10
        # self.age = self.age + age

    def run(self):
        value = f"bega greitai {self.name}"
        print(value)

    def lipti_i_medi(self):
        self.run()
        print(f"{self.name} karstosi i medi")

    def begti_lipti_i_medi(self):
        self.run()
        self.lipti_i_medi()

animal = Animal()

animal.begti_lipti_i_medi()