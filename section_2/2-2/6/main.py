recipe_book = {"Pancakes": ["flour", "milk", "eggs", "sugar"], 
               "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]}
print(f"{recipe_book['Pancakes']}")

def add_recipe(recipe_book: dict, recipe_key: str, ingredients:list):
    recipe_book[recipe_key] = ingredients
    return recipe_book

def update_ingredients(recipe_book: dict, recipe_key: str, new_ingredients:list):
    if recipe_key in recipe_book:
        if recipe_book[recipe_key] != new_ingredients:
            # Updates the dictionary within the new ingredients
            recipe_book[recipe_key]+=new_ingredients
            return recipe_book
        else:
            return recipe_book
    else:
        return recipe_book

# Add a new recipe to the recipe book
ingredients = ["banana", "milk", "honey"]
recipe_book = add_recipe(recipe_book, "Smoothie", ingredients)
#print(f"{recipe_book}")

# Add a new ingredient to an existing recipe
new_ingredient = ["blueberries"]
recipe_book = update_ingredients(recipe_book, "Smoothie", new_ingredient)
print(f"{recipe_book}")

"""Create the Recipe Book:
Create a dictionary named recipe_book with the following recipes:
"Pancakes": ["flour", "milk", "eggs", "sugar"]
"Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
Access Ingredients:
Print the list of ingredients for "Pancakes".
Add a New Recipe:
Add a new recipe "Smoothie" with the ingredients ["banana", "milk", "honey"] to the dictionary.
Modify a Recipe:
Add "blueberries" to the "Smoothie" recipe.
Print All Recipes:
Print the entire recipe_book dictionary to verify the updates."""