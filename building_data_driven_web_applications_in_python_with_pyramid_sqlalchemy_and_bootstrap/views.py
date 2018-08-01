from pyramid.view import view_config


@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(request):
    return {'project': 'building_data_driven_web_applications_in_python_with_pyramid_sqlalchemy_and_bootstrap'}
