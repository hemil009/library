from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.


class Book(models.Model):
    LANGUAGE = (
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
        ('German', 'German'),
        ('Hindi', 'Hindi'),
    )

    THEME = (
        ('Sci-fi', 'Sci-fi'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Fiction', 'Fiction'),
        ('Biography', 'Biography'),
        ('Adventure', 'Adventure')
    )
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    language = MultiSelectField(choices=LANGUAGE, blank=False, default="English")
    genre = MultiSelectField(choices=THEME, blank=False)

    class Meta:
        db_table = "book"
