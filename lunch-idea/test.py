# import requests
from common.database import Database
from models.idea import LunchIdea
import random

# from models.user import User

Database.initialize()

# ideas = LunchIdea.get_ideas('tradicionalna')
# all_ideas = []
# past_ideas = []
#
# for idea in ideas:
#     all_ideas.append(idea)
#
# print(all_ideas)
# count = 3
#
# print(count)
#
# current_idea = (all_ideas[random.randint(0, count)])
# if current_idea in past_ideas:
#     current_idea = (all_ideas[random.randint(0, count)])
# else:
#     print(current_idea)
#     past_ideas.append(current_idea)

# print(past_ideas)
#
num = 10
name = "Лазањи"
ingredients = ['кори за лазањи', '300г мелено месо', '150г кашкавал']
category = 'tradicionalna'
prep_time = '40mins'
#
# #
# #
# # # new_user = User("Losh", "123@gmail.com", "123123")
# # # new_user.register("Milosh", "123@gmail.com", "123123")
# #
LunchIdea.add_idea(num, name, ingredients, category, prep_time)
# new_idea.add_idea(name, ingredients, category, prep_time)
#
# current_idea = LunchIdea.get_idea("tradicionalna")
# print(len(current_idea.ingredients))
# print(current_idea.ingredients[0])
# print(len(current_idea))

print(Database.count_entries('ideas'))

#
# LunchIdea.add_idea(name, ingredients, category, prep_time)
# print(type(new_idea))
# LunchIdea('Meso so kompir', ['200g meso', '200g kompir'], 'tradicionalna', '40mins').save_idea()
