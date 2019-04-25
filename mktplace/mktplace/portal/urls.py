from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    #Search urls
    url(r'^search$', views.search, name='search'),
    #Product urls
    url(r'^my_products$', views.my_products, name='my_products'),
    url(r'^my_data', views.my_data, name='my_data'),
    url(r'^product/new$', views.product_new, name='product_new'),
    url(r'^product/new/question/(?P<product_id>[\d]+)$', views.product_new_question, name='product_new_question'),
    url(r'^product/edit/(?P<product_id>[\d]+)$', views.product_edit, name='product_edit'),
    url(r'^product/(?P<slug>[-\d\w]+)$', views.product_show, name='product_show'),
    #Questions urls
    url(r'^product/(?P<product_id>[\d]+)/questions/$', views.product_question, name='product_question'),
    url(r'^product/(?P<product_id>[\d]+)/questions/(?P<question_id>[\d]+)$', views.product_answer_question, name='product_answer_question'),

    # Images urls
    #url(r'^product/(?P<product_id>[\d]+)/images$', views.product_images, name='product_images'),
    #url(r'^product/new/image/(?P<product_id>[\d]+)$', views.product_images_new, name='product_images_new'),
    # url(r'^product/(?P<product_id>[\d]+)/image/(?P<image_id>[\d]+)/delete$', views.prodcut_images_delete,
    # name='product_images_delete'),
]