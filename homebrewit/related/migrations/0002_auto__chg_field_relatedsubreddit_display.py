# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RelatedSubreddit.display'
        db.alter_column(u'related_relatedsubreddit', 'display', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'RelatedSubreddit.display'
        db.alter_column(u'related_relatedsubreddit', 'display', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'related.relatedsubreddit': {
            'Meta': {'ordering': "('display',)", 'object_name': 'RelatedSubreddit'},
            'display': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['related']