from django.contrib import admin
from .models import ServiceRequest, ServiceRequestAttachment
from django.utils import timezone


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'request_type', 'status', 'created_at', 'resolved_at', 'staff_member')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('user__username', 'user__email', 'request_type', 'details')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'resolved_at')

    def save_model(self, request, obj, form, change):
        new_status = form.cleaned_data.get('status')
        if new_status == 'resolved' and obj.status != 'resolved':
            obj.staff_member = request.user
            obj.resolved_at = timezone.now()
        super().save_model(request, obj, form, change)

@admin.register(ServiceRequestAttachment)
class ServiceRequestAttachmentAdmin(admin.ModelAdmin):
    list_display = ('request', 'file')