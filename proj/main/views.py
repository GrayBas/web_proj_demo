from django.shortcuts import render, redirect
from main.forms import Upload_file_form
from main.models import Coordinate_System, Upload_file
from django.http import HttpResponse, FileResponse


# Create your views here.
class SepError(Exception):
    pass


main_menu = [{'title': "Местная СК", 'url_name': "msk"},
             {'title': "СК 1963г. зона 1", 'url_name': "cs63_c1"},
             {'title': "СК 1963г. зона 2", 'url_name': "cs63_c2"},
             {'title': "СК 1963г. зона 3", 'url_name': "cs63_c3"}
             ]


def main_str(request):
    obj = {'menu': main_menu,
           'msk': Coordinate_System.objects.filter(SC="MSK")[:30],
           'c1': Coordinate_System.objects.filter(zone="C1")[:30],
           'c2': Coordinate_System.objects.filter(zone="C2")[:30],
           'c3': Coordinate_System.objects.filter(zone="C3")[:30],
           'title': "Главная страница"
           }

    return render(request, 'main.html', context=obj)


def msk(request):
    return render(request, 'MSK.html',
                  {'menu': main_menu, 'title': "Местная СК", 'msk': Coordinate_System.objects.filter(SC="MSK")})


def cs63_c1(request):
    return render(request, 'CS_63_C1.html',
                  {'menu': main_menu, 'title': "СК 1963г. зона 1", 'c1': Coordinate_System.objects.filter(zone="C1")})


def cs63_c2(request):
    return render(request, 'CS_63_C2.html',
                  {'menu': main_menu, 'title': "СК 1963г. зона 2", 'c2': Coordinate_System.objects.filter(zone="C2")})


def cs63_c3(request):
    return render(request, 'CS_63_C3.html',
                  {'menu': main_menu, 'title': "СК 1963г. зона 3", 'c3': Coordinate_System.objects.filter(zone="C3")})


def spl(string, separator):
    if separator not in string:
        raise SepError
    if separator == ' ':
        return string.split()
    return string.split(separator)


def conv(inp_file, separator, name):
    out_file = '.'.join(name.split('.')[:-1]) + '.top'
    inp = inp_file.readlines()
    with open(f'main/download_file/{out_file}', 'w') as out:
        for i in inp:
            tmp = spl(str(i), separator)[:4]
            tmp.insert(1, '051')
            print(*map(str.strip, tmp), sep='     ', file=out)
        return out_file


def upload_file(request):
    if request.method == 'POST':
        form = Upload_file_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = form.cleaned_data["file"]
                sep = form.cleaned_data["separator"]
                name = form.cleaned_data["file"].name
                f = conv(file, sep, name)
                return FileResponse(open(f'main/download_file/{f}', 'rb'))
            except SepError:
                form = Upload_file_form()
        else:
            form = Upload_file_form()
    else:
        form = Upload_file_form()

    return render(request, 'upload.html', {'menu': main_menu, 'title': "Конвертация в '.top'", 'form': form})

# def download_file(request):
# return render(request, 'download.html', {'menu': main_menu, 'title': "Скачать"})
