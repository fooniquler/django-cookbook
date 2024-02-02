# django-cookbook

## Description
Django cookbook app with the following functionality:
* #### Database
  The application database stores a list of products. The product has a name, as well as the number of uses of this product in cooking. Recipes of dishes are also stored in the database. The recipe has a name, as well as a set of products included in the recipe, indicating the weight in grams.
  For example, a Cheesecake recipe, which includes products Cottage cheese 200g, Egg 50g, Sugar 10g.

* #### End-points
  The application provides the following HTTP functions that receive parameters using the GET method:
  * add_product_to_recipe/ with the recipe_id, product_id, weight parameters. The function adds the specified product with the specified weight to the specified recipe. If there is already such a product in the recipe, then the function changes its weight in this recipe to the specified one.
  * cook_recipe/ with the recipe_id parameter. The function increases by one the number of cooked dishes for each product included in the specified recipe.
  * show_recipes_without_product/ with the product_id parameter. The function returns the HTML page where the table is located. The table shows the IDs and names of all recipes in which the specified product is missing, or is present in an amount less than 10 grams.
* #### Admin panel
  Django admin panel has been set up, where the user can manage the products and recipes included in the database. For recipes, it is possible to edit the products included in them and their weight in grams.

## Technologies
* Python
* Django
* HTML
* Bootstrap

## Installation and usage
Install requirements
```
pip install -r requirements.txt
```

Add your secret key to the .env file in the base directory (on the same level as manage.py)

Migrate the database
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Create superuser
```
python manage.py createsuperuser
```
Run server
```
python manage.py runserver
```
  
