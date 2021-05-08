from django.shortcuts import render, HttpResponse, redirect
import random
COINS = {
    "gold": (4,9),
    "silver": (2,7),
    "bronze": (10,20),
    "plastic": (5,15),
}

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


def newMembers(request):
    if request.method == 'GET':
        return redirect('/form/')
    request.session['results'] = {
        'memberName': request.POST['memberName'],
    }
    return redirect('/results')

def results(request):
    context = {
        'results': request.session['results'],
    }
    return render(request, 'results.html', context)

def theCoin(request):
    if not "price" in request.session:
        request.session['price'] = 0
    return render(request, 'NinjCoin.html')

def reset(request):
    request.session.clear()
    return redirect('/ninjcoin')

def purchase(request):
    if request.method == 'GET':
        return redirect('/ninjcoin/')

    itemName = request.POST['categories']
    categories = COINS[itemName]

    currTotal = random.randint(categories[0], categories[1])

    result = 'total'

    request.session['price'] += currTotal
    return redirect('/ninjcoin/')

    

# Create your views here.
