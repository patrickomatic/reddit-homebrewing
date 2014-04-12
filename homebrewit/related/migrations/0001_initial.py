# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RelatedSubreddit'
        db.create_table(u'related_relatedsubreddit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'related', ['RelatedSubreddit'])


    def backwards(self, orm):
        # Deleting model 'RelatedSubreddit'
        db.delete_table(u'related_relatedsubreddit')


    models = {
        u'related.relatedsubreddit': {
            'Meta': {'ordering': "('display',)", 'object_name': 'RelatedSubreddit'},
            'display': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['related']