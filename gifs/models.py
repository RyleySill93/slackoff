from django.db import models


# Create your models here.
class Image(models.Model):
    s3_key = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    width = models.IntegerField()
    height = models.IntegerField()
    is_base_gif = models.BooleanField(default=False)


class ImageData(models.Model):
    type = models.CharField(max_length=1000)  # should get rid of this or the one on the image or both
    background_image_path = models.CharField(max_length=10000)
    foreground_image_path = models.CharField(max_length=10000, null=True, blank=True)


class TrackedElement(models.Model):
    index = models.IntegerField()  # should be able to delete this after everything is migrated
    image_data = models.ForeignKey(ImageData, on_delete=models.CASCADE)


class FrameData(models.Model):
    image_data = models.ForeignKey(ImageData, on_delete=models.CASCADE)
    index = models.IntegerField()
    has_foreground = models.BooleanField(default=False)


class TrackedElementPosition(models.Model):
    frame_data = models.ForeignKey(FrameData, on_delete=models.CASCADE, null=True, blank=True)
    tracked_element = models.ForeignKey(TrackedElement, null=True, blank=True, on_delete=models.CASCADE)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)
    z = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    rotation = models.IntegerField(null=True, blank=True)
    brightness = models.IntegerField(null=True, blank=True)


class TrackedElementAdjustment(TrackedElementPosition):

    class Meta:
        proxy = True
