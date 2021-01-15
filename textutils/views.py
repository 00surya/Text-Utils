# I have created this file - Snehill!
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name':'Snehill', 'place':'gola'}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')
    # return HttpResponse('Home')

def analyze(request):
    # print(request.GET.get('text','default'))
    #Get the text
    djtext = request.POST.get('text','default')

    # Check checkbox values
    removepun = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charaterCounter = request.POST.get('charaterCounter','off')
    print(removepun)
    print(djtext)
    print(newlineremover)
    # analyzed = djtext

    #Analyze the text
    # return HttpResponse('Remove Punc')
    if removepun == "on":
        punchuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punchuations:
                analyzed +=char        
        # print(analyzed)        
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed +=char.upper()         
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        
    if(extraspaceremover=="on"):
        analyzed=""
        for char in djtext:
            analyzed+=char
        analyzed = analyzed.replace("  ","")
        params = {'purpose':'extraspaceremover','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
  
    if(newlineremover=="on"):
        # print("hrlo")
        # analyzed  = analyzed.upper() 
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char    
            if char == "\n":   
                analyzed+=" "    
        # analyzed= analyzed.replace("\n","")
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
          
    if(charaterCounter=="on"):
        i=0
        analyzed=""
        for char in djtext:         
            analyzed+=char
        P = analyzed.replace(" ","")    
        for x in P:
            i+=1 
        params = {'purpose':f'Character Count of <{analyzed}> are {i}.'}
        # return render(request, 'analyze.html', params)

    if(removepun == "off" and fullcaps=="off" and extraspaceremover=="off" and newlineremover=="off" and charaterCounter=="off"):
        # return HttpResponse(djtext)
        params = {'purpose':'You havn\'t check any option.','analyzed_text':djtext}
        return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)
    # else:
        # return HttpResponse('Sorry We can\'t process you request.<br> You may not clicked on check button.')    

# def capfirst(request):
#     return HttpResponse('Capatalize First..')

# def newlineremove(request):
#     return HttpResponse('Newline Remove')    

# def spaceremove(request):
#     return HttpResponse('spaceremove')    
    
# def charcount(request):
#     return HttpResponse('charcount')    
