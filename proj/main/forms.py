from django import forms
from main.models import Upload_file


class Upload_file_form(forms.Form):

    separator_type = [(" ", "Пробел"), ("   ", "Табуляция"), (",", "Запятая"), (";", "Точка с запятой")]

    file = forms.FileField(label="Файл")
    separator = forms.ChoiceField(label="Разделитель", choices=separator_type)

    




#class Upload_file_form(forms.ModelForm):

    #class Meta:
        #model = Upload_file
        #fields = ('file_in', 'separator')
        #labels = {'file_in': "Файл", 'separator': "Разделитель"}