from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Category, Product, ProductQuestion, ProductAnswer, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


class CategoryAdmin(AjaxSelectAdmin):
    prepopulated_fields = { "slug" : ('name', )}
    list_filter = ['hidden']
    list_display = ('name', 'parent', 'hidden')
    form = make_ajax_form(Category, {
        'parent': 'categories'
    })


class ProductAdmin(AjaxSelectAdmin):
    prepopulated_fields = { "slug" : ('name', )}
    list_filter = ['status']
    list_display = ('name', 'short_description', 'status')
    #inlines = (ProductImageInline,)
    form = make_ajax_form(Product, {
        'user': 'user',
    })

class ProductAnswerInline(admin.StackedInline):
    model = ProductAnswer
    can_delete = False
    extra = 0
    list_filter = ['status']
    list_display = ('user', 'answer', 'product_question', 'status')


class ProductQuestionsAdmin(admin.ModelAdmin):
    inlines = (ProductAnswerInline, )
    list_filter = ['status']
    list_display = ('id', 'product', 'question', 'status')

### Product Images administration
# class ProductImageInline(admin.StackedInline):
#     model = ProductImages



admin.site.unregister(User),
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestion, ProductQuestionsAdmin)




#Customizing the page's title and text from navbar
admin.site.site_header = 'Marketplace Admin'
admin.site.index_title = 'Marketplace'
admin.site.site_title = 'Admin'
