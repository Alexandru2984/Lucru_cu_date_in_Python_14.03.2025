from django.shortcuts import render
import numpy as np
# Create your views here.

def random_color_view(request):
    
    culori_rgb = np.random.randint(0, 255, 3)
    context = {
        'rosu' : culori_rgb[0],
        'verde' : culori_rgb[1],
        'albastru' : culori_rgb[2],
    }
    return render(request, "culoare_random.html", context)  
