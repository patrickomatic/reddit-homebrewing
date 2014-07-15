# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ExperienceLevel.css_img_url'
        db.alter_column(u'experiencelevel_experiencelevel', 'css_img_url', self.gf('django.db.models.fields.FilePathField')(path='/Users/patrick/reddit-homebrewing/homebrewit/static/images/icons/experience_levels', max_length=100))

        # Changing field 'ExperienceLevel.img_url'
        db.alter_column(u'experiencelevel_experiencelevel', 'img_url', self.gf('django.db.models.fields.FilePathField')(path='/Users/patrick/reddit-homebrewing/homebrewit/static/images/icons/experience_levels', max_length=100))

        # Changing field 'ExperienceLevel.name'
        db.alter_column(u'experiencelevel_experiencelevel', 'name', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'ExperienceLevel.css_img_url'
        db.alter_column(u'experiencelevel_experiencelevel', 'css_img_url', self.gf('django.db.models.fields.FilePathField')(path='/Users/patrick/reddit-homebrewing/media/images/icons/experience_levels', max_length=100))

        # Changing field 'ExperienceLevel.img_url'
        db.alter_column(u'experiencelevel_experiencelevel', 'img_url', self.gf('django.db.models.fields.FilePathField')(path='/Users/patrick/reddit-homebrewing/media/images/icons/experience_levels', max_length=100))

        # Changing field 'ExperienceLevel.name'
        db.alter_column(u'experiencelevel_experiencelevel', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'experiencelevel.experiencelevel': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ExperienceLevel'},
            'css_img_url': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/patrick/reddit-homebrewing/homebrewit/static/images/icons/experience_levels'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/patrick/reddit-homebrewing/homebrewit/static/images/icons/experience_levels'", 'max_length': '100'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'experiencelevel.userexperiencelevel': {
            'Meta': {'object_name': 'UserExperienceLevel'},
            'experience_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['experiencelevel.ExperienceLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['experiencelevel']