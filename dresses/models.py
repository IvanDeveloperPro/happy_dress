from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

DELIVERY_CHOICES = [
    ('PI', 'Самовывоз'),
    ('DL', 'Доставка')
]


class DressType(models.Model):
    item = models.CharField(
        max_length=200,
        verbose_name='Тип платья'
    )

    class Meta:
        verbose_name = 'Тип платья'
        verbose_name_plural = 'Тип платьев'

    def __str__(self):
        return self.item


class Color(models.Model):
    color = models.CharField(
        max_length=200,
        verbose_name='Цвет'
    )

    class Meta:
        verbose_name = 'Цвет',
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.color


class LeaseType(models.Model):
    type = models.CharField(
        max_length=200,
        verbose_name='Тип использования',
    )

    class Meta:
        verbose_name = 'Тип использования',
        verbose_name_plural = 'Типы использования'

    def __str__(self):
        return self.type


class Dress(models.Model):
    item = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    price = models.FloatField(
        verbose_name='Цена'
    )
    size = models.PositiveIntegerField(
        verbose_name='Рост'
    )
    volume = models.PositiveIntegerField(
        verbose_name='Объем груди'
    )
    type = models.ManyToManyField(
        DressType,
        verbose_name='Тип платья',
        related_name='dresses',
        blank=True,
    )
    color = models.ForeignKey(
        Color,
        verbose_name='Цвет',
        on_delete=models.SET_NULL,
        related_name='dresses'
    )
    discount = models.PositiveIntegerField(
        verbose_name='Скидка',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='dresses/media',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Платье',
        verbose_name_plural = 'Платья'

    def __str__(self):
        return self.item


class Order(models.Model):
    tenant = models.ForeignKey(
        User,
        verbose_name='Заказчик',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    dress = models.ManyToManyField(
        Dress,
        verbose_name='Платье',
        related_name='orders'
    )
    date_order = models.DateTimeField(
        verbose_name='Дата заказа',
        auto_now_add=True,
        db_index=True
    )
    type_lease = models.ForeignKey(
        LeaseType,
        verbose_name='Тип использования',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
        blank=True
    )
    delivery = models.CharField(
        max_length=2,
        verbose_name='Вид доставки',
        choices=DELIVERY_CHOICES,

    )
    address = models.CharField(
        max_length=500,
        verbose_name='Адрес доставки',
        null=True,
        blank=True,
    )
    cost = models.FloatField(
        verbose_name='Стоимость заказа'
    )

    class Meta:
        verbose_name = 'Заказ',
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.id} - {self.tenant.name}'
