from pprint import pprint

import requests


class Drink:
    endpoint = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

    def __init__(self, name: str) -> None:
        self.endpoint: str = f"{Drink.endpoint}{name}"
        self._data = None
        self._ingredients = None
        self.name = name

    @property
    def template(self):
        return {
            "name": self.name,
            "thumbnail": self.thumbnail,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
        }

    @property
    def thumbnail(self):
        return self.data['strDrinkThumb']

    @property
    def instructions(self):
        return self.data['strInstructions']

    @property
    def ingredients(self):
        if self._ingredients is None:
            self._ingredients = []
            for i in range(1, 16):
                ingredient = self.data.get(f"strIngredient{i}", None)
                measure = self.data.get(f"strMeasure{i}", None)
                if ingredient is not None and measure is not None:
                    self._ingredients.append((ingredient, measure))
        return self._ingredients


    @property
    def data(self):
        if self._data is None:
            self._data = requests.get(self.endpoint).json()["drinks"][0]
        return self._data


pprint(Drink("Margarita").data)
