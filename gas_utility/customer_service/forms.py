from django import forms
from .models import ServiceRequest, ServiceRequestAttachment

class ServiceRequestForm(forms.ModelForm):
    attachments = forms.FileField(
        widget=forms.FileInput(attrs={'multiple': False}), 
        required=False
    )

    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details']

    def save(self, commit=True):
        service_request = super().save(commit=False)
        if commit:
            service_request.save()
            attachments = self.files.getlist('attachments')
            for attachment in attachments:
                ServiceRequestAttachment.objects.create(
                    request=service_request,
                    file=attachment
                )
        return service_request