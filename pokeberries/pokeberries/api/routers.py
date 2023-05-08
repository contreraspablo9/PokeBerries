from rest_framework.routers import DefaultRouter

class PokeberriesRouter(DefaultRouter):
    """
    Wrap DRF's DefaultRouter to return an alphabetized list of endpoints.
    """
    def get_api_root_view(self, api_urls=None):
        api_root_dict = {}
        list_name = self.routes[0].name
        for prefix, viewset, basename in sorted(self.registry, key=lambda x: x[0]):
            api_root_dict[prefix] = list_name.format(basename=basename)

        return self.APIRootView.as_view(api_root_dict=api_root_dict)
