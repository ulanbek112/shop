from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import DecimalField

User = get_user_model()


class LatestProductsManager:
    pass


def get_products_for_main_page(*args, **kwargs):
    with_respect_to = kwargs.get('with_respect_to')
    products = []
    ct_models = ContentType.objects.filter(model__in=args)
    for ct_model in ct_models:
        model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:3]
        products.extend(model_products)
    if with_respect_to:
        ct_models = ContentType.objects.filter(model=with_respect_to)

        if ct_models.exists():
            if with_respect_to in args:
                return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to),
                              reverse=True
                              )
    return products


class LatestProducts:
    objects = LatestProductsManager()


# ************
# 1 Category
# 2 Product
# 3 CartProduct
# 4 cart
# 5 order
# ************
# 6 Customer
# 7 Specification
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Назименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="цена")

    def __str__(self):
        return self.title


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=255, verbose_name='Разрвешение эерана')
    accum_volume = models.CharField(max_length=255, verbose_name='Обьем экрана')
    ram = models.CharField(max_length=255, verbose_name='Оперативная памяать')
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name="Максимальный обьем встравмой памяти")
    main_cam_mp = models.CharField(max_length=255, verbose_name='Главный камера')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронталная камера')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


####
class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    video = models.CharField(max_length=255, verbose_name='видеокарта')
    tine_without_charge = models.CharField(max_length=255, verbose_name='Время работу аккуьулятора')

    def __str__(self):
        return "{} :{}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    dty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="обЩая цена")

    def __str__(self):
        return 'Продукт: {} (для корзина)'.format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=8)
    final_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = models.CharField(max_length=28, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Specifications(models.Model):
    content_tyre = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name='имя товара для харектеристик')

    def __str__(self):
        return "Харектеристики для товара: {}".format(self.name)


class someModel(models.Model):
    image = models.ImageField()

    def __str__(self):
        return str(self.id)
##


# Create your models here.
