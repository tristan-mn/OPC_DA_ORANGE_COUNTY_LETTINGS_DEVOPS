from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model d'objet profile pour la création d'instances

    Args:
        models (object): on hérite de l'objet Model des models de database de django

    Returns:
        string: on retourne une chaine de caractères
        représentant l'instance avec le username du user
    """

    user = models.OneToOneField(
        User, related_name="user_profile_app", on_delete=models.CASCADE
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
