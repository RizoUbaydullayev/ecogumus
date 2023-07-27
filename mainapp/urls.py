from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('<str:lang>/', views.MainPageView.as_view(), name='main_page'),
    path('<str:lang>/about_company', views.AboutCompanyPageView.as_view(), name='about_company_page'),
    path('<str:lang>/product', views.ProductPageView.as_view(), name='product_page'),
    path('<str:lang>/cooperation', views.CooperationPageView.as_view(), name='cooperation_page'),
]