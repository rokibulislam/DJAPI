from django.db import models
import json  #python's library
# Create your models here.
#
#
# class PersonQuerySet(models.QuerySet):

#     def serialize(self):   #called when list of data is needed
#         response_list = list( self.values("id","name","email","mobile") )
#         return json.dumps(response_list)


# class PersonManager(models.Manager):
#     def get_queryset(self):
#         return PersonQuerySet(self.model,using=self._db)   #connecting model manager with model queryset

class PublishQuerySet(models.QuerySet):
	def active(self):
		return self.filter(active=True)

	def serialize(self):
		response_list = list(self.values("id","title","content","active"))
		return json.dumps(response_list)

class PublishedManager(models.Manager):
	def get_queryset(self):
		return PublishQuerySet(self.model, using=self._db)
		# return super(PublishedManager,self).get_queryset().filter(active=True)
	def serialize(self):
		return self.get_queryset().serialize()

	def active(self):
		return self.get_queryset().serialize()


class PersonQuerySet(models.QuerySet):
	def serialize(self):
		response_list = list(self.values("id","name","email","mobile"))
		return json.dumps(response_list)

class PersonManager(models.Manager):

	def get_queryset(self):
		return PersonQuerySet(self.model,using=self._db)

	def serialize(self):
		return self.get_queryset().serialize()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

class Person(models.Model):
	name   = models.CharField(max_length=254)
	email  = models.CharField(max_length=254,unique=True)
	mobile = models.CharField(max_length=11)

	def __str__(self):
		return self.name

	# def serialize(self):   #called for a single instance
 #        data = {
 #            "id" : self.id,
 #            "name" : self.name,
 #            "email" : self.email,
 #            "mobile" : self.mobile
 #        }
 #        response = json.dumps(data) #need python's json library to convert python's dictionary to json
 #        return response