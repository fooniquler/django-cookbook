from django.urls import path
from .views import HomeView, AddProductToRecipeView, CookRecipeView, ShowRecipesWithoutProductView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_product_to_recipe/', AddProductToRecipeView.as_view(), name='add_product'),
    path('cook_recipe/', CookRecipeView.as_view(), name='cook_recipe'),
    path('show_recipes_without_product/', ShowRecipesWithoutProductView.as_view(), name='show_recipes'),
]
