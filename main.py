from recipe_list import get_recipe_list
from recipe_details import get_recipe_details

recipe_list = get_recipe_list()

for recipe in recipe_list:
    recipe_info = get_recipe_details(recipe)
    
    if recipe_info == []:
        pass
    else:
        '''
        0['name']
        1['nutrition']
        2['recipeIngredient']
        3['prepTime']
        4['cookTime']
        5['totalTime']
        6 str_url
        '''
        print("scraped " + recipe_info[0] + " from " + recipe_info[6])
    