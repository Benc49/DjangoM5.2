from django.shortcuts import render

# Create your views here.

def near_hundred(request):
    if request.GET:
        close = abs(100 - int(request.GET["number"])) <= 10 or abs(200 - int(request.GET["number"])) <= 10
        return render(request, "near_hundred.html", {"close": close})
    else:
        return render(request, "near_hundred.html")

def string_splosion(request):
    if request.GET:
            string = ""
            result = request.GET["result"]
            for i in range(len(result)):
                result = result + result[:i+1]
            return render(request, "string_splosion.html", {"result": result})
    else:
        return render(request, "string_splosion.html")
def cat_dog(request):
    if request.GET:
        word = str(request.GET["word"])
        count = word.count("cat") == word.count("dog")
        return render(request, "cat_dog.html", {"count": count})
    else:
        return render(request, "cat_dog.html")
    


def lone_sum(request):
    if request.GET:
        a = int(request.GET["num1"])
        b = int(request.GET["num2"])
        c = int(request.GET["num3"])
        if a == b and b == c:
            total = 0
        elif a == c:
            total = b
        elif a == b: 
            total = c
        elif a == c:
            total = b
        elif b == c:
            total = a
        elif a != b and b != c:
            total = a + b + c
        return render(request, "lone_sum.html", {"total": total})
    else:
        return render(request, "lone_sum.html")

