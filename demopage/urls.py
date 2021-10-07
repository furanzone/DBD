from django.urls import path
from demopage.views import mapping

app_name = 'demopage'

urlpatterns = [
    # path('', DemoView.as_view(), name='demo')
    path('mapping/', mapping.as_view(), name='mapping')
]