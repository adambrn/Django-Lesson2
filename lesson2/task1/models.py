from django.db import models

class Client(models.Model):
   name = models.CharField(max_length=255, verbose_name='Имя клиента')
   email = models.EmailField(verbose_name='Email клиента')
   phone_number = models.CharField(max_length=20, verbose_name='Номер телефона клиента')
   address = models.TextField(verbose_name='Адрес клиента')
   registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации клиента')
   
   class Meta:
       verbose_name = 'Клиент'
       verbose_name_plural = 'Клиенты'
   
   def __str__(self):
       return self.name

class Product(models.Model):
   name = models.CharField(max_length=255, verbose_name='Название товара')
   description = models.TextField(verbose_name='Описание товара')
   price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
   quantity = models.PositiveIntegerField(verbose_name='Количество товара на складе')
   added_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')

   def __str__(self):
       return self.name
   
   class Meta:
       verbose_name = 'Товар'
       verbose_name_plural = 'Товары'

class Order(models.Model):
   client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
   products = models.ManyToManyField(Product, verbose_name='Товары в заказе')
   total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая стоимость заказа')
   order_date = models.DateTimeField( verbose_name='Дата оформления заказа')

   class Meta:
       verbose_name = 'Заказ'
       verbose_name_plural = 'Заказы'

   def __str__(self):
       return f"Заказ № {self.pk} от {self.client.name}"
