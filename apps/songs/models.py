from django.db import models
from cloudinary.models import CloudinaryField
from apps.genre.models import Genre
# Create your models here.
class Song(models.Model):
    # class Meta(object):
    #     db_table='songs'
        name= models.CharField(
            'Name', blank= False, null=False, max_length=50, db_index=True
        )
        description = models.TextField(
            'description', blank=False, null= False, max_length=200
        )
        rating= models.IntegerField(
            'rating', blank=False,null=False
        )
        songs_duration= models.IntegerField(
            'duration',blank=False,null=False,default=45
        )
        genre_id = models.ForeignKey(
            Genre,on_delete=models.CASCADE
        )
        thumbail=CloudinaryField(
            blank=True,null=True
        )
        music=CloudinaryField(
           'music', resource_type='raw'
        )
        
        created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
        )
        updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
        )



