# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BJCPJudgingResult.phenolic'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_phenolic')

        # Deleting field 'BJCPJudgingResult.mouthfeel_score'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_score')

        # Deleting field 'BJCPJudgingResult.solvent'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_solvent')

        # Deleting field 'BJCPJudgingResult.grassy'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_grassy')

        # Deleting field 'BJCPJudgingResult.alcoholic'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_alcoholic')

        # Deleting field 'BJCPJudgingResult.estery'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_estery')

        # Deleting field 'BJCPJudgingResult.light_struck'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_light_struck')

        # Deleting field 'BJCPJudgingResult.astringent'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_astringent')

        # Deleting field 'BJCPJudgingResult.sulfur'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_sulfur')

        # Deleting field 'BJCPJudgingResult.acetaldehyde'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_acetaldehyde')

        # Deleting field 'BJCPJudgingResult.metallic'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_metallic')

        # Deleting field 'BJCPJudgingResult.aroma_score'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_aroma_score')

        # Deleting field 'BJCPJudgingResult.oxidized'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_oxidized')

        # Deleting field 'BJCPJudgingResult.sour_acidic'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_sour_acidic')

        # Deleting field 'BJCPJudgingResult.mouthfeel_description'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_description')

        # Deleting field 'BJCPJudgingResult.overall_impression_score'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_overall_impression_score')

        # Deleting field 'BJCPJudgingResult.musty'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_musty')

        # Deleting field 'BJCPJudgingResult.flavor_score'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_flavor_score')

        # Deleting field 'BJCPJudgingResult.flavor_description'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_flavor_description')

        # Deleting field 'BJCPJudgingResult.yeasty'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_yeasty')

        # Deleting field 'BJCPJudgingResult.overall_impression_description'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_overall_impression_description')

        # Deleting field 'BJCPJudgingResult.appearance_score'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_appearance_score')

        # Deleting field 'BJCPJudgingResult.dms'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_dms')

        # Deleting field 'BJCPJudgingResult.aroma_description'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_aroma_description')

        # Deleting field 'BJCPJudgingResult.diacetyl'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_diacetyl')

        # Deleting field 'BJCPJudgingResult.vegetal'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_vegetal')

        # Deleting field 'BJCPJudgingResult.appearance_description'
        db.delete_column(u'contest_bjcpjudgingresult', 'old_appearance_description')

    def backwards(self, orm):
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.mouthfeel_score'
        db.add_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.phenolic'
        db.add_column(u'contest_bjcpjudgingresult', 'old_phenolic',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.solvent'
        db.add_column(u'contest_bjcpjudgingresult', 'old_solvent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.grassy'
        db.add_column(u'contest_bjcpjudgingresult', 'old_grassy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.alcoholic'
        db.add_column(u'contest_bjcpjudgingresult', 'old_alcoholic',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.estery'
        db.add_column(u'contest_bjcpjudgingresult', 'old_estery',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.light_struck'
        db.add_column(u'contest_bjcpjudgingresult', 'old_light_struck',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.astringent'
        db.add_column(u'contest_bjcpjudgingresult', 'old_astringent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.sulfur'
        db.add_column(u'contest_bjcpjudgingresult', 'old_sulfur',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.acetaldehyde'
        db.add_column(u'contest_bjcpjudgingresult', 'old_acetaldehyde',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.metallic'
        db.add_column(u'contest_bjcpjudgingresult', 'old_metallic',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.aroma_score'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.aroma_score' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.aroma_score'
        db.add_column(u'contest_bjcpjudgingresult', 'old_aroma_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.oxidized'
        db.add_column(u'contest_bjcpjudgingresult', 'old_oxidized',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.sour_acidic'
        db.add_column(u'contest_bjcpjudgingresult', 'old_sour_acidic',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.mouthfeel_description'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.mouthfeel_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.mouthfeel_description'
        db.add_column(u'contest_bjcpjudgingresult', 'old_mouthfeel_description',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.overall_impression_score'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.overall_impression_score' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.overall_impression_score'
        db.add_column(u'contest_bjcpjudgingresult', 'old_overall_impression_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.musty'
        db.add_column(u'contest_bjcpjudgingresult', 'old_musty',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.flavor_score'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.flavor_score' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.flavor_score'
        db.add_column(u'contest_bjcpjudgingresult', 'old_flavor_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.flavor_description'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.flavor_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.flavor_description'
        db.add_column(u'contest_bjcpjudgingresult', 'old_flavor_description',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.yeasty'
        db.add_column(u'contest_bjcpjudgingresult', 'old_yeasty',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.overall_impression_description'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.overall_impression_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.overall_impression_description'
        db.add_column(u'contest_bjcpjudgingresult', 'old_overall_impression_description',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.appearance_score'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.appearance_score' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.appearance_score'
        db.add_column(u'contest_bjcpjudgingresult', 'old_appearance_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.dms'
        db.add_column(u'contest_bjcpjudgingresult', 'old_dms',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.aroma_description'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.aroma_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.aroma_description'
        db.add_column(u'contest_bjcpjudgingresult', 'old_aroma_description',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.diacetyl'
        db.add_column(u'contest_bjcpjudgingresult', 'old_diacetyl',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BJCPJudgingResult.vegetal'
        db.add_column(u'contest_bjcpjudgingresult', 'old_vegetal',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BJCPJudgingResult.appearance_description'
        raise RuntimeError("Cannot reverse this migration. 'BJCPJudgingResult.appearance_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'BJCPJudgingResult.appearance_description'
        db.add_column(u'contest_bjcpjudgingresult', 'old_appearance_description',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intangibles': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'judge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'judge_bjcp_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'stylistic_accuracy': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'technical_merit': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
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
