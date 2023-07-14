from django.shortcuts import render
from django.db.models import Q, F, Func, ExpressionWrapper, Value, DecimalField, TextField
from django.db.models.functions import Concat
from django.http import HttpResponse
from store.models import Product, OrderItem, Order, Customer, Collection, CartItem, Cart
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from tags.models import TaggedItem
from django.contrib.contenttypes.models import ContentType
from django.db import transaction


def say_hello(request):

    return render(request, 'hello.html', {'name': 'Mosh'})
