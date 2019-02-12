from django.db import models
def content_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Champs(models.Model):
    champ_name = models.CharField(max_length=100)
    champ_image = models.ImageField(upload_to=content_path)


