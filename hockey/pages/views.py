from django.shortcuts import render

# We create new page view with this function
def page_view(request):
    return render(request, "page.html", {})