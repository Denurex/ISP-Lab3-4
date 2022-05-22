
"""The composition of the application.
Models that should be stored in the database"""

from django.db import models


class Comment(models.Model):
    name = models.CharField('Имя', max_length=30)
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Product(models.Model):
    PHONE = 'phone'
    LAPTOP = 'laptop'
    PC = 'pc'
    ACC = 'accessories'

    CHOICE_GROUP = {
        (PHONE, 'phone'),
        (LAPTOP, 'laptop'),
        (PC, 'pc'),
        (ACC, 'accessories')
    }

    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=PHONE)
    img = models.ImageField(default='no_image.jpeg', upload_to="product_image")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

