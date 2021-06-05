import factory

from lostcats.models import LostCat


class LostCatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LostCat

    title = factory.Faker("catch_phrase")
    description = factory.Faker("paragraph", nb_sentences=2)
    latitude = factory.Faker("pyfloat", min_value=-180, max_value=180)
    longitude = factory.Faker("pyfloat", min_value=-180, max_value=180)
    image = (
        factory.django.ImageField()
    )  # https://factoryboy.readthedocs.io/en/stable/orms.html#factory.django.ImageField
