import grok

from todo import resource

class Todo(grok.Application, grok.Container):
    pass

class Index(grok.View):
    def update(self):
        resource.style.need()
