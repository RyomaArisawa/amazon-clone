# Generated by Django 3.1.5 on 2021-02-06 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0002_shoppingcart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': 'ショッピングカート', 'verbose_name_plural': 'ショッピングカート'},
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='数量')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='amazon.shoppingcart', verbose_name='ショッピングカート')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amazon.product', verbose_name='商品')),
            ],
            options={
                'verbose_name': 'ショッピングカートアイテム',
                'verbose_name_plural': 'ショッピングカートアイテム',
            },
        ),
    ]
