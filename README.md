## Setup
`pip install django`

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