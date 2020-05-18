from django.shortcuts import render

# Creating our views here
def home_view(request): # home_view is the name of our page template
    return render(request, "home.html", {}) # we return a render of our html page

def about_view(request):
    return render(request, "about.html", {})

def rules_view(request):
    return render(request, "rules.html", {})

def stats_view(request):
    return render(request, "statistics.html", {})

def tournaments_view(request):
    return render(request, "tournaments.html", {})

def impressum_view(request):
    return render(request, "impressum.html", {})

def reference_view(request):
    return render(request, "reference.html", {})