from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Document
import pandas as pd
import os
import pandas_profiling
import PIL
from django.core.handlers.wsgi import WSGIRequest
from io import StringIO
context = {'message':'Upload your CSV file'}
def file_upload_view(request):
    print(request)
    # import pdb; pdb.set_trace()        
    global context
    if request.method == 'POST':
        working_file = True
        my_file = request.FILES.get('file')
        data_bytes = my_file.file.getvalue()
        f = open(f'media/{my_file.name}', 'wb')
        f.write(data_bytes)
        f.close()
        df = pd.read_csv(f'media/{my_file.name}')
        profile = pandas_profiling.ProfileReport(df)
        # profile.to_file('export.html')
        html_profile = profile.html
        context = {'message': html_profile}
        return render(request, 'list.html', context)
        # return redirect(request.META['HTTP_REFERER'])
                
    return render(request, 'list.html', context)