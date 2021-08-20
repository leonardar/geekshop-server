from django.db import models
from authapp.models import User
from mainapp.models import Product
from django.utils.functional import cached_property
from geekshop import settings

# Create your models here.

# class BasketQuerySet(models.QuerySet):
#
#     def delete(self, *args, **kwargs):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         super(BasketQuerySet, self).delete(*args, **kwargs)

class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def product_cost(self):
        return self.quantity * self.product.price

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    def total_quantity(self):
        _items = self.get_items_cached
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    def total_cost(self):
        _items = self.get_items_cached
        return sum(basket.product_cost() for basket in _items)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         print(f'{self.product.quantity} -= {self.quantity} - {self.__class__.get_item(self.pk).quantity}')
    #         self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
    #         print(f'{self.product.quantity}')
    #     else:
    #         print(f'{self.product.quantity} -= {self.quantity}')
    #         self.product.quantity -= self.quantity
    #         print(f'{self.product.quantity}')
    #     self.product.save()
    #     super(self.__class__, self).save(*args, **kwargs)
