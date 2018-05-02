from django.db import models


# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=50)
	people = models.IntegerField(blank=False,null=True)
	date = models.DateTimeField(max_length=12,null=True,blank=False)
	message = models.CharField(max_length=5000,null=True,blank=False)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		managed = True
		db_table = "website_contact_database"