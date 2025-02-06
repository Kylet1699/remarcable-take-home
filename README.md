# Django Product Catalog
A take-home project made with Django where users can search products by description, filter by categories and tags.

## Setup
1. Clone the repository:\
`git clone https://github.com/Kylet1699/remarcable-take-home.git`
`cd remarcable_take_home`

2. Install Django\
`pip install django`

3. Apply migration\
`python manage.py migrate`

1. Create superuser for admin access\
`python manage.py createsuperuser`

1. Run the development server\
`python manage.py runserver`

1. Access the product catalog at `http://127.0.0.1:8000/`

## Front-End & Styling
- Django template system
- Tailwind CSS

## Admin
`username: kylet`
`password: kylet123`

## Assumptions
1. Each product belongs to one category
2. Product can have multiple tags
3. Search field checks both product name and description
4. Category dropdown is single select since all product belongs to only one category
5. Tag filter allows multiple selections

## AI usage
- Generate sample data for 5 categories, 10 tags, 20 products

## Tasks
1. Create models for products, categories, and tags
   1. Category
      1. created_at: DateTimeField
      2. updated_at: DateTimeField
      3. name: CharField
      4. description: TextField
   2. Product
      1. created_at: DateTimeField
      2. updated_at: DateTimeField
      3. name: CharField
      4. description: TextField
      5. price: DecimalField
      6. category: ForeignKey (Many-to-One, 1 category with many products)
      7. tags: ManyToManyField (Many-to-Many)
   3. Tag
      1. created_at: DateTimeField
      2. updated_at: DateTimeField
      3. name: CharField
2. Make a superuser and populate 5 categories, 10 tags, 20 products with admin interface
3. Setup View for handling search and filters
   1. Should be able to combine search with products, categories and tags
4. Frontend with Django templates
   1. Search text field for description
   2. Checklist for tags and categories, maybe multiselect
   3. Display search result including all product information
