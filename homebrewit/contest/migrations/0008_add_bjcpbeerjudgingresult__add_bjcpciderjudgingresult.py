# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column(u'contest_bjcpjudgingresult', 'acetaldehyde', 'old_acetaldehyde')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_acetaldehyde', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'alcoholic', 'old_alcoholic')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_alcoholic', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'astringent', 'old_astringent')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_astringent', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'diacetyl', 'old_diacetyl')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_diacetyl', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'dms', 'old_dms')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_dms', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'estery', 'old_estery')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_estery', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'grassy', 'old_grassy')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_grassy', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'light_struck', 'old_light_struck')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_light_struck', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'metallic', 'old_metallic')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_metallic', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'musty', 'old_musty')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_musty', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'oxidized', 'old_oxidized') 
        db.alter_column(u'contest_bjcpjudgingresult', 'old_oxidized', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'phenolic', 'old_phenolic')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_phenolic', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'solvent', 'old_solvent')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_solvent', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'sour_acidic', 'old_sour_acidic')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_sour_acidic', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'sulfur', 'old_sulfur')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_sulfur', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'vegetal', 'old_vegetal')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_vegetal', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'yeasty', 'old_yeasty')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_yeasty', self.gf('django.db.models.fields.BooleanField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'aroma_description', 'old_aroma_description')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_aroma_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'aroma_score', 'old_aroma_score')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_aroma_score', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'appearance_description', 'old_appearance_description')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_appearance_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'appearance_score', 'old_appearance_score')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_appearance_score', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'flavor_description', 'old_flavor_description')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_flavor_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'flavor_score', 'old_flavor_score')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_flavor_score', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'mouthfeel_description', 'old_mouthfeel_description')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'mouthfeel_score', 'old_mouthfeel_score')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_score', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'overall_impression_description', 'old_overall_impression_description')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_overall_impression_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))
        db.rename_column(u'contest_bjcpjudgingresult', 'overall_impression_score', 'old_overall_impression_score')
        db.alter_column(u'contest_bjcpjudgingresult', 'old_overall_impression_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Adding model 'BJCPBeerJudgingResult'
        db.create_table(u'contest_bjcpbeerjudgingresult', (
            (u'bjcpjudgingresult_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contest.BJCPJudgingResult'], unique=True, primary_key=True)),
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
            ('aroma_description', self.gf('django.db.models.fields.TextField')()),
            ('aroma_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('appearance_description', self.gf('django.db.models.fields.TextField')()),
            ('appearance_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('flavor_description', self.gf('django.db.models.fields.TextField')()),
            ('flavor_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mouthfeel_description', self.gf('django.db.models.fields.TextField')()),
            ('mouthfeel_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('overall_impression_description', self.gf('django.db.models.fields.TextField')()),
            ('overall_impression_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'contest', ['BJCPBeerJudgingResult'])

        # Adding model 'BJCPCiderJudgingResult'
        db.create_table(u'contest_bjcpciderjudgingresult', (
            (u'bjcpjudgingresult_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contest.BJCPJudgingResult'], unique=True, primary_key=True)),
            ('acetaldehyde', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('acetified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('acidic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alcoholic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('astringent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diacetyl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('farmyard', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fruity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('metallic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mousy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oaky', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oily_ropy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oxidized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phenolic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('spicy_smoky', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sulfite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sweet', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vegetal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('aroma_description', self.gf('django.db.models.fields.TextField')()),
            ('aroma_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('appearance_description', self.gf('django.db.models.fields.TextField')()),
            ('appearance_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('flavor_description', self.gf('django.db.models.fields.TextField')()),
            ('flavor_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('overall_impression_description', self.gf('django.db.models.fields.TextField')()),
            ('overall_impression_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'contest', ['BJCPCiderJudgingResult'])

    def backwards(self, orm):
        # Deleting model 'BJCPBeerJudgingResult'
        db.delete_table(u'contest_bjcpbeerjudgingresult')

        # Deleting model 'BJCPCiderJudgingResult'
        db.delete_table(u'contest_bjcpciderjudgingresult')

        db.rename_column(u'contest_bjcpjudgingresult', 'old_acetaldehyde', 'acetaldehyde')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_alcoholic', 'alcoholic')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_astringent', 'astringent')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_diacetyl', 'diacetyl')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_dms', 'dms')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_estery', 'estery')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_grassy', 'grassy')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_light_struck', 'light_struck')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_metallic', 'metallic')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_musty', 'musty')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_oxidized', 'oxidized') 
        db.rename_column(u'contest_bjcpjudgingresult', 'old_phenolic', 'phenolic')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_solvent', 'solvent')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_sour_acidic', 'sour_acidic')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_sulfur', 'sulfur')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_vegetal', 'vegetal')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_yeasty', 'yeasty')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_aroma_description', 'aroma_description')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_aroma_score', 'aroma_score')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_appearance_description', 'appearance_description')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_appearance_score', 'appearance_score')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_flavor_description', 'flavor_description')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_flavor_score', 'flavor_score')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_description', 'mouthfeel_description')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_score', 'mouthfeel_score')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_overall_impression_description', 'overall_impression_description')
        db.rename_column(u'contest_bjcpjudgingresult', 'old_overall_impression_score', 'overall_impression_score')


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
            'parent_style': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subcategories'", 'null': 'True', 'to': u"orm['contest.BeerStyle']"})
        },
        u'contest.bjcpbeerjudgingresult': {
            'Meta': {'object_name': 'BJCPBeerJudgingResult', '_ormbases': [u'contest.BJCPJudgingResult']},
            'acetaldehyde': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appearance_description': ('django.db.models.fields.TextField', [], {}),
            'appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aroma_description': ('django.db.models.fields.TextField', [], {}),
            'aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'astringent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'bjcpjudgingresult_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contest.BJCPJudgingResult']", 'unique': 'True', 'primary_key': 'True'}),
            'diacetyl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flavor_description': ('django.db.models.fields.TextField', [], {}),
            'flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'grassy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'sulfur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vegetal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yeasty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contest.bjcpciderjudgingresult': {
            'Meta': {'object_name': 'BJCPCiderJudgingResult', '_ormbases': [u'contest.BJCPJudgingResult']},
            'acetaldehyde': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'acetified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'acidic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appearance_description': ('django.db.models.fields.TextField', [], {}),
            'appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aroma_description': ('django.db.models.fields.TextField', [], {}),
            'aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'astringent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'bjcpjudgingresult_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contest.BJCPJudgingResult']", 'unique': 'True', 'primary_key': 'True'}),
            'diacetyl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'farmyard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flavor_description': ('django.db.models.fields.TextField', [], {}),
            'flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'fruity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'metallic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mousy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'oaky': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'oily_ropy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'overall_impression_description': ('django.db.models.fields.TextField', [], {}),
            'overall_impression_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'oxidized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phenolic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spicy_smoky': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sulfite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sweet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vegetal': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contest.bjcpjudgingresult': {
            'Meta': {'object_name': 'BJCPJudgingResult'},
            'old_acetaldehyde': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_alcoholic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_appearance_description': ('django.db.models.fields.TextField', [], {}),
            'old_appearance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_aroma_description': ('django.db.models.fields.TextField', [], {}),
            'old_aroma_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_astringent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_diacetyl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_dms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_estery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_flavor_description': ('django.db.models.fields.TextField', [], {}),
            'old_flavor_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_grassy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intangibles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'judge_bjcp_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'old_light_struck': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_metallic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_mouthfeel_description': ('django.db.models.fields.TextField', [], {}),
            'old_mouthfeel_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_musty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_overall_impression_description': ('django.db.models.fields.TextField', [], {}),
            'old_overall_impression_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_oxidized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_phenolic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_solvent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_sour_acidic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stylistic_accuracy': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_sulfur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'technical_merit': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'old_vegetal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'old_yeasty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
