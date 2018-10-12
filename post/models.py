from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import os
from django.utils import timezone
import markdown
from PIL import Image

# class PostManager(models.Manager):
#     author_id = request.user.id
#     def current(self,author_id):
#         return author.posts.all()

def upload_image(instance,filename):
    """
    builds the media path for where it will store the post image
    """
    file_extention = filename.split('.')[1]
    start_file = filename.split('.')[0]
    time = timezone.now().strftime('%Y-%m-%d')
    if len(start_file) < 5:
        generic_file_name = start_file + time
    else:
        generic_file_name = start_file[:5] + time
    filename = generic_file_name + '.' + file_extention
    return os.path.join('image','user_{0}','{1}').format(instance.author.id,filename)

class Post(models.Model):
    title = models.CharField(max_length=255,default="")
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    image = models.ImageField(upload_to=upload_image,blank=True,null=True)
    text = models.TextField()
    text_html = models.TextField(editable=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True,null=True)


    def save(self,*args,**kwargs):
        self.text_html = markdown.markdown(self.text)
        super().save(*args,**kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 500 or img.width>700:
                output_size = (500,700)
                img.thumbnail(output_size)
                img.save(self.image.path)

    @property
    def get_image_url(self):
        if self.image:
            return '/media/{}'.format(self.image)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.text[:5]


    def get_absolute_url(self):
        return reverse ('post:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering = ['-date_posted']
