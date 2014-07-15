# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ContestYear.prize_description'
        db.alter_column(u'contest_contestyear', 'prize_description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'JudgingResult.mouthfeel_description'
        db.alter_column(u'contest_judgingresult', 'mouthfeel_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'JudgingResult.overall_impression_description'
        db.alter_column(u'contest_judgingresult', 'overall_impression_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'JudgingResult.flavor_description'
        db.alter_column(u'contest_judgingresult', 'flavor_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'JudgingResult.judge_bjcp_id'
        db.alter_column(u'contest_judgingresult', 'judge_bjcp_id', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'JudgingResult.aroma_description'
        db.alter_column(u'contest_judgingresult', 'aroma_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'JudgingResult.appearance_description'
        db.alter_column(u'contest_judgingresult', 'appearance_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BeerStyle.name'
        db.alter_column(u'contest_beerstyle', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BJCPJudgingResult.flavor_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'flavor_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BJCPJudgingResult.aroma_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'aroma_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BJCPJudgingResult.judge_bjcp_id'
        db.alter_column(u'contest_bjcpjudgingresult', 'judge_bjcp_id', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'BJCPJudgingResult.mouthfeel_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'mouthfeel_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BJCPJudgingResult.overall_impression_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'overall_impression_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BJCPJudgingResult.appearance_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'appearance_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Entry.special_ingredients'
        db.alter_column(u'contest_entry', 'special_ingredients', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Entry.beer_name'
        db.alter_column(u'contest_entry', 'beer_name', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'ContestYear.prize_description'
        db.alter_column(u'contest_contestyear', 'prize_description', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True))

        # Changing field 'JudgingResult.mouthfeel_description'
        db.alter_column(u'contest_judgingresult', 'mouthfeel_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'JudgingResult.overall_impression_description'
        db.alter_column(u'contest_judgingresult', 'overall_impression_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'JudgingResult.flavor_description'
        db.alter_column(u'contest_judgingresult', 'flavor_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'JudgingResult.judge_bjcp_id'
        db.alter_column(u'contest_judgingresult', 'judge_bjcp_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'JudgingResult.aroma_description'
        db.alter_column(u'contest_judgingresult', 'aroma_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'JudgingResult.appearance_description'
        db.alter_column(u'contest_judgingresult', 'appearance_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'BeerStyle.name'
        db.alter_column(u'contest_beerstyle', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'BJCPJudgingResult.flavor_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'flavor_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'BJCPJudgingResult.aroma_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'aroma_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'BJCPJudgingResult.judge_bjcp_id'
        db.alter_column(u'contest_bjcpjudgingresult', 'judge_bjcp_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'BJCPJudgingResult.mouthfeel_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'mouthfeel_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'BJCPJudgingResult.overall_impression_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'overall_impression_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'BJCPJudgingResult.appearance_description'
        db.alter_column(u'contest_bjcpjudgingresult', 'appearance_description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'Entry.special_ingredients'
        db.alter_column(u'contest_entry', 'special_ingredients', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True))

        # Changing field 'Entry.beer_name'
        db.alter_column(u'contest_entry', 'beer_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

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
        u'contest.beerdetail': {
            'Meta': {'object_name': 'BeerDetail'},
            'beer_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'beer_details'", 'to': u"orm['contest.BeerStyle']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'must_specify': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'contest.beerdetailchoice': {
            'Meta': {'object_name': 'BeerDetailChoice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple_choice_beer_detail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': u"orm['contest.BeerDetail']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'contest.beerstyle': {
            'Meta': {'object_name': 'BeerStyle'},
            'contest_year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'beer_styles'", 'to': u"orm['contest.ContestYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'parent_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'null': 'True', 'to': u"orm['contest.BeerStyle']"})
        },
        u'contest.bjcpjudgingresult': {
            'Meta': {'object_name': 'BJCPJudgingResult'},
            'acetaldehyde': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appearance_description': ('django.db.models.fields.TextField', [], {}),
            'appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aroma_description': ('django.db.models.fields.TextField', [], {}),
            'aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'astringent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diacetyl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flavor_description': ('django.db.models.fields.TextField', [], {}),
            'flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'grassy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intangibles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'judge_bjcp_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'light_struck': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metallic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mouthfeel_description': ('django.db.models.fields.TextField', [], {}),
            'mouthfeel_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'musty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'overall_impression_description': ('django.db.models.fields.TextField', [], {}),
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
            'prize_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'contest.entry': {
            'Meta': {'ordering': "('style', 'score')", 'object_name': 'Entry'},
            'beer_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bjcp_judging_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BJCPJudgingResult']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailed_entry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'received_entry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_ingredients': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BeerStyle']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contest.entrybeerdetail': {
            'Meta': {'object_name': 'EntryBeerDetail'},
            'beer_detail': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.BeerDetail']"}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_beer_details'", 'to': u"orm['contest.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'contest.judgingresult': {
            'Meta': {'object_name': 'JudgingResult'},
            'appearance_description': ('django.db.models.fields.TextField', [], {}),
            'appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aroma_description': ('django.db.models.fields.TextField', [], {}),
            'aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contest.Entry']"}),
            'flavor_description': ('django.db.models.fields.TextField', [], {}),
            'flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intangibles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'judge_bjcp_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mouthfeel_description': ('django.db.models.fields.TextField', [], {}),
            'mouthfeel_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'overall_impression_description': ('django.db.models.fields.TextField', [], {}),
            'overall_impression_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'stylistic_accuracy': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'technical_merit': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['contest']