from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

all_posts = [
    {
        "slug": "Hike-in-the-mountains 2021",
        "image": "1.jpg",
        "author": "Soliman",
        "date": date(2021, 7, 22),
        "title": "Mountain Hiking 2021",
        "excerpt": "There is nothing like a mountain hiking",
        "content": """
                All the bla bla bla
        """,
    },
    {
        "slug": "Hike-in-the-mountains 2022",
        "image": "2.jpg",
        "author": "Soliman",
        "date": date(2022, 7, 22),
        "title": "Mountain Hiking 2022",
        "excerpt": "There is nothing like a mountain hiking",
        "content": """
                All the bla bla bla
        """,
    },
    {
        "slug": "Hike-in-the-mountains 2023",
        "image": "3.jpg",
        "author": "Soliman",
        "date": date(2023, 7, 22),
        "title": "Mountain Hiking 2023",
        "excerpt": "There is nothing like a mountain hiking",
        "content": """
                All the bla bla bla
        """,
    },
]


def get_date(post):
    return post.get("date")
    # return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    print(latest_post)
    print(all_posts)
    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})


# def index(request):
#     return HttpResponse("Hello, world. You're at the blogs index.")
