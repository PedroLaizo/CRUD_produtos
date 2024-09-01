from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    codigo_produto = models.CharField(max_length=50, unique=True)
    descricao_produto = models.TextField()
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_produto
