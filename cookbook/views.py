from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic, View
from .models import Recipe, Product, RecipeProduct


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class AddProductToRecipeView(View):
    def get(self, request):
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        recipe_product, created = RecipeProduct.objects.update_or_create(recipe=recipe, product=product,
                                                                         defaults={'weight': weight})

        if not created:
            return HttpResponse('Был обновлен вес')

        return HttpResponse('Был добавлен продукт')


class CookRecipeView(View):
    def get(self, request):
        recipe_id = request.GET.get('recipe_id')

        recipe = get_object_or_404(Recipe, pk=recipe_id)

        recipe_products = RecipeProduct.objects.filter(recipe=recipe)

        for recipe_product in recipe_products:
            with transaction.atomic():
                product = Product.objects.select_for_update().get(pk=recipe_product.product.pk)
                product.times_used += 1
                product.save()

        return HttpResponse('Было увеличено на единицу количество приготовленных блюд для каждого продукта, '
                            'входящего в указанный рецепт.')


class ShowRecipesWithoutProductView(generic.ListView):
    model = Recipe
    template_name = 'show_recipes.html'

    def get_queryset(self):
        product_id = self.request.GET.get('product_id')

        product = get_object_or_404(Product, pk=product_id)

        queryset = (self.model.objects.filter(~Q(recipeproduct__product=product) | Q(recipeproduct__product=product,
                                                                                     recipeproduct__weight__lt=10))
                    .distinct())

        return queryset
