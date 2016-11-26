# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from medweb.homepage.models import Person, Evaluation


class EvaluationInline(admin.StackedInline):
    model = Evaluation
    readonly_fields = ("created", "modified",)

class PersonAdmin(admin.ModelAdmin):
    inlines = (EvaluationInline,)
    readonly_fields = ("created", "modified",)
    list_filter = ["created", "contacted"]
    search_fields = ['first_name', 'last_name',]

admin.site.register(Person, PersonAdmin)
