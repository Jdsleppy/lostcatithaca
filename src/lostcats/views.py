from bakery.views import BuildableTemplateView, BuildableListView, BuildableDetailView

from lostcats.models import LostCat
from lostcats.serializers import cat_serializer


class Home(BuildableTemplateView):
    template_name = "lostcats/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home_tab"] = True
        return context


class Robots(BuildableTemplateView):
    template_name = "lostcats/robots.txt"
    content_type = "text/plain"


class Map(BuildableListView):
    model = LostCat
    context_object_name = "cats"
    template_name = "lostcats/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["json_data"] = [cat_serializer(cat) for cat in context.get("cats", [])]
        context["metadata_title"] = "Map"
        context["map_tab"] = True
        return context


class CatDetail(BuildableDetailView):
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


class Gallery(BuildableListView):
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
