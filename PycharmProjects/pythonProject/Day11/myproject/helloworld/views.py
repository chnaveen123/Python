from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hello World</h1")
    return render(request, "home.html",{'gname':"Naveen Chiruveru"})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    val3 = val1 + val2
    return render(request, 'result.html',{'res':val3})




def sub(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    val3 = val1 - val2
    return render(request, 'result.html', {'res': val3})

def multi(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    val3 = val1 * val2
    return render(request, 'result.html', {'res': val3})

def div(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    val3 = val1 / val2
    return render(request, "result.html", {"res": val3})

    if val2 == 0:
        val3 = "Zero divide error"
        return render(request, "result.html", {"result": val3})
    else:
        val3 = val1 / val2
        return render(request, "result.html", {"result": val3})


def calculator(request):


    if request.method == "POST":
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        opr = request.POST.get("opr")

        if opr == "+":
            val3 = val1 + val2

        elif opr == "-":
            val3 = val1 - val2

        elif opr == "*":
            val3 = val1 * val2

        elif opr == "/":
            val3 = val1 / val2


    return render(request,"result.html",{'res':val3})

