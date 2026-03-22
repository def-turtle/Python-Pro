
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
import json
from django.forms.models import model_to_dict

class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.select_related('user').all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

@csrf_exempt
def orders(request):
    if request.method == 'GET':
        data = list(Order.objects.values())
        return JsonResponse({'orders': data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        data['user'] = user
        order = Order.objects.create(**data)
        return JsonResponse(model_to_dict(order), status=201)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def order_detail(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     user_id = data.get('user')
    #     user = User.objects.get(id=user_id)
    #     data['user'] = user
    #     order = Order.objects.create(**data)
    #     return JsonResponse({'id': order.id}, status=201)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(order))

    elif request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        user_id = data.get('user')
        if 'user' in data:
            try:
                data['user'] = User.objects.get(id=data['user'])
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)
        for key, value in data.items():
            if hasattr(order, key):
                setattr(order, key, value)
        order.save()
        return JsonResponse(model_to_dict(order))

    elif request.method == 'DELETE':
        order.delete()
        return JsonResponse({'deleted': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)
@csrf_exempt
def group(request):
    
    if request.method == 'GET':
        data = list(Group.objects.values())
        return JsonResponse({'groups': data})

    if request.method == 'POST':
        data = json.loads(request.body)
        group = Group.objects.create(**data)
        return JsonResponse({'id': group.id}, status=201)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def group_detail(request, id):
    try:
        group = Group.objects.get(id=id)
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        data = {
            "id": group.id,
            "name": group.name,
        }
        return JsonResponse(data)
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     user_id = data.get('user')
    #     user = User.objects.get(id=user_id)
    #     data['user'] = user
    #     group = Group.objects.create(**data)
    #     return JsonResponse({'id': group.id}, status=201)
    if request.method == 'GET':

        return JsonResponse(model_to_dict(group))

    elif request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        
        for key, value in data.items():
            setattr(group, key, value)
        group.save()
        return JsonResponse({"id": group.id, "name": group.name})

    elif request.method == 'DELETE':
        group.delete()
        return JsonResponse({'deleted': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)