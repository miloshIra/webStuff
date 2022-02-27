# import requests
from common.database import Database
from models.idea import LunchIdea
# from models.user import User

Database.initialize()

ideas = LunchIdea.get_ideas('tradicionalna')

count = 0

for idea in ideas:
    count = count + 1

print(count)
#
# num = 3
# name = "Спањак"
# ingredients = ['300г ориз', '300 спањак', '2 јајца']
# category = 'tradicionalna'
# prep_time = '40mins'
#
# # with open('data.csv', 'r') as data:
# #     for item in data:
# #         LunchIdea.add_idea(item[0], item[1], item[3], item[4])
# #
# #
# # # new_user = User("Losh", "123@gmail.com", "123123")
# # # new_user.register("Milosh", "123@gmail.com", "123123")
# #
# new_idea = LunchIdea.add_idea(num, name, ingredients, category, prep_time)
# new_idea.add_idea(name, ingredients, category, prep_time)
#
# current_idea = LunchIdea.get_idea("tradicionalna")
# print(len(current_idea.ingredients))
# print(current_idea.ingredients[0])
# print(len(current_idea))

# print(Database.count_entries('ideas'))

#
# LunchIdea.add_idea(name, ingredients, category, prep_time)
# print(type(new_idea))
# LunchIdea('Meso so kompir', ['200g meso', '200g kompir'], 'tradicionalna', '40mins').save_idea()
