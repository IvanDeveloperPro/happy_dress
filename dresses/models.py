from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.db import models

User = get_user_model()

DELIVERY_CHOICES = [
    ('PI', 'Самовывоз'),
    ('DL', 'Доставка')
]


class Dress(models.Model):
    item = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    size = models.CharField(
        max_length=30,
        verbose_name='Рост'
    )
    volume = models.PositiveIntegerField(
        verbose_name='Объем груди'
    )

    discount = models.PositiveIntegerField(
        verbose_name='Скидка',
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    image_1 = models.ImageField(
        verbose_name='Фото_1',
        upload_to='dresses/media',
        blank=True,
        null=True
    )
    image_2 = models.ImageField(
        verbose_name='Фото_2',
        upload_to='dresses/media',
        blank=True,
        null=True
    )
    image_3 = models.ImageField(
        verbose_name='Фото_3',
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
    rent_date = models.DateTimeField(
        verbose_name='Дата брони',
        db_index=True
    )
    type_lease = models.CharField(
        verbose_name='Где будут использовать платье',
        max_length=50,
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=500,
        verbose_name='Адрес доставки',
        null=True,
        blank=True,
    )
    cost = models.PositiveIntegerField(
        verbose_name='Стоимость заказа'
    )

    class Meta:
        verbose_name = 'Заказ',
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.id} - {self.tenant.username}'


class Basket(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Заказчик',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='baskets'
    )
    session = models.ForeignKey(
        Session,
        verbose_name='Сессия',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='baskets'
    )
    dress = models.ManyToManyField(
        Dress,
        verbose_name='Платье',
        related_name='baskets'
    )
    rent_date = models.DateField(
        verbose_name='Дата аренды',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
