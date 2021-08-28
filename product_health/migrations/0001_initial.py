# Generated by Django 3.2.6 on 2021-08-27 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20210805_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('viewed_on', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductyActivity', to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Product Activity',
            },
        ),
    ]
