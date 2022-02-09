
Woah .. You actually opened this. Good for you :D.

So, first thx for your help :)

Rules:

- We focus on functionality not complexity or architecture, make it extra simple. So simple that it has no option but to work. Kinda like Forrest Gump.
- Check the FIST LOGIN and EVERY OPEN photos for how the flow should was imagined.(Paint skills on point!)
- Everything is a subject to change, I am not Denis Ritchie here, I probably know way less than you do.
- Everything you do and change, please explain it well, like for a mentally challenged monkey with 1 good eye. That would be me.
- Have fun.

So this app should just have a semi-decent user authentication,
and once you are logged in you are never logged out kinda like instagram.

There is two models USER, and IDEA (for now)
While USER is self-explanatory.

IDEA is a model that will suffer most changes, it is:

- A meal idea,
- with attributes: name, (name of the meal)
                   ingredients( should be a list or probably dict of items and their amount in grams),
                   category(which should be something like, traditional, modern, vegetarian, ect.)
                   prep_time(the time it takes to cook it.)

  it should be saved in the database, and we should be able to filter it by all attributes, I think.
  it should end up in the /idea endpoint as a single idea, or in /weekly endpoint as a list of idea objects ?
  and we should be to generate a weekly shopping list from its ingredients and their amount.

Err.. that's it, for more AMA or don't.

