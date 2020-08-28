from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.views.generic import ListView
from USER.decorators import staff_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from WEB.models import *
from KM.models import *

class SearchView(ListView):
        template_name = 'web/cari.html'
        count = 0
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context['count'] = self.count or 0
            context['query'] = self.request.GET.get('q')
            return context

        def get_queryset(self):
            request = self.request
            query = request.GET.get('q', None)

            if query is not None:
                staff_results = Staff.objects.search(query)
                berita_results = Berita.objects.search(query)
                acara_results = Acara.objects.search(query)
                publikasi_results = Publikasi.objects.search(query)

                # combine querysets
                queryset_chain = chain(
                    staff_results,
                    berita_results,
                    acara_results,
                    publikasi_results,

                    
                )

                qs = sorted(queryset_chain,
                            key=lambda instance: instance.pk,
                            reverse=True)
                self.count = len(qs)  # since qs is actually a list
                return qs
            return Berita.objects.none()

@method_decorator([login_required, staff_required], name='dispatch')
class SearchKMView(ListView):
    template_name = 'web/cari.html'
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            staff_results = Staff.objects.search(query)
            berita_results = Berita.objects.search(query)
            acara_results = Acara.objects.search(query)
            publikasi_results = Publikasi.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                staff_results,
                berita_results,
                acara_results,
                publikasi_results,

            )

            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Berita.objects.none()