from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")

def analyze(request):
    text = request.GET.get('text','Default')
    punctuation = '''.,!?;:'"-—()[]{}...@#$%&*/\_'''
    removerpunc = request.GET.get('removepunc','off')
    capitilized = request.GET.get('capitilized','off')
    charcount = request.GET.get('charcount','off')
    removespace = request.GET.get('removespace','off')
    case = request.GET.get('case','default')
    
    analyzedText = ""
    if removerpunc=='on':
        for char in text:
            if char not in punctuation:
                analyzedText = analyzedText+char
    else:
        analyzedText=text
    
    if(capitilized == 'on'):
        analyzedText = analyzedText.capitalize()
    
    length=0
    if(charcount =='on'):
        length = len(analyzedText)
    
    tempstring=""
    if(removespace == 'on'):
        for i in analyzedText:
            if i != ' ' :
                tempstring = tempstring+i
        analyzedText = tempstring

    if(case == "uppercase"):
        analyzedText = analyzedText.upper();
    elif(case=="lowercase"):
        analyzedText = analyzedText.lower();
    else:
        print("this is not proper choice")

    print(len(analyzedText));
    print(analyzedText);
    params = {'analysed':analyzedText ,'charcount':length}
    return render(request,"analyze.html",params)