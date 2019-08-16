from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def bid(request):
    """Allows a user to place a bid on an item and refreshes products page"""
    

    