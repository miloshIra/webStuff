from common.database import Database


class LunchIdea:
    """ This is the idea class """
    def __init__(self, name, ingredients, category, prep_time, _id=None, ):
        self.name = name  # should be the name of the meal
        self.ingredients = ingredients  # should be a list of a dictionary of ingredients with this amount in grams
        self.category = category  # should be a category of food ex: traditional, modern, italian, vegetarian, vegan🤮
        self.prep_time = prep_time # should be average preparation time .. or we just drop this :)

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
            "name": self.name,
            "ingredients": self.ingredients,
            "category": self.category,
            "prep_time": self.prep_time,
                }

    def save_idea(self): # Will be used to populate the database I guess..
        """Saves an idea to the database"""
        Database.insert("ideas", self.json())




