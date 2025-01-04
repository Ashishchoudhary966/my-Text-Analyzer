# I have created this file - Ashish

from django.http import HttpResponse
from django.shortcuts import render


# home page
def home(request):
    return render(request , 'index.html')


# analyze page
def analyze(request):

    # get textarea value in djtext
    djtext = request.POST.get('text' , 'default')

    # get checkbox values(default is off)
    rem_punch = request.POST.get('removepunc' , 'off')
    textcaps = request.POST.get('textcaps' , 'off')
    newLineRemover = request.POST.get('newLineRemover' , 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover' , 'off')
    charCount = request.POST.get('charCount' , 'off')

    # which checkbox is on
    if rem_punch == 'on':
        punchuations = '''!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punchuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punchuation' , 'analyzed_text':analyzed}
        djtext = analyzed
    
    if textcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Converted in upper case' , 'analyzed_text':analyzed}
        djtext = analyzed
    
    if newLineRemover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r' :
                analyzed = analyzed + char
        params = {'purpose':'New Line Removed' , 'analyzed_text':analyzed}
        djtext = analyzed
    
    if extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index + 1]  == ' '):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Removed' , 'analyzed_text':analyzed}
        djtext = analyzed
    
    if charCount == 'on':
        analyzed = ""
        count = 0
        for char in djtext:
            count = count +1
        analyzed = count
        params = {'purpose':'Total Character counted' , 'analyzed_text':analyzed}
    
    if rem_punch == 'off' and textcaps == 'off' and newLineRemover == 'off' and extraSpaceRemover == 'off' and charCount == 'off' :
        return HttpResponse (''' <h2>Please Select any operation and try again!!</h2> ''')

    return render(request , 'analyze.html' , params)

