from django.urls import path
from mainapp.views import ProductView

ap_name = 'mainapp'

# urlpatterns = [
#     path ('', ProductView.as_view(), name='index'),
#     path ('<int:category_id>/', ProductView.as_view(), name='product'),
#     path ('page/<int:page>/<int:category_id>/', ProductView.as_view(), name='page'),
#     path ('page/<int:page>/', ProductView.as_view(), name='page'),
#     path ('categories/', ProductCategoryView.as_view(), name='categories')
# ]

urlpatterns = [
    path ('', ProductView.as_view(), name='index'),
    path ('<int:category_id>/', ProductView.as_view(), name='product'),
    path ('page/<int:page>/', ProductView.as_view(), name='page')
]