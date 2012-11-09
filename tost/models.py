# -*- coding: utf-8 -*-
from django.db import models

class FirstClass(models.Model):
	name = models.CharField(max_length = '30')
	home = models.CharField(max_length = '30')
	work = models.TextField(u'текст')

	def __unicode__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = u'Первый класс'
		verbose_name_plural = u'Первый класс'
			

		
		
