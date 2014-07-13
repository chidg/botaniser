# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'core_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', null=True, to=orm['auth.User'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', null=True, to=orm['core.Location'])),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', null=True, to=orm['core.Species'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('status', self.gf('django.db.models.fields.CharField')(default='accepted', max_length=12)),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['Report'])

        # Adding model 'Location'
        db.create_table(u'core_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=8)),
            ('lon', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=8)),
        ))
        db.send_create_signal(u'core', ['Location'])

        # Adding model 'Species'
        db.create_table(u'core_species', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Species'])

        # Adding model 'Photo'
        db.create_table(u'core_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('note', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'core', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'core_report')

        # Deleting model 'Location'
        db.delete_table(u'core_location')

        # Deleting model 'Species'
        db.delete_table(u'core_species')

        # Deleting model 'Photo'
        db.delete_table(u'core_photo')


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
        u'core.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '8'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '8'})
        },
        u'core.photo': {
            'Meta': {'object_name': 'Photo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'core.report': {
            'Meta': {'object_name': 'Report'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'null': 'True', 'to': u"orm['core.Location']"}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'null': 'True', 'to': u"orm['core.Species']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'accepted'", 'max_length': '12'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'core.species': {
            'Meta': {'object_name': 'Species'},
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']