from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria de productos'
        verbose_name_plural = 'Categorias de productos'

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey(
        'CategoryModel',
        on_delete=models.CASCADE, # CASCADA: si eliminamos una categoría, se elimina el producto de esa categoría.
        db_column='category_id', # Nombre de la columna en la BD, 'category', es solo el nombre de la relación.
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'