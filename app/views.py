from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
    {
        "title": f"Question {j}",
        "text": f"{j}) Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "number": j,
    } for j in range(1, 20)
]

ANSWERS = [
    {
        "title": f"Answer {j}",
        "text": f"{j}) Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "number": j,
    } for j in range(1, 7)
]


def index(request):
    paginator = Paginator(QUESTIONS, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(request, "index.html", {"questions": QUESTIONS, "page": page})

def intro(request):
    return render(request, "intro.html")

def ask(request):
    return render(request, "ask.html")

def question_page(request, i: int):
    return render(request, "question_page.html", {"answers": ANSWERS, "questions": QUESTIONS[i - 1]}) 

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

