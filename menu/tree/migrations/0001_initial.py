# Generated by Django 3.2.18 on 2024-03-06 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название меню.', max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(help_text=('Укажите адресс меню.', 'Допустимые символы 0-9 A-Z a-z - _'), max_length=200, unique=True, verbose_name='Адресс меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите человекочитаемое имя секции меню.', max_length=200, verbose_name='Название')),
                ('adress', models.CharField(help_text=('Укажите адресс секции в формате', '`namespace:name`. Без кавычек.'), max_length=200, verbose_name='Адресс секции')),
                ('menu', models.ForeignKey(help_text='Укажите к какому меню относится. Выбранная верхняя секция должна относится к выбраному меню!', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='tree.menu', verbose_name='Меню секции')),
                ('top_section', models.ForeignKey(blank=True, default=None, help_text='Укажите родительскую секцию. Если родительская секция не будет указана - секция появится в корне меню.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='down_sections', to='tree.section', verbose_name='Родительская секция')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секции',
            },
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(fields=('name', 'menu'), name='name_menu'),
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(fields=('adress', 'menu'), name='adress_menu'),
        ),
    ]