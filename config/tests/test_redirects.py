import pytest

##from django.urls import resolve
from django.test import RequestFactory

from config import redirect


def mk_page_data(name):
    return dict(
        title_en=name,
        slug_en=name,
        heading_en="test_%s heading" %name,
        description_en="%s description" % name,
    )


LANDING_DATA = mk_page_data('industries')
SECTOR_DATA_1 = mk_page_data('aerospace')
SECTOR_DATA_2 = mk_page_data('creative')


def setup_view(view, request, *args, **kwargs):
    """Mimic ``as_view()``, but returns view instance.
    Use this function to get view instances on which you can run unit tests,
    by testing specific methods."""
    # from https://stackoverflow.com/questions/33645780/how-to-unit-test-methods-inside-djangos-class-based-views
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


@pytest.mark.django_db
def test_needs_prefix_map():
    class TestRedirect(redirect.RedirectPrefixes):
        # no prefix_map attribute,
        pass

    with pytest.raises(AttributeError):
        TestRedirect()


@pytest.mark.django_db
def test_prefix_as_urls():
    class TestRedirect(redirect.RedirectPrefixedPage):
        prefix_map = [('int/a', 'a'), ('int', '/')]
        pass

    assert TestRedirect.as_urls() == 'int/a|int'


@pytest.mark.django_db
@pytest.mark.parametrize(
    'path, expected',
    (
        ('/planets/pluto/charon/', '/dwarf-planets/pluto/charon/'),
        ('/planets/pluto/', '/dwarf-planets/pluto/'),
        ('/planets/venus/', '/planets/venus/'),
        ('/asteroids/vesta/', '/asteroids/vesta/'),
    ),
)
def test_prefix_mappings(path, expected):
    class ExampleRedirector(redirect.RedirectPrefixes):
        prefix_map = [('planets/pluto/', 'dwarf-planets/pluto/')]

    def test_view(path):
        factory = RequestFactory()
        request = factory.get(path)
        view = setup_view(ExampleRedirector, request)
        view.get_redirect_url(view)
        return request

    request = test_view(path)
    assert request.path == expected



#
# @pytest.mark.django_db
# def test_setup_guide_landing_page(client):
#     from sector.models import SectorPage, SectorLandingPage
#     from wagtail.core.models import Page
#
#     root = Page.objects.filter(pk=1).get()
#     home = Page.objects.get(id=3)  # or better Page query
#
#     landing = SectorLandingPage(**LANDING_DATA)
#     home.add_child(instance=landing)
#
#     sector1 = SectorPage(**SECTOR_DATA_1)
#     sector2 = SectorPage(**SECTOR_DATA_2)
#
#     landing.add_child(instance=sector1)
#     landing.add_child(instance=sector2)
#
#
#     response = client.get('/industries/')
#     wsgi_request = response.wsgi_request
#
#     path_components = '/industries'.split('/')
#     route = root.specific.route(wsgi_request, path_components)
#     assert route.page == landing
#
#     import ipdb; ipdb.set_trace()
