from django.db import models

# Create your models here.
class Blogpost(models.Model):
	post_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=30)
	head0 = models.CharField(max_length=40, default="")
	chead0 = models.CharField(max_length=4000, default="") #content of heading 0
	head1 = models.CharField(max_length=40, default="")
	chead1 = models.CharField(max_length=4000, default="")
	head2 = models.CharField(max_length=40, default="")
	chead2 = models.CharField(max_length=4000, default="")
	pub_date = models.DateField()
	thumbnail = models.ImageField(upload_to="blog/images", default="")

	def __str__(self):
		return self.title