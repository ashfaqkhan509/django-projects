from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('mail/', views.mail_send_view),
    re_path('tag/(?P<tag_slug>[\w]+)/$', views.post_list_view, name='post_list_by_tag_name'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail'),
    path('<int:id>/share/', views.mail_send_view),
    path('new/', views.post_create_view, name='post_create'),
]


# from django.urls import path, re_path
# from blog import views

# app_name = 'blog'  # Add the app_name to specify the namespace

# urlpatterns = [
#     path('', views.post_list_view, name='post_list'),
#     re_path(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_list_view, name='post_list_by_tag_name'),
#     path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail'),
#     path('post/<int:id>/share/', views.mail_send_view, name='mail_send_view'),
# ]





# from django.urls import path, re_path
# from . import views

# app_name = 'blog'  # specify the app namespace

# urlpatterns = [
#     path('mail/', views.mail_send_view),
#     path('', views.post_list_view),
#     re_path(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_list_view, name='post_list_by_tag_name'),
#     # path('', views.PostListView.as_view()),
#     re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[\w-]+)/$', views.post_detail_view, name='post_detail'),
#     path('<int:id>/share/', views.mail_send_view),
# ]
