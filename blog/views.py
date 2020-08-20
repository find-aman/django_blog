from django.shortcuts import render

posts = [
    {
        "author": "aman",
        "title": "blog post",
        "content": "first post content",
        "date_posted": "August 21, 2020",
    },
    {
        "author": "akash",
        "title": "blog post 2 ",
        "content": "second post content",
        "date_posted": "August 21, 2020",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
