import random
from common.database import Database

latest_ideas = []


class LunchIdea:
    """ This is the idea class """
    def __init__(self, num, name, ingredients, category, prep_time, _id=None,):
        self.num = num
        self.name = name  # should be the name of the meal
        self.ingredients = ingredients  # should be a list of a dictionary of ingredients with this amount in grams
        self.category = category  # should be a category of food ex: traditional, modern, italian, vegetarian, vegan🤮
        self.prep_time = prep_time  # should be average preparation time .. or we just drop this :)

    @classmethod
    def add_idea(cls, num, name, ingredients, category, prep_time, _id=None):   # Wrote it with my ass, maybe it works.
        """Just a method to use to populate the meal database collection"""
        # count = Database.count_entries('ideas')
        # print(count)
        new_idea = cls(num, name, ingredients, category, prep_time)
        print(new_idea.name)
        new_idea.save_idea()
        return "Your idea has been added to the database."

    # These get ideas by category, might need some to get they my _id .. when we have an _id for ideas xD
    @classmethod
    def get_idea(cls, category, num):
        """Gets an idea from the database by category"""
        data = Database.find_one("ideas", {"category": category, "num": num})  # Not tested but should work
        if data is not None:
            return cls(**data)

    @classmethod
    def generate_idea(cls, category):
        """Generates an idea from the database by category and number to be shown client side"""
        if len(latest_ideas) == 2:
            latest_ideas.clear()
        count = Database.count_entries('ideas')
        num = random.randint(0, count-1)
        current_idea = Database.find_one("ideas", {"category": category, "num": num})

        if current_idea not in latest_ideas and not None:
            latest_ideas.append(current_idea)
            print(latest_ideas)
            return cls(**current_idea)
        else:
            current_idea = Database.find_one("ideas", {"category": category, "num": num-1})
            return cls(**current_idea)

    @classmethod
    def get_ideas(cls, category):
        """Gets all ideas from a category"""
        data = Database.find("ideas", {"category": category})  
        return data
        # Not tested don't know if it will work for list of objects might need to iterate list of objects

    def json(self):
        return {
            "num": self.num,
            "name": self.name,
            "ingredients": self.ingredients,
            "category": self.category,
            "prep_time": self.prep_time,
                }

    def save_idea(self):  # Will be used to populate the database I guess..
        """Saves an idea to the database"""
        Database.insert("ideas", self.json())
