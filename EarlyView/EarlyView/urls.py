from django.conf.urls import include, url,patterns
from django.contrib import admin

#rest api 에서 사용되는 router 이것을 통하여 data를 post get한다.
from rest_framework import routers

#rest api를 통하여 가져올 것들  as를 사용해야지 여러 class에서 가져올 수 있다.
from Company import views as companyViews
from UserTest import views as userViews

#media의 사진을 가죠오는 것을 사용하기 위한 것.
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
    #관리자/
    url(r'^admin/', include(admin.site.urls)),
    #rest api 로그인 로그아웃 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  #  url(r'^companytest/',include('Company.urls')),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

