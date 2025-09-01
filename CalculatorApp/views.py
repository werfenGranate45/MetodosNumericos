from django.shortcuts import render
from django.http import HttpResponseBadRequest

from utils_logic.utils_calculatorApp import match_operation
from .forms import DegreeForm
from show_func.showFunction import ShowFunction

#Esta vista es la que se encarga de mostrar la vista principal
def index(request):
    
    context = {} #En caso de que se agreguen mas inputs
    context['form'] = DegreeForm()
    return render(request, 'CalculatorApp/index.html', context)

#Esta es la vista que se va encargar de mostrar el resultado
#Ya funciona la parte de la validacion y es mejor en django cargar la 
def calculator_view(request):
    labelX, func  = 'Angulo [RAD]', 'f(x)'
    form  = DegreeForm(request.GET or None)
    image = None
    oper  = request.GET.get('operacion')

    #Verifico que el input sea valido y que el operacion este entre los seleccionados
    if form.is_valid() and oper in ('sen', 'cos', 'exp'):          
        #Una vez valida el input, obtengo el valor por medio de su clave que es como se llama la variable en el form
        number      = form.cleaned_data['degree_field'] 
        result      = match_operation(oper, number)
        #En caso de que sea None, manda un bad Request
        if result is None:
            return HttpResponseBadRequest("Operacion fallida, intente de nuevo")
        #Muestra la informacion
        show_result = ShowFunction(result[0], result[1])
        show_result.custom_labels(oper,labelX, func)
        image = show_result.get_image() #Lo convierte en imagen para ser renderizada
        return render(request, 'CalculatorApp/result.html', {'image': image}) #Mando a lo chido
    else:
       #En caso de que no sea valida, o oper no este en la tupla se carga el form y se renderiza de nuevo
       form = DegreeForm()
    
    return render(request, 'CalculatorApp/index.html', {'form': form})

    


