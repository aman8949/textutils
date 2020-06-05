# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Typeutils</h1>")
def analyze(request):
    
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    
    if(removepunc=="on"):
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyze=""
        for c in djtext:
            if c not in punctuations:
                analyze=analyze+c
        djtext=analyze
        params={'purpose':'Remove Punctuations','analyzed_text':djtext}
        
        # return render(request,'analyze.html', params)
    
    if(fullcaps=="on"):
        analyze=djtext.upper()
        djtext=analyze
        params={'purpose': 'Convert to Uppercase', 'analyzed_text':djtext}
       
        # return render(request,'analyze.html', params)
    
    if(charcount=="on"):
        analyze=len(djtext)
        djtext=analyze
        params={'purpose': 'Text Length', 'analyzed_text':djtext}
        # return render(request,'analyze.html', params)
    
    if(newlineremover=="on"):
        analyze=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyze=analyze+char
        djtext=analyze
        params={'purpose': 'Remove New Line Character', 'analyzed_text':djtext}
        
        # return render(request,'analyze.html', params)
    
    if(spaceremover=="on"):
        analyze=""
        for i,char in enumerate(djtext):
            if not (djtext[i]==" " and djtext[i+1]==" "):
                analyze=analyze+char
        djtext=analyze
        params={'purpose': 'Remove Multiple Spaces', 'analyzed_text':djtext}
        # return render(request,'analyze.html', params)
    params={'purpose': 'Remove Multiple Spaces', 'analyzed_text':djtext}
    return render(request,'analyze.html', params)

# def capitalizefirst(request):
#     return HttpResponse("<h1>capitalize First</h1>")
# def newlineremove(request):
#     return HttpResponse("<h1>New Line Remove</h1>")
# def spaceremove(request):
#     return HttpResponse("<h1>Space Remove</h1>")
# def charcount(request):
#     return HttpResponse("<h1>Character Count</h1>")
# def about(request):
#     return HttpResponse("<h1>About Aman</h1>")
