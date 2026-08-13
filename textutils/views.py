from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # print(removepunc)

    
    # print(djtext)

    analyzed = djtext
    purpose = []

    # 1. Remove Punctuation
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\\,*<>./?@#$%^&*_~'''

        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        purpose.append("Removed Punctuation")

    # 2. Convert to Full Caps
    if fullcaps == "on":

        analyzed = analyzed.upper()

        purpose.append("Changed to Uppercase")

    # 3. Remove New Lines
    if newlineremover == "on":

        analyzed = analyzed.replace("\n", "")
        analyzed = analyzed.replace("\r", "")

        purpose.append("Removed New Lines")

    # 4. Remove Extra Spaces
    if extraspaceremover == "on":

        analyzed = " ".join(analyzed.split())

        purpose.append("Removed Extra Spaces")

    # If nothing is selected
    if not purpose:
        return HttpResponse("Please select at least one operation.")

    params = {
        'purpose': " + ".join(purpose),
        'analyzed_text': analyzed
    }

    return render(request, 'analyze.html', params)