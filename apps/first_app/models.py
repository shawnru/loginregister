# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

class User_manager(models.Manager):
    def register(self, postdata):
        error = []
        response_to_views = {}
        if postdata:
            print postdata.get('first_name')
            print postdata.get('password')
            print 'hello'
            print len(postdata.get('password'))
            if len(postdata['first_name']) < 2 and not re.search(r'^\w+$', postdata['first_name']):
                error.append('Please use two or more letters to write your first name.')
                response_to_views['errors'] = error
            elif len(postdata['last_name']) < 2 and not re.search(r'^\w+$', postdata['last_name']):
                error.append('Please use two or more letters to write your last name.')
                response_to_views['errors'] = error
            elif not re.search(r'^\w+@\w+\.\w+$', postdata['email']):
                error.append('Please use a correct email address.')
                response_to_views['errors'] = error
            elif len(postdata.get('password')) < 8 and postdata.get('password') != postdata.get('confirmpw'):
                error.append('Please correct your password fields. You must use at least 8 characters and both passwords must match.')
                response_to_views['errors'] = error
            else:
                self.create(email=postdata['email'],password=postdata['password'])
        return response_to_views

    def signin(self, postdata):
        if postdata:
            if User.objects.filter(email=postdata['email'], password=postdata['password']):
                return True
        else:
            return False

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='password')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = User_manager()
