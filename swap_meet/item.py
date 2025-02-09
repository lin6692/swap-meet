class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_desc = ["please check with customer service",
                          "worn/used few times",
                          "no flaws",
                          "good",
                          "excellent",
                          "new",]
        return condition_desc[int(self.condition)]