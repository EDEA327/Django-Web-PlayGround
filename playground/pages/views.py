from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import PageForm
from .models import Page


# Create your views here.
class StaffRequiredMixin(object):
    """This mixin requires the user to be a member of the staff. """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))

        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required,name="dispatch")
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

    #* Si quiero restringir la vista dde un usuario anonimo puedo hacerlo con.
    #* La porcion de ocdigo que esta debajo, pero esto no es escalable y se vuelver
    #* repetitivo pues tendria que hacerlo en todas las vistas que quiera restringir
    #* Para evitar la repeticion se usan los mixins.

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_staff:
    #         return redirect(reverse_lazy('admin:login'))

    #     return super(PageCreate,self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required,name="dispatch")
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffixed = '_update_form'

    def get_success_url(self):
        return  reverse_lazy('pages:update',args = [self.object.id]) + '?ok'

@method_decorator(staff_member_required,name="dispatch")
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')