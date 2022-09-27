from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from peticao.models import Peticao



@admin.register(Peticao)
class PeticaoAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)