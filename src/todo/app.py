import grok

from todo import resource

class Todo(grok.Application, grok.Container):
    todolists = []

class Index(grok.View):
    def update(self):
        form = self.request.form
        if 'new_list' in form:
            title = form['list_title']
            description = form['list_description']
            self.context.todolists.append({'title':title, 
                                           'description':description,
                                           'items':[]
                                         })
            return
        if 'list_index' in form:
            index = int(form['list_index'])
            items = self.context.todolists[index]['items']
            if 'new_item' in form:
                description = form['item_description']
                items.append(({'description':description, 'checked':False}))
                return
            elif 'update_list' in form:
                for item in range(len(items)):
                    if 'item_%s' % item in form:
                        items[item]['checked'] = True
                    else:
                        items[item]['checked'] = False
                return
            else:
                for item in range(len(items)):
                    if 'delete_%s' % item in form:
                        items.remove(items[item])
