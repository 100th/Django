from django import forms

class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'


class RateitjsWidget(forms.NumberInput):
    input_type = 'rating'
    template_name = 'widgets/rateitjs_number.html'

    class Media:
        css = {
            'all': [
                'widgets/rateit.js/rateit.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'widgets/rateit.js/jquery.rateit.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({
            'min': 0,
            'max': 5,
            'step': 1,
        })
        return attrs


class AutoCompleteSelect(forms.Select):
    template_name = 'widgets/autocomplete_select.html'

    class Media:
        css = {
            'all': [
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs);
        context['style'] = 'min-width: 200px;'
        return context


class DatePickerWidget(forms.DateInput):
    template_name = 'widgets/picker_date.html'

    class Media:
        css = {
            'all': [
            '//code.jquery.com/ui/1.12.1/themes/blitzer/jquery-ui.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            '//code.jquery.com/ui/1.12.1/jquery-ui.min.js',
        ]


class PreviewClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/preview_clearable_file_input.html'

    class Media:
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
        ]


class TuiEditorWidget(forms.Textarea):
    template_name = 'widgets/tuieditor_widget.html'

    class Media:
        css = {
            'all': [
                'codemirror/lib/codemirror.css',
                'highlightjs/styles/github.css',
                'tui-editor/dist/tui-editor.css',
                'tui-editor/dist/tui-editor-contents.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'tui-code-snippet/dist/tui-code-snippet.js',
            'markdown-it/dist/markdown-it.js',
            'to-mark/dist/to-mark.js',
            'codemirror/lib/codemirror.js',
            'highlightjs/highlight.pack.js',
            'squire-rte/build/squire.js',
            'tui-editor/dist/tui-editor-Editor.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['style'] = 'display: none;'
        return attrs
