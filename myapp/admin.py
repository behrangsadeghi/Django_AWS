from django.contrib import admin
from .models import Author, Book 

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Specify fields to display in the list view
    search_fields = ('title', 'author')           # Fields that can be searched
    list_filter = ('title', 'author')             # Fields that can be filtered

@admin.register(Author)
class YourModel2Admin(admin.ModelAdmin):
    list_display = ('name', 'family')
    search_fields = ('family',)
    list_filter = ('family',)

# Alternatively, you can use this simpler method if customization is not needed
# admin.site.register(YourModel1)
# admin.site.register(YourModel2)
