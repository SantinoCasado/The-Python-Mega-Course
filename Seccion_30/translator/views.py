from django.shortcuts import render
from . import translate
import asyncio

def Translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = asyncio.run(translate.translate(original_text))
        return render(request, 'translator.html', {'output_text': output, 'original_text': original_text})
    else:
        return render(request, 'translator.html')