# Generated by Django 3.2.6 on 2021-08-31 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210805_1650'),
        ('product_health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productactivity',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producty_activity', to='products.product'),
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Product History',
            },
        ),
    ]
