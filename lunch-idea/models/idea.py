from common.database import Database


class LunchIdea:
    """ This is the idea class """
    def __init__(self, num, name, ingredients, category, prep_time, _id=None,  ):
        self.num = num
        self.name = name  # should be the name of the meal
        self.ingredients = ingredients  # should be a list of a dictionary of ingredients with this amount in grams
        self.category = category  # should be a category of food ex: traditional, modern, italian, vegetarian, vegan🤮
        self.prep_time = prep_time  # should be average preparation time .. or we just drop this :)

    @classmethod
    def add_idea(cls, num, name, ingredients, category, prep_time, _id=None):   # Wrote it with my ass, maybe it works.
        """Just a method to use to populate the meal database collection"""
        count = Database.count_entries('ideas')
        print(count)
        new_idea = cls(num, name, ingredients, category, prep_time)
        print(new_idea.name)
        new_idea.save_idea()
        return "Your idea has been added to the database."

    # These get ideas by category, might need some to get they my _id .. when we have an _id for ideas xD
    @classmethod
    def get_idea(cls, category):
        """Gets an idea from the database by category"""
        data = Database.find_one("ideas", {"category": category})  # Not tested but should work
        if data is not None:
            return cls(**data)

    @classmethod
    def get_ideas(cls, category):
        """Gets all ideas from a category"""
        data = Database.find("ideas", {"category": category})  
        return cls(**data)
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


