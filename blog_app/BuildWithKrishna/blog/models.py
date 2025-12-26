from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    post_content = models.CharField(max_length=5000)
    post_image = models.ImageField(upload_to="post/images")
    post_time = models.DateTimeField()
    post_author = models.CharField(max_length=100,default="unknown User")

    def __str__(self):
        return self.post_title

