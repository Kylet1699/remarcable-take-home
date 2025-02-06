# Django Product Catalog
A take-home project made with Django where users can search products by description, filter by categories and tags.

## Setup
1. Clone the repository:\
`git clone https://github.com/Kylet1699/remarcable-take-home.git`\
`cd remarcable_take_home`

2. Install Django\
`pip install django`

3. Run the development server\
`python manage.py runserver`

4. Access the product catalog at `http://127.0.0.1:8000/`

## Front-End & Styling
- Django template system
- Tailwind CSS

## Admin
`username: kylet`\
`password: kylet123`

## Assumptions
1. Each product belongs to one category
2. Product can have multiple tags
3. Search field checks both product name and description
4. Category dropdown is single select since all product belongs to only one category
5. Tag filter allows multiple selections

## Models
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

## AI usage
- Generate sample data for 5 categories, 10 tags, 20 products

