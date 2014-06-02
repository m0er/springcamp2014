# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'speaker_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
        ))
        db.send_create_signal(u'speaker', ['Speaker'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'speaker_speaker')


    models = {
        u'speaker.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['speaker']