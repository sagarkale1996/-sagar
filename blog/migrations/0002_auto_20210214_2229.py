# Generated by Django 3.1.6 on 2021-02-14 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.product')),
            ],
        ),
        migrations.DeleteModel(
            name='sagar',
        ),
    ]