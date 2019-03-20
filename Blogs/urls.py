from django.urls import include,path
from . import views
urlpatterns=[
	path('',views.BlogsListView.as_view(),name='homeBlog'),
	path('results',views.search,name='search'),
	path('results1',views.search1,name='search1'),
	path('results2',views.search2,name='search2'),
	path('blogs/<int:pk>',views.BlogsDetailView.as_view(),name='blogsDetail'),
	path('blogs/new/',views.BlogsCreateView.as_view(),name='blogsCreate'),
	path('blogs/<int:pk>/update',views.BlogsUpdateView.as_view(),name='blogsUpdate'),
	path('blogs/<int:pk>/delete',views.BlogsDeleteView.as_view(),name='blogsDelete'),
]