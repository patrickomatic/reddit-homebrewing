# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContestYear'
        db.create_table(u'contest_contestyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contest_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2014, unique=True, db_index=True)),
            ('allowing_entries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('finished_judging', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prize_description', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
        ))
        db.send_create_signal(u'contest', ['ContestYear'])

        # Adding model 'BeerStyle'
        db.create_table(u'contest_beerstyle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contest_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.ContestYear'])),
            ('judge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'contest', ['BeerStyle'])

        # Adding model 'BeerStyleSubcategory'
        db.create_table(u'contest_beerstylesubcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('beer_style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.BeerStyle'])),
        ))
        db.send_create_signal(u'contest', ['BeerStyleSubcategory'])

        # Adding model 'Entry'
        db.create_table(u'contest_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.BeerStyle'])),
            ('style_subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.BeerStyleSubcategory'], null=True, blank=True)),
            ('bjcp_judging_result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.BJCPJudgingResult'], null=True, blank=True)),
            ('beer_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('special_ingredients', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('winner', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rank', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True, null=True, blank=True)),
            ('score', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('mailed_entry', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('received_entry', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'contest', ['Entry'])

        # Adding model 'BJCPJudgingResult'
        db.create_table(u'contest_bjcpjudgingresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('judge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('judge_bjcp_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acetaldehyde', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alcoholic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('astringent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diacetyl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dms', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('grassy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('light_struck', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('metallic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('musty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oxidized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phenolic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('solvent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sour_acidic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sulfur', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vegetal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('yeasty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('aroma_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('aroma_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('appearance_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('appearance_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('flavor_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('flavor_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mouthfeel_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('mouthfeel_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('overall_impression_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('overall_impression_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('stylistic_accuracy', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('technical_merit', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('intangibles', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'contest', ['BJCPJudgingResult'])

        # Adding model 'JudgingResult'
        db.create_table(u'contest_judgingresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('judge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('judge_bjcp_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.Entry'])),
            ('aroma_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('aroma_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('appearance_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('appearance_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('flavor_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('flavor_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mouthfeel_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('mouthfeel_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('overall_impression_description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('overall_impression_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('stylistic_accuracy', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('technical_merit', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('intangibles', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'contest', ['JudgingResult'])


    def backwards(self, orm):
        # Deleting model 'ContestYear'
        db.delete_table(u'contest_contestyear')

        # Deleting model 'BeerStyle'
        db.delete_table(u'contest_beerstyle')

        # Deleting model 'BeerStyleSubcategory'
        db.delete_table(u'contest_beerstylesubcategory')

        # Deleting model 'Entry'
        db.delete_table(u'contest_entry')

        # Deleting model 'BJCPJudgingResult'
        db.delete_table(u'contest_bjcpjudgingresult')

        # Deleting model 'JudgingResult'
        db.delete_table(u'contest_judgingresult')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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