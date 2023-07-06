from .models import *
menu= [{'index':'Резюме','acad':'Системы САПР', 'arbeit':'Мои проекты','programm':'Мои программы','feedback':'Обратная связь '} ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context=kwargs


        cats = Category.object.all()
        context['menu']=menu
        context['cats']