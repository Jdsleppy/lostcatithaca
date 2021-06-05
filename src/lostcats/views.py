from django.core.exceptions import BadRequest
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView

from lostcats.forms import CatCreateForm, CatLocateForm
from lostcats.models import LostCat
from lostcats.serializers import cat_serializer


class Home(TemplateView):
    template_name = "lostcats/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home_tab"] = True
        return context


class Robots(TemplateView):
    template_name = "lostcats/robots.txt"
    content_type = "text/plain"


class Map(ListView):
    model = LostCat
    context_object_name = "cats"
    template_name = "lostcats/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["json_data"] = [cat_serializer(cat) for cat in context.get("cats", [])]
        context["metadata_title"] = "Map"
        context["map_tab"] = True
        return context


class CatDetail(DetailView):
    model = LostCat
    template_name = "lostcats/cat_detail.html"
    context_object_name = "cat"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context.get("cat")  # type: LostCat
        context["json_data"] = cat_serializer(cat)
        context["metadata_title"] = cat.title
        context["metadata_description"] = cat.description
        context["metadata_image_uri"] = self.request.build_absolute_uri(cat.image_url)
        context["metadata_image_alt"] = f"A LostCat titled {cat.title}"
        return context


class CatLocate(FormView):
    template_name = "lostcats/cat_locate.html"
    form_class = CatLocateForm


class CatCreate(CreateView):
    template_name = "lostcats/cat_create.html"
    form_class = CatCreateForm
    success_url = None  # will reverse the model objects absolute URL

    MISSING_COORDS_MESSAGE = "Missing latitude and longitude query params"

    def get_initial(self):
        initial = super().get_initial()

        if self.request.method == "GET":
            if any(x not in self.request.GET for x in ("latitude", "longitude")):
                raise BadRequest(self.MISSING_COORDS_MESSAGE)

            initial["latitude"] = self.request.GET["latitude"]
            initial["longitude"] = self.request.GET["longitude"]

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if any(x not in self.request.GET for x in ("latitude", "longitude")):
            raise BadRequest(self.MISSING_COORDS_MESSAGE)

        context["json_data"] = {
            "latitude": self.request.GET["latitude"],
            "longitude": self.request.GET["longitude"],
        }

        return context


class Gallery(ListView):
    model = LostCat
    context_object_name = "cats"
    template_name = "lostcats/gallery.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["metadata_title"] = "Gallery"
        context["elided_page_range"] = list(
            context["paginator"].get_elided_page_range(
                context["page_obj"].number, on_each_side=1, on_ends=1
            )
        )
        context["gallery_tab"] = True
        return context
