from django.db import models
from django.shortcuts import render

# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    template = "formbuilder/form_page.html"
    intro = RichTextField(blank=True)
    
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)
    
            if form.is_valid():
                self.process_form_submission(form)

                # Update the original landing page context with other data
                landing_page_context = self.get_context(request)
                print("context here")
                print(landing_page_context)
                landing_page_context['Name'] = form.cleaned_data['name']
                landing_page_context['Dish'] = form.cleaned_data['type-of-dish']
                landing_page_context['Hobbies'] = form.cleaned_data['enter-your-hobbies']
                print(form.cleaned_data)
                return render(request,self.get_landing_page_template(request),landing_page_context)
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        return render(request,self.get_template(request),context)

