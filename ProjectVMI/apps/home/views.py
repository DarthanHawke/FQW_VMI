from django import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import VMIform
from pyswarm import pso
from math import sqrt


def index(request):
    if request.method == 'GET':
        visibility = "none"
        context = {'segment': 'index', 'visibility': visibility}

        html_template = loader.get_template('home/index.html')
        return HttpResponse(html_template.render(context, request))
    if request.method == 'POST':
        form = VMIform(request.POST)
        if form.is_valid():
             C1 = form.cleaned_data['C1']
             C2 = form.cleaned_data['C2']
             R = form.cleaned_data['R']
             H = form.cleaned_data['H']
             F = form.cleaned_data['F']
             A = form.cleaned_data['A']
             args = [C1, C2, R, H, F]
             lb = [1]
             ub = [A/(C1+C2)]
             xopt, fopt = pso(VMIform.VMI, lb, ub, args=args)
             Q = '{:.0f}'.format(float(xopt[0]))
             F = '{:.0f}'.format(xopt[0] * F)
             vmi = '{:.0f}'.format(float(fopt))
             minargs = [xopt[0], C1, C2, R, H]
             TC = VMIform.TC(minargs)
             TC = '{:.0f}'.format(float(TC))
             visibility = "block"
             data = {"vmi": vmi, "Q": Q, "F": F,
                     "TC": TC, 'visibility': visibility}
             html_template = loader.get_template('home/index.html')
             return HttpResponse(html_template.render(data, request))
        else:
            form = VMIform()
            return render(request, 'home/index.html', {'form': form})
    visibility = 0
    context = {'segment': 'index', 'visibility': visibility}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))