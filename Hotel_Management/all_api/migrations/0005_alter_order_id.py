# Generated by Django 4.1.1 on 2022-10-10 04:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('all_api', '0004_alter_bill_id_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
