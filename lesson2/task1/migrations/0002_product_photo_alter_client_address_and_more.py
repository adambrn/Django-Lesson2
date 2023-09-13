# Generated by Django 4.2.4 on 2023-09-13 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
        migrations.AlterField(
            model_name="client",
            name="address",
            field=models.TextField(verbose_name="Адрес клиента"),
        ),
        migrations.AlterField(
            model_name="client",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Email клиента"),
        ),
        migrations.AlterField(
            model_name="client",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя клиента"),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.CharField(
                max_length=20, verbose_name="Номер телефона клиента"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="registration_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата регистрации клиента"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="task1.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(verbose_name="Дата оформления заказа"),
        ),
        migrations.AlterField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                to="task1.product", verbose_name="Товары в заказе"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Общая стоимость заказа"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="added_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата добавления товара"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="Описание товара"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название товара"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Цена товара"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(
                verbose_name="Количество товара на складе"
            ),
        ),
    ]