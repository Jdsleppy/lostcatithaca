from django.contrib.staticfiles.storage import staticfiles_storage


class MetadataFallbackMiddlewre:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_template_response(self, request, response):
        response.context_data[
            "metadata_image_uri_fallback"
        ] = request.build_absolute_uri(
            staticfiles_storage.url("lostcats/images/og-image.png")
        )

        return response
