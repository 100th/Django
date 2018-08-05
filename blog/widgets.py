from django import forms

class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'


class RateitjsWidget(forms.NumberInput):
    input_type = 'rating'
    template_name = 'widgets/rateitjs_number.html'

    # class Media:
    #     css = {
    #         'all': [
    #             'widgets/rateit.js/rateit.css',
    #         ],
    #     }
    #     js = [
    #         '//code.jquery.com/jquery-2.2.4.min.js',
    #         'widgets/rateit.js/jquery.rateit.min.js',
    #     ]

    # def build_attrs(self, *args, **kwargs):
    #     attrs = super().build_attrs(*args, **kwargs)
    #     attrs.update({
    #         'min': 0,
    #         'max': 5,
    #         'step': 1,
    #     })
    #     return attrs
