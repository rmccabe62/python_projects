from django.shortcuts import render

def home(request):
    return render(request, 'AppCheckbook/index.html')

def create_account(request):
    return render(request, 'AppCheckbook/CreateNewAccount.html')

def balance(request):
    return render(request, 'AppCheckbook/BalanceSheet.html')

def transaction(request):
    return render(request, 'AppCheckbook/AddTransaction.html')

