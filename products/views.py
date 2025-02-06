from django.shortcuts import render
from .models import Category, Tag, Product
from django.db.models import Q


# Create your views here.
def products(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()

    #  Example product object
    # {
    #     "id": 1,
    #     "created_at": datetime.datetime(
    #         2025, 2, 6, 1, 6, 31, 202753, tzinfo=datetime.timezone.utc
    #     ),
    #     "updated_at": datetime.datetime(
    #         2025, 2, 6, 1, 6, 31, 202767, tzinfo=datetime.timezone.utc
    #     ),
    #     "name": 'MacBook Pro 14"',
    #     "description": "Latest model with M2 chip, 16GB RAM, 512GB SSD",
    #     "price": Decimal("1999.99"),
    #     "category_id": 7,
    #     "tags": [1, 2, 3]
    # }

    # Get search parameter from URL after form submission
    search_query = request.GET.get("search", "")
    category_id_query = request.GET.get("category", "")
    # Ex. ['1', '2', '3',]
    tags_id_query = request.GET.getlist("tags")

    # Filter for products
    if search_query:
        # Check the search query against both name and description
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    # Filter for categories
    if category_id_query:
        products = products.filter(Q(category_id=int(category_id_query)))

    # Filter for tags
    selected_tags = []  # Prep the array for the template
    if tags_id_query:
        # Match for all the tags
        for tag_id in tags_id_query:
            products = products.filter(Q(tags__id=int(tag_id)))
            selected_tags.append(int(tag_id))

    context = {
        "categories": categories,
        "tags": tags,
        "products": products,
        "search_query": search_query,
        "selected_tags": selected_tags,
        "selected_category": (
            int(category_id_query)
            if category_id_query and category_id_query.isdigit()
            else None
        ),
    }
    return render(request, "products.html", context)
