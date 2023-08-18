from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model d'objet address pour la création d'instances

    Args:
        models (object): on hérite de l'objet Model des models de database de django

    Returns:
        string: on retourne une chaine de caractères
        représentant l'instance avec le numero et la rue
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model d'objet letting pour la création d'instances

    Args:
        models (object): on hérite de l'objet Model des models de database de django

    Returns:
        string: on retourne une chaine de caractères représentant l'instance avec le titre
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
