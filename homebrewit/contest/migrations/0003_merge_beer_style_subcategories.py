# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for subcategory in orm.BeerStyleSubcategory.objects.all():
            parent_style = subcategory.beer_style

            new_style = orm.BeerStyle(name=subcategory.name, 
                    contest_year=parent_style.contest_year, 
                    judge=parent_style.judge, 
                    parent_style=parent_style)
            new_style.save()

            for entry in orm.Entry.objects.filter(style_subcategory=subcategory):
                entry.style = new_style
                entry.save()


    def backwards(self, orm):
        "Write your backwards methods here."


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
        u'contest.beerstyle': {
            'Meta': {'object_name': 'BeerStyle'},
            'contest_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.ContestYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'null': 'True', 'to': u"orm['contest.BeerStyle']"})
        },
        u'contest.beerstylesubcategory': {
            'Meta': {'object_name': 'BeerStyleSubcategory'},
            'beer_style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BeerStyle']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contest.bjcpjudgingresult': {
            'Meta': {'object_name': 'BJCPJudgingResult'},
            'acetaldehyde': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appearance_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aroma_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'astringent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diacetyl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flavor_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'grassy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intangibles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'judge_bjcp_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'light_struck': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metallic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mouthfeel_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'mouthfeel_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'musty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'overall_impression_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'overall_impression_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'oxidized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phenolic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'solvent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sour_acidic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stylistic_accuracy': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sulfur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'technical_merit': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'vegetal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yeasty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contest.contestyear': {
            'Meta': {'ordering': "('-contest_year',)", 'object_name': 'ContestYear'},
            'allowing_entries': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contest_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2014', 'unique': 'True', 'db_index': 'True'}),
            'finished_judging': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prize_description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'})
        },
        u'contest.entry': {
            'Meta': {'ordering': "('style', 'score')", 'object_name': 'Entry'},
            'beer_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bjcp_judging_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BJCPJudgingResult']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailed_entry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'received_entry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_ingredients': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BeerStyle']"}),
            'style_subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BeerStyleSubcategory']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contest.judgingresult': {
            'Meta': {'object_name': 'JudgingResult'},
            'appearance_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aroma_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.Entry']"}),
            'flavor_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intangibles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'judge_bjcp_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mouthfeel_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'mouthfeel_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'overall_impression_description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'overall_impression_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'stylistic_accuracy': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'technical_merit': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['contest']
    symmetrical = True
