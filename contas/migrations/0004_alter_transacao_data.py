# Generated by Django 4.1.7 on 2023-03-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_alter_transacao_options_alter_transacao_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
