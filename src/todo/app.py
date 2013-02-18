import grok

from todo import resource

class Todo(grok.Application, grok.Container):
    todolists = [{
        'title':'Daily tasks for Grok',
        'description':'A list of tasks that Grok does everyday',
        'items':['Clean cave', 'Hunt breakfast', 'Sharpen ax']
        }]

class Index(grok.View):
    def update(self):
        resource.style.need()
