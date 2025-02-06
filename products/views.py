from django.shortcuts import render
from .models import Category, Tag, Product
from django.db.models import Q


# Create your views here.
def products(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()

    # Get search parameter
    search_query = request.GET.get("search", "")
    category_id = request.GET.get("category", "")
    tag_ids = request.GET.getlist("tags")

    # Filter for products
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    context = {
        "categories": categories,
        "tags": tags,
        "products": products,
        "search_query": search_query,
        "selected_categories": int(category_id) if category_id else None,
    }
    return render(request, "products.html", context)
