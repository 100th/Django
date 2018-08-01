import json
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.encoding import smart_text
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder


class IamportBaseForm(forms.ModelForm):
    template_name = None
    params_names = None
    imp_fn_name = None


    def get_iamport_params(self):
        params = {}
        for name in self.params_names:
            if hasattr(self.instance, name):
                params[name] = getattr(self.instance, name)
        return params


    def as_iamport(self):
        hidden_fields = mark_safe(''.join(smart_text(field) for field in self.hidden_fields()))

        iamport_params = self.get_iamport_params()
        json_string = json.dumps(iamport_params, cls=DjangoJSONEncoder, ensure_ascii=False)
        iamport_json_fields = mark_safe(json_string)

        template_name = getattr(self, 'template_name', None)
        if not template_name:
            raise ValueError('아임포트 템플릿 경로를 지정해주세요.')

        return hidden_fields + render_to_string(template_name, {
            'json_fields': iamport_json_fields,
            'iamport_shop_id': settings.IAMPORT_SHOP_ID,
            'imp_fn_name': self.imp_fn_name,
        })


    def save(self, commit=True):
        order = super().save(commit=False)
        order.update(commit=commit)
        return order
