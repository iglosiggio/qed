from django import template

from enunciados.utils import enunciados_url_parser

register = template.Library()

register.simple_tag(enunciados_url_parser.url_enunciado)
register.simple_tag(enunciados_url_parser.url_editar_enunciado)
register.simple_tag(enunciados_url_parser.url_versiones_enunciado)
