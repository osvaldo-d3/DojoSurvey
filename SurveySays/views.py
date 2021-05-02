from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "surveyName": "Dojo Survey",
        "surveyLocation": "H-Town, TX",
        "surveyTypes": ["Amateur", "Novice", "Expert", "Master"]
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("All about our Project/Application")

# Without Sessions and Redirect

#def form(request):
    #return render(request, "surveyForm.html")
    #if request.method == "GET":
    #    print("GET request was made for surveyForm.html")
    #   return render(request, "surveyForm.html")
    #if request.method == "POST":
    #    print("POST request was made for surveyForm.html")

#def results(request):
    #if request.method == "POST":
        #context = {
                #'memberName': request.POST['memberName'],
        #}
        #return render(request, 'results.html', context)
    #return render(request, 'results.html')

def form(request):
    return render(request, 'surveyForm.html')


def newMember(request):
    if request.method == 'GET':
        return redirect('/form/')
    request.session['results'] = {
        'memberName': request.POST['memberName'],
    }
    return redirect('/results/')

def results(request):
    context = {
        'memberName': request.session['memberName'],
    }
    return render(request, 'results.html', context)

# Create your views here.
