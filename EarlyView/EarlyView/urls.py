from django.conf.urls import include, url
from django.contrib import admin
'''
'''
#rest api ���� ���Ǵ� router �̰��� ���Ͽ� data�� post get�Ѵ�.
from rest_framework import routers

#rest api�� ���Ͽ� ������ �͵�  as�� ����ؾ��� ���� class���� ������ �� �ִ�.
from Company import views as companyViews
from UserTest import views as userViews

#media�� ������ ���ҿ��� ���� ����ϱ� ���� ��.
from django.conf import settings
from django.conf.urls.static import static

#router setting
router = routers.DefaultRouter()
router.register(r'company', companyViews.CompanyViewSet)
router.register(r'company/image', companyViews.TaskViewSet)
router.register(r'users', userViews.UserViewSet)
router.register(r'groups',userViews.GroupViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'EarlyView.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #router urls
    url(r'^', include(router.urls)),
    #������/
    url(r'^admin/', include(admin.site.urls)),
    #rest api �α��� �α׾ƿ� 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  #  url(r'^companytest/',include('Company.urls')),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

