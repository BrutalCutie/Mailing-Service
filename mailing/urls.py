from mailing import views

from mailing.apps import MailingConfig

from django.urls import path

app_name = MailingConfig.name


urlpatterns = [
    path('', views.MailingListView.as_view(), name='main_page'),
    path('mailing_new/', views.MailingCreateView.as_view(), name='mailing_new'),
    path('mailing_detail/<int:pk>/', views.MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_update/<int:pk>/', views.MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>/', views.MailingDeleteView.as_view(), name='mailing_delete'),

    path('receiver_list/', views.ReceiverListView.as_view(), name='receiver_list'),
    path('receiver_new/', views.ReceiverCreateView.as_view(), name='receiver_new'),
    path('receiver_detail/<int:pk>/', views.ReceiverDetailView.as_view(), name='receiver_detail'),
    path('receiver_update/<int:pk>/', views.ReceiverUpdateView.as_view(), name='receiver_update'),
    path('receiver_delete/<int:pk>/', views.ReceiverDeleteView.as_view(), name='receiver_delete'),

    path('message_list/', views.MessageListView.as_view(), name='message_list'),
    path('message_new/', views.MessageCreateView.as_view(), name='message_new'),
    path('message_detail/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>/', views.MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', views.MessageDeleteView.as_view(), name='message_delete'),


]
