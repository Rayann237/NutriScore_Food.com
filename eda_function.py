"""This package contains the functions used in the recipe analysis."""

import pandas as pd

def unique_ingredient(df):
    """This function returns the number of different ingredients in the dataset.

    Args:
        df : dataframe containing the recipes

    Returns:
        list: list of the different ingredients
    """
    recipes_ingredients = df["ingredients"]
    ingredients = []
    for i in recipes_ingredients:
        ingredients.extend(i) 
    print("The number of different ingredients:", len(set(ingredients)))
    return list(set(ingredients)), ingredients

def ingredient_frequency(df, ingredients):
    """This function returns the n most used ingredients in the dataset.

    Args:
        ingredients : list of the different ingredients
        df : dataframe containing the recipes

    Returns:
        DataFrame: dataframe containing the frequency of used ingredients
    """
    ingredient_count = {}
    for ingredient in ingredients:
        if ingredient in ingredient_count:
            ingredient_count[ingredient] += 1
        else:
            ingredient_count[ingredient] = 1
    ingredient_count = pd.DataFrame.from_dict(ingredient_count, orient='index', columns=['count'])
    ingredient_count = ingredient_count.reset_index().rename(columns={'index':'ingredient'})
    ingredient_count['percentage'] = round(ingredient_count['count'] / len(df) * 100, 2)
    return ingredient_count.sort_values(by=['count'], ascending=False)
    