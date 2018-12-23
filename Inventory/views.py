from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class DeviceList(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class DeviceGroupList(APIView):
    def get(self, request):
        devicegroups = DeviceGroup.objects.all()
        serializer = DeviceGroupSerializer(devicegroups, many=True)
        return Response(serializer.data)

class IndexView(generic.ListView):
    template_name = "Inventory/index.html"
    def get_queryset(self):
        return DeviceGroup.objects.all()

class DeviceIndex(generic.ListView):
    template_name = "Inventory/device_index.html"
    def get_queryset(self):
        return Device.objects.all()

class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = "Inventory/device_detail.html"

class GroupDetailView(generic.DetailView):
    model = DeviceGroup
    template_name = "Inventory/detail.html"

class GroupCreate(CreateView):
    model = DeviceGroup
    fields = ['groupname', 'description']

class DeviceCreate(CreateView):
    model = Device
    fields = ['IP_Address', 'hostname', 'devicegroups']

class GroupUpdate(UpdateView):
    model = DeviceGroup
    fields = ['groupname', 'description']

class DeviceUpdate(UpdateView):
    model = Device
    fields = ['IP_Address', 'hostname', 'devicegroups']

class GroupDelete(DeleteView):
    model = DeviceGroup
    success_url = reverse_lazy('index')
    fields = ['groupname', 'description']

class DeviceDelete(DeleteView):
    model = Device
    success_url = reverse_lazy('device_index')
    fields = ['IP_Address', 'hostname', 'devicegroups']

def search(request):
    template = 'Inventory/searchD.html'
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            results = DeviceGroup.objects.filter(Q(groupname__icontains=query) | Q(description__icontains=query))
            if results:
                return render(request,template, {'results':results})
            else:
                messages.error(request, 'No groups found')
    return render(request, template, {'results': results})

def home(request):
    return render(request, 'Inventory/home.html', {})

class UserFormView(View):
    form_class = UserForm
    template_name = 'Inventory/UserRegistrationForm.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
                # save the field values locally in an object
            user = form.save(commit=False)
                # clean and normalize the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(user.password)
            user.save()
            # Authentication
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
        return render(request, self.template_name, {'form': form})

class Login_View(FormView):
    form_class = AuthenticationForm
    template_name = 'Inventory/Loginpage.html'

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
           if user.is_active:
               login(request, user)
               return render(request, 'Inventory/home.html' , {'user':user})
           else:
               return HttpResponse("Inactive user.")
        messages.error(request, 'Invalid Credentials')
        return render(request, self.template_name, {'form': form})

class Logout_View(View):
    def get(self, request):
        logout(request)
        return redirect('login')
