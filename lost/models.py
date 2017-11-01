from django.db import models

class Item(models.Model):
    it_name = models.CharField(max_length = 64)
    it_id = models.IntegerField(primary_key=True)
    it_url = models.CharField(max_length = 128, null=True)
    it_title = models.CharField(max_length = 128, null=True)
    it_get_date = models.DateField(null=True)
    it_take_place = models.CharField(max_length = 128, null=True)
    it_contact = models.CharField(max_length = 32, null=True)
    it_cate = models.CharField(max_length = 16, null=True)
    it_get_position = models.CharField(max_length = 128, null=True)
    it_get_place = models.CharField(max_length = 128, null=True)
    it_get_thing = models.TextField(null=True)
    it_status = models.CharField(max_length = 32, null=True)
    it_code = models.CharField(max_length = 16, null=True)
    it_image_url = models.CharField(max_length = 512, null=True)
    it_drive_num = models.CharField(max_length = 32, null=True)
    it_get_nm = models.CharField(max_length = 32, null=True)
    words = models.CharField(max_length = 4096, null=True)

    def __str__(self):
        return "[ %d ] %s" % (self.it_id, self.it_name)
    def __repr__(self):
        return "[ %d ] %s" % (self.it_id, self.it_name)
    def __unicode__(self):
        return "[ %d ] %s" % (self.it_id, self.it_name)
