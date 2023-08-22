import requests
from jinja2 import FileSystemLoader,Environment

def get_data_from_api(api_url):
    response=requests.get(api_url)
    data=response.json()
    return data


def render_temp(template_mess,data):
    file_loading=FileSystemLoader(".")
    environ=Environment(file_loading)
    template=environ.get_template(template_mess)
    rendered_template=template.render(api_data=data)
    return rendered_template