# import requests
from common.database import Database
from models.idea import LunchIdea
import csv
# from models.user import User

Database.initialize()

name = "Meso so kompir"
ingredients = ['200g meso', '200g kompir']
category = 'tradicionalna'
prep_time = '40mins'

with open('data.csv', 'r') as data:
    for item in data:
        LunchIdea.add_idea(item[0], item[1], item[3], item[4])


# new_user = User("Losh", "123@gmail.com", "123123")
# new_user.register("Milosh", "123@gmail.com", "123123")

LunchIdea.add_idea(name, ingredients, category, prep_time)
# new_idea.add_idea(name, ingredients, category, prep_time)


#
# LunchIdea.add_idea(name, ingredients, category, prep_time)
# print(type(new_idea))
# LunchIdea('Meso so kompir', ['200g meso', '200g kompir'], 'tradicionalna', '40mins').save_idea()
