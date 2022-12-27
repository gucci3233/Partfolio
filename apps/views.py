from django.views.generic import ListView

from apps.models import Profile, AboutMe, MyPortfolio, DetailPort, ContactMe, SecondResume, LangImage


# Create your views here.

class indexListView(ListView):
    queryset = Profile.objects.first()
    template_name = 'apps/index.html'
    context_object_name = 'profile'


class AboutListView(ListView):
    queryset = AboutMe.objects.first()
    template_name = 'apps/about.html'
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['second'] = SecondResume.objects.first()
        context['ims'] = LangImage.objects.first()
        return context


class PortfolioListView(ListView):
    queryset = MyPortfolio.objects.all()
    template_name = 'apps/portfolio.html'
    context_object_name = 'portfolio'

    # paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['detail'] = DetailPort.objects.all()
        return context


class ContactListView(ListView):
    queryset = ContactMe.objects.first()
    template_name = 'apps/contact.html'
    context_object_name = 'contact'
