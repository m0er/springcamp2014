# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Speaker.desc'
        db.add_column(u'speaker_speaker', 'desc',
                      self.gf('django.db.models.fields.TextField')(default=datetime.datetime(2014, 6, 2, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Speaker.desc'
        db.delete_column(u'speaker_speaker', 'desc')


    models = {
        u'speaker.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['speaker']