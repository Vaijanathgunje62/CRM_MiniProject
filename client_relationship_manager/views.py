from pyexpat.errors import messages
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Client
from .forms import CreateClientForm, UpdateClientForm
from django.contrib import messages


# Create your views here.

class HomeView(ListView):
    paginate_by = 3
    model = Client
    template_name = "index.html"
    
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(owner=self.request.user)

class SearchResultsView(ListView):
    model = Client
    template_name = "search_results.html"
    context_object_name = "results"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            results = Client.objects.filter(
                Q(owner=self.request.user) 
                & (Q(name__icontains=query)
                | Q(email__icontains=query))
            )
            return results



class CreateClientView(CreateView):
    model = Client
    form_class = CreateClientForm
    template_name = "create_client.html"
    
    def get_success_url(self):
        messages.success(self.request, "Client created.")
        return reverse("crm:detail-client", args=[self.object.id])

    def form_valid(self, form,commit=True):
        user = form.save(commit=False)
        user.owner =self.request.user
        if commit:
            user.save()
        return super().form_valid(form)


class DetailClientView(DetailView):
    model = Client
    template_name = "detail_client.html"


class UpdateClientView(UpdateView):
    model = Client
    form_class = UpdateClientForm
    template_name = "update_client.html"
    
    def get_success_url(self):
        messages.success(self.request, "Client updated.")
        return reverse("crm:detail-client", args=[self.object.id])


class DeleteClientView(DeleteView):
    model = Client
    template_name = "delete_client.html"
    
    def get_success_url(self):
        messages.success(self.request, "Client deleted.")
        return reverse("crm:index")