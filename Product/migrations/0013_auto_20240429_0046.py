# Generated by Django 2.2.28 on 2024-04-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category', '-created')},
        ),
    ]
