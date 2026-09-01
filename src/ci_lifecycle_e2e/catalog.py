from jinja2 import Template
import yaml


CATALOG_TEMPLATE = Template("Items: {{ items | join(', ') }}")


def render_catalog(document: str) -> str:
    catalog = yaml.safe_load(document) or {}
    return CATALOG_TEMPLATE.render(items=catalog.get("items", []))
