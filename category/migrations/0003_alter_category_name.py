from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
