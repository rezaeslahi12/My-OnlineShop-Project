from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    P_name = models.CharField(max_length=100,null=True)
    discrption=models.TextField(null=True)
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to ='%Y/%m/%d',null=True,blank=True)
    like = models.ManyToManyField(User,related_name="ProductLike",blank=True)
    def __str__ (self):
        return self.P_name
    def getsnippet(self):
        return self.discrption[0:30] + '...'
