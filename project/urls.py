from django.contrib import admin
from django.urls import path, include
from restaurant import views as restaurant_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', restaurant_views.index, name='index'), 
    
    # 🌟 NEW: Path สำหรับหน้ารายละเอียด (รับค่า ID เป็น integer)
    path('<int:restaurant_id>/', restaurant_views.detail, name='detail'), 
]