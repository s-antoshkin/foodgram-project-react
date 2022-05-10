from django.contrib import admin

from .models import Cart, Favorite, Recipe, Ingredient, IngredientAmount, Tag


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('favorites_count',)
    inlines = [
        IngredientAmountInline
    ]

    def favorites_count(self, obj):
        return obj.favorites.count()

    favorites_count.short_description = 'Число добавлений в избранное'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    pass
