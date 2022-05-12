import json

from django.db import transaction

from api.models import Ingredient


with open("/app/data/ingredients.json", encoding='utf-8') as f:
    data = json.load(f)

    with transaction.atomic():
        for item in data:
            ingredient = Ingredient.objects.get_or_create(
                name=item['name'],
                measurement_unit=item['measurement_unit']
            )
