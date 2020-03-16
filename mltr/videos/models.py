from django.db import models
from django.urls import reverse
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50, blank=True, default=None)
    description = models.CharField(max_length=500, blank=True, null=True, default=None)
    video = models.FileField(upload_to='videos/', null=True, blank=False, default=None)
    # thumbnail = models.ImageField(upload_to='images', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"video_id": self.id}) #f"/videos/{self.id}"