# Generated by Django 4.1.7 on 2023-03-29 06:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total amount')),
                ('payment_type', models.CharField(default='By Cash', max_length=25, verbose_name='Payment Type')),
                ('orders', models.ManyToManyField(to='order.order', verbose_name='orders')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.table', verbose_name='table')),
            ],
            options={
                'verbose_name': 'Bill',
                'verbose_name_plural': 'Bills',
                'ordering': ('-created_at',),
            },
        ),
    ]