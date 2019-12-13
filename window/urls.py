from django.urls import path
from . import views as window_views
app_name = "window"

urlpatterns = [
    path('window/', window_views.menu, name = "menu"),
    path('window/about/', window_views.about, name = "about"),
    path('window/incheon/', window_views.incheon, name = "incheon"),
    path('window/seoul/', window_views.seoul, name = "seoul"),
    path('show/<str:topic_title>/', window_views.show, name='show'),
    #path('link/', window_views.link, name='link'),
   
    path('zzim/', window_views.zzim, name='zzim'),
    path('window/myfage', window_views.myfage, name='myfage'),
    # commnet path
    path('show/<str:topic_title>/comment/', window_views.comment , name='comment'),

    # 복붙...
    path('articles/<int:article_id>/edit/', window_views.edit, name="edit"),
    path('articles/<int:article_id>/delete/', window_views.delete, name="delete"),
    path('comments/', window_views.comments, name="comments"),
    path('comments/<int:comment_id>/edit/', window_views.edit_comment, name="edit_comment"),
    path('comments/delete/', window_views.delete_comment, name="delete_comment"),

]