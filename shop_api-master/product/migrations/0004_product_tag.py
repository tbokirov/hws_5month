# Generated by Django 4.2.2 on 2023-06-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_tag_alter_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='product.tag'),
        ),
    ]