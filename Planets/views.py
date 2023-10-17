from django.shortcuts import render
from django.http import HttpResponse
import requests  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search(request):
    # Make an API request to NASA to fetch image data
    query = request.GET.get('q',"")

    page = request.GET.get('page',1)

    api_url = f"https://images-api.nasa.gov/search?q={query}&page={page}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        # Extract relevant data from the API response
        image_data = data.get("collection", {}).get("items", [])
    else:
        image_data = []  # Handle the case when the API request fails

    # Configure pagination
    paginator = Paginator(image_data, 12)  # 10 items per page

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        images = paginator.page(paginator.num_pages)

    # Render the template and pass the paginated images
    return render(request, 'search_results.html', {'query': query,'images': images})

def home(request):
    return render(request,"index.html")