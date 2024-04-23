from django.shortcuts import render

def about_us_page(request):
    return render(request,'about_us.html')