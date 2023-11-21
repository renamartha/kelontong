from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, tambah_jumlah_item, kurangi_jumlah_item, hapus_item, edit_product, get_product_json, add_product_ajax, delete_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id_item>/tambah_jumlah_item/', tambah_jumlah_item, name='tambah_jumlah_item'),
    path('product/<int:id_item>/kurangi_jumlah_item/', kurangi_jumlah_item, name='kurangi_jumlah_item'),
    path('product/<int:id_item>/hapus_item/', hapus_item, name='hapus_item'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-ajax/', delete_ajax, name='delete_ajax')
]