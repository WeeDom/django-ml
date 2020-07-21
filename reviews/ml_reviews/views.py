from django.shortcuts import render
from django.http import HttpResponse
from .models import Review, Opinion


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def review(request, review_id):
    latest_reviews_list = Review.objects.order_by('-sampled_date')[:5]
    context = {'latest_reviews_list': latest_reviews_list}
    return render(request, 'index.html', context)
    # response = "You're looking at the results of review %s."
    # return HttpResponse(response % review_id)


def home(request):
    return HttpResponse("You're seeing the home page")


def opinion(request, opinion_id):
    return HttpResponse("You're seeing the opinion %s." % opinion_id)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
