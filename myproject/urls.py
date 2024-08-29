
from django.contrib import admin
from django.urls import path,include
from myapp import views
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import UserViewSet

# from myapp import views as myapp_view
# from myapp1 import views as myapp1_views

router = DefaultRouter()
router.register(r'users', userViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/add_permission/', userViewSet.as_view({'post': 'add_permission'})),
    path('users/<int:pk>/remove_permission/', userViewSet.as_view({'post': 'remove_permission'})),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('admin/', admin.site.urls),
    path('signup/',views.signup),
    path('signup_email/',views.signup_email),
    path('signup_otp_verify/',views.signup_otp_verify),
    path('login/', views.login, name='login'),
    path('login_otp_verify/',views.login_otp_verify),
    # path('create_item_attribute/',views.create_item_attribute),
    path('add_item/<id>/',views.add_item),
    path('edit_item/<id>/',views.edit_item),
    path('delete_item/<id>/',views.delete_item),
    path('transaction_item/<id>/',views.transaction_item),
    path('item/<id>/',views.item),
    path('stock_in/',views.stock_in),
    path('rack_stockin_view/<id>/',views.rack_stockin_view),
    path('stockin_excel_upload/<id>/',views.stockin_excel_upload),
    path('stock_out/',views.stock_out),
    path('rack_stockout_view/<id>/',views.rack_stockout_view),
    path('stockout_excel_upload/<id>/',views.stockout_excel_upload),
    path('adjust/',views.adjust),
    path('summary/<id>/',views.summary),
    # path('summary_count/<id>/',views.summary_count),
    path('photoupload/',views.photoupload),
    path('create_team/',views.create_team),
    path('update_team/<id>/',views.update_team),
    path('get_team_details/<id>/',views.get_team_details),
    path('delete_team/<id>/',views.delete_team),
    path('company_information/',views.company_information),
    path('team_list/<Email>/',views.team_list),
    path('get_team_details/<id>/',views.get_team_details),
    path('item_list_view/<id>/',views.item_list_view),
    path('add_attribute/<id>/',views.add_attribute),
    path('send_attribute/<id>/',views.send_attribute),
    path('edit_attribute/<id>/',views.edit_attribute),
    path('delete_attribute/<id>/',views.delete_attribute),
    # path('excel_upload/', ExcelUploadView.as_view(), name='excel-upload'),
    path('add_item_excel_upload/<id>/',views.add_item_excel_upload),
    path('add_partner/<id>/',views.add_partner),
    path('partner_view/<id>/',views.partner_view),
    path('partner_edit/<id>/',views.partner_edit),
    path('partner_delete/<id>/',views.partner_delete),
    path('groupby/',views.groupby),
    path('transaction/<id>/',views.transaction),
    path('initial_quantity/<id>/',views.initial_quantity),
    path('today_transaction/<id>/',views.today_transaction),
    path('user_edit/<Email>/',views.user_edit),
    path('user_show/<Email>/',views.user_show),
    path('team_delete/<id>/',views.team_delete),
    path('assign_permission/<id>/',views.assign_permission),
    path('resend_email/<id>/',views.resend_email),
    # path('assign_group/',views.assign_group),
    path('get_groups_permissions/',views.get_groups_permissions),
    path('invited_user_list/<id>/',views.invited_user_list),
    path('change_status/<token>/',views.change_status),
    path('custom_permission/<id>/',views.custom_permission),
    path('custom_permission_view/<id>/',views.custom_permission_view),
    path('view_custom_permission/<id>/',views.view_custom_permission),
    path('delete_permiteduser/<id>/',views.delete_permiteduser),
    path('find_similar_image/',views.find_similar_image),
    path('dashboard/<id>/',views.dashboard),
    path('yesterday_data/<id>/',views.yesterday_data),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
