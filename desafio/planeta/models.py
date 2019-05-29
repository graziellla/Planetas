from django.db import models

class Posicao(models.Model):
    nome = models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.nome


class Composicao(models.Model):
    descricao = models.CharField(max_length=200,verbose_name="Composição Atmosferica")

    def __str__(self):
        return self.descricao




class Planeta(models.Model):
    imagem = models.FileField(upload_to='fotos/')
    nome = models.CharField(max_length=120)
    rotacao = models.TimeField()
    Translacao = models.PositiveIntegerField()
    Luas = models.PositiveIntegerField()
    fk_posicao = models.ForeignKey("Posicao",on_delete= models.PROTECT)
    fk_composicao = models.ManyToManyField(Composicao)



    def __str__(self):
        return self.nome



