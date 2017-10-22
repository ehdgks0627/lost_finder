from django.db import models

class Item(models.Model):
    it_name = models.CharField(max_length = 64)
    it_id = models.IntegerField(primary_key=True)
    it_url = models.CharField(max_length = 128)
    it_title = models.CharField(max_length = 128)
    it_get_date = models.DateField()
    it_take_place = models.CharField(max_length = 128)
    it_contact = models.CharField(max_length = 32)
    it_cate = models.CharField(max_length = 16)
    it_get_position = models.CharField(max_length = 128)
    it_get_place = models.CharField(max_length = 128)
    it_get_thing = models.TextField()
    it_status = models.CharField(max_length = 32)
    it_code = models.CharField(max_length = 16)
    it_image_url = models.CharField(max_length = 512)
    it_drive_num = models.CharField(max_length = 32)
    it_get_nm = models.CharField(max_length = 32)

    def __init__(self):
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass
