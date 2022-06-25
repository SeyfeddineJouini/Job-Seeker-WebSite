from django.db import models


class categories(models.Model):
    category_type = models.CharField(max_length=200, verbose_name="La catégorie/الفئة")

    class Meta:
        db_table = "categorie"

    def __str__(self):
        return "%s" % (self.category_type)
class files(models.Model):
    title=models.CharField(max_length=100,verbose_name="titre/العنوان")
    pdf = models.FileField(upload_to='documents/',verbose_name="fichier/ملف")

    class Meta:
        db_table = "document"
    def __str__(self):
        return "%s" % (self.title)
    def delete(self,*args,**kwargs):
        self.pdf.delete()
        super().delete(*args,**kwargs)
class programme(models.Model):
    title=models.CharField(max_length=100,verbose_name="titre/العنوان")
    prog=models.FileField(upload_to='programmes/',verbose_name="programmede formation/برنامج التكوين")
    class Meta:
        db_table = "programm"
    def __str__(self):
        return "%s" % (self.title)
    def delete(self,*args,**kwargs):
        self.prog.delete()
        super().delete(*args,**kwargs)

class formations(models.Model):
    Nom_for = models.CharField(max_length=200, verbose_name="la formation/مجال التكوين")
    start = models.CharField(max_length=100, verbose_name="session 1/الدورة1")
    end = models.CharField(max_length=100, verbose_name="session 2/الدورة2")
    middle=models.CharField(max_length=100,verbose_name="session3/الدورة3")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="prix/الثمن")
    categ = models.ForeignKey(categories, on_delete=models.CASCADE, default=None,verbose_name="catégorie/الفئة")
    doc = models.ForeignKey(files, on_delete=models.CASCADE, default=None,verbose_name="fiche d'inscripton/إستمارة التسجيل")
    prog = models.ForeignKey(programme, on_delete=models.CASCADE, default=None,verbose_name="برنامج التكوين/programme devformation")
    actif=models.BooleanField(default=False)

    class Meta:
        db_table = "forma"

    def __str__(self):
        return "%s" % (self.Nom_for)




class seeker(models.Model):
    nom=models.CharField(max_length=200,verbose_name="nom et prénom/الاسم و اللقب ")
    num_tel=models.IntegerField(verbose_name="Téléphone/الهاتف")
    adress=models.EmailField(verbose_name="adresse mail/البريد الإلكتروني ",max_length=200)
    f=models.ForeignKey(formations,on_delete=models.CASCADE,default=None,verbose_name="formation/مجال التكوين")
    a= models.CharField(max_length=200,verbose_name="administration/الادارة")
    class Meta:
        db_table="seeker"
class choices(models.Model):
    choice=models.CharField(max_length=10,verbose_name="mois")
    def __str__(self):
        return "%s" % (self.choice)
    class Meta:
        db_table="choices"

class choiceans(models.Model):
    choice=models.CharField(max_length=10)
    def __str__(self):
        return "%s" % (self.choice)
    class Meta:
        db_table="choiceannee"

class month(models.Model):  
    mois=models.ForeignKey(choices ,on_delete=models.CASCADE,default=None,verbose_name="mois")
    annee=models.ForeignKey(choiceans ,on_delete=models.CASCADE,default=None,verbose_name="année")
    def __str__(self):
        return "%s" % (self.mois)
    class Meta:
        db_table="month"

