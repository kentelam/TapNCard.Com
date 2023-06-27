                                                                  
from django.db import models

# Create your models here.

class Tapncard(models.Model):

   logo = models.ImageField( upload_to='images/site',null=False, blank=False, default='media/images/profile/defaultBizman_5lfB6OA.jpg')
   default_picture = models.ImageField( upload_to='images/site',null=False ,blank=False, default='media/images/site/defaultBizman_5lfB6OA.jpg')
   ad_picture1 = models.ImageField( upload_to='images/site',null=False ,blank=False, default='media/images/site/defaultBizman_5lfB6OA.jpg')
   ad_picture2 = models.ImageField( upload_to='images/site',null=False ,blank=False, default='media/images/site/defaultBizman_5lfB6OA.jpg')
   ad_picture3 = models.ImageField( upload_to='images/site',null=False ,blank=False, default='media/images/site/defaultBizman_5lfB6OA.jpg')

   def __str__(self):

     return f"{self.logo}, {self.ad_picture1}, {self.ad_picture2}, {self.ad_picture3}"
