from typing import List, Dict

from django.urls import path, include, reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from cvinterface.controlled_vocabularies import requests
from cvinterface.views.base_views import UnitsListView
from cvinterface.views.request_views import RequestsView, request_list_views, request_create_views, request_update_views
from cvinterface.views.vocabulary_views import VocabulariesView, list_views, detail_views

urlpatterns: List[path] = [
    path('', VocabulariesView.as_view(), name='home'),
    path('units/', UnitsListView.as_view(), name='units'),
    path('requests/', RequestsView.as_view(), name='requests_list'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='cvinterface/account/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
]

# cv list views
cv_name: str

for cv_name in list_views:
    view: ListView = list_views[cv_name]

    urlpatterns += [
        path(f'{cv_name}/', view, name=cv_name),
    ]

# cv detail views
for cv_name in detail_views:
    view: DetailView = detail_views[cv_name]

    urlpatterns += [
        path(f'{cv_name}/<slug:term>/', view, name=f'{cv_name}_detail'),
        path(f'{cv_name}/<slug:term>/<int:pk>', view, name=f'{cv_name}_detail')
    ]

# request list views
for request_name in request_list_views:
    view: ListView = request_list_views[request_name]

    urlpatterns += [
        path(f'requests/{requests[request_name]["vocabulary"]}/', view, name=request_name),
    ]

# request create views
for request_name in request_create_views:
    vocabulary: str = requests[request_name]["vocabulary"]
    view: CreateView = request_create_views[request_name]
    urlpatterns += [
        path(f'requests/{vocabulary}/new/', view, name=f'{vocabulary}_form'),
        path(f'requests/{vocabulary}/new/<slug:vocabulary_id>', view, name=f'{vocabulary}_form'),
    ]

# request update views
for request_name in request_update_views:
    vocabulary: str = requests[request_name]["vocabulary"]
    view: UpdateView = request_update_views[request_name]

    urlpatterns += [
        # TODO: change pk here.
        path(f'requests/{requests[request_name]["vocabulary"]}/(?P<pk>[-\w]+)/$', view,
            name=requests[request_name]['vocabulary'] + '_update_form'),
    ]
