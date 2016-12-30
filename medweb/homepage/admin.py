# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from medweb.homepage.models import Person, Evaluation, RandomReferral
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _


class EvaluationInline(admin.StackedInline):
    model = Evaluation
    readonly_fields = ("created", "modified",)


class PersonAdmin(admin.ModelAdmin):
    inlines = (EvaluationInline,)
    readonly_fields = ("created", "modified",)
    list_filter = ["created", "contacted", 'evaluation__call_time']
    search_fields = ['first_name', 'last_name', ]
    list_display = ['first_name', 'last_name', 'email', 'office_phone', 'position', 'get_call_time']

    def get_call_time(self, obj):
        return obj.evaluation.call_time

    get_call_time.short_description = 'Call Time'
    get_call_time.admin_order_field = 'evaluation__call_time'


class RandomReferralAdmin(admin.ModelAdmin):
    readonly_fields = ('referral', 'created')
    list_display = ['referral', 'created']

    def has_add_permission(self, request):
        return False


admin.site.site_header = _('Synergy+ administration')
admin.site.register(Person, PersonAdmin)
admin.site.register(RandomReferral, RandomReferralAdmin)
