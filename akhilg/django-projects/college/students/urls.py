from django.urls import path
from.import views

urlpatterns=[

    path('',views.index,name='index.html'),
    # path('aboutus',views.about,name='aboutus'),
    # path('contact',views.contact,name='contact')
]
