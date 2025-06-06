from django.urls import path
from . import views

urlpatterns = [
    path("welcome", views.my_view, name="index"),
    path("real_home", views.real_home, name="real_home"),
    path("", views.home , name="home"),
    path("receive/", views.my_receive_view),
    path("receive_main/", views.my_receive_main_view, name="receive_main"),
    path('sender/create/', views.CreateSenderView.as_view(), name='create-sender'),
    path('senderid/<int:user>/', views.SenderIdView.as_view(), name='sender-id'),
    path('senders/', views.SenderListView.as_view(), name='list-sender-transactions'),
    path('recipients/', views.RecipientListView.as_view(), name='list-recipients'),
    path('recipient/create/', views.CreateRecipientView.as_view(), name='create-recipient'),
    path('transaction/create/', views.CreateTransactionView.as_view(), name='create-transaction'),
    path('transactions/', views.TransactionListView.as_view(), name='list-transactions'),
    path("sender/by_wallet/<str:wallet_address>/", views.SenderByWalletView.as_view(), name="get_sender_by_wallet"),
    path("recipient/by_email/<str:email>/", views.RecipientByEmailView.as_view(), name="get_recipient_by_email"),
    path("transaction/by_txid/<str:tx_hash>/", views.TransactionByIdView.as_view(), name="get_transaction_by_txid"),
    path("transaction/by_email/<str:to_receiver_email>/", views.TransactionByEmailListView.as_view(), name="get_transaction_by_email"),
    path("update/status/<str:tx_hash>/", views.UpdateTransactionStatusView.as_view(), name="update_transaction_status"),
    path('sender/update-wallet/<str:sender_id>/', views.UpdateWalletAddressView.as_view(), name='update-wallet'),
    path("email/send/", views.send_welcome_email, name="send_welcome_email"),
    path("sol/send/", views.send_sol, name="send_sol"),
    path("logout", views.logout_view, name="logout"),
    path('api/moonpay-key/', views.get_moonpay_key),

]

# Compare this snippet from lazr/lazr/urls.py:
# from django.contrib import admin