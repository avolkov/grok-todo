import grok

from todo import resource

class Todo(grok.Application, grok.Container):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.next_id = 0
        self.title = 'To-Do list manager'
        self.todolists = []

    def add_list(self, title, description):
        id = str(self.next_id)
        self.next_id = self.next_id + 1
        self[id] = TodoList(title, description)

    def delete_list(self, list):
        del self[list]

class TodoList(grok.Container):
    def __init__(self, list_title, list_description):
        super(TodoList, self).__init__()
        self.next_id = 0
        self.title = list_title
        self.description = list_description

    def add_item(self, description):
        id = str(self.next_id)
        self.next_id = self.next_id + 1
        self[id] = TodoItem(description)

    def delete_item(self, item):
        del self[item]

    def update_items(self, items):
        for name,item in self.items():
            if name in items:
                self[item].checked = True
            else:
                self[item].checked = False
    def toggle_check(self):
        self.checked = not self.checked

class TodoItem(grok.Model):
    def __init__(self, item_description):
        super(self.__class__, self).__init__()
        self.description = item_description
        self.checked = False
    def toggle_check(self):
        self.checked = not self.checked

class TodoItemCheck(grok.View):
    grok.context(TodoItem)
    grok.name('check')
    

    def update(self, list_index, item_index):
        self.div_id = 'div_item_%s_%s' % (list_index, item_index)
        list_index = int(list_index)
        item_index = int(item_index)
        items = self.context.todolists[listinidex]['items']
        items[item_index]['checked'] = not items[ite_index]['checked']
    def render(self):
        return self.div_id

class TodoAddList(grok.View):
    grok.context(Todo)
    grok.name('addlist')

    def update(self, title, description):
        self.context.add_list(title, description)

    def render(self):
        self.redirect(self.url('index'))

class TodoDeleteList(grok.View):
    grok.context(Todo)
    grok.name('deletelist')

    def update(self, list):
        self.context.delete_list(list)
    def render(self):
        self.redirect(self.url('index'))

class TodoSetTitle(grok.View):
    grok.context(Todo)
    grok.name('settitle')

    def update(self, title):
        self.context.title = title
    def render(self):
        return self.context.title

class TodoListAddItem(grok.View):
    grok.context(TodoList)
    grok.name('additem')

    def update(self, description):
        self.context.add_item(description)
    def render(self):
        self.redirect(self.url(self.context.__parent__, 'index'))

class TodoListDeleteItem(grok.View):
    grok.context(TodoList)
    grok.name('deleteitem')
    
    def update(self, item):
        self.context.delete_item(item)
    def render(self):
        self.redirect(self.url(self.context.__parent__, 'index'))

class TodoListUpdateItems(grok.View):
    grok.context(TodoList)
    grok.name('updateitems')

    def update(self, items):
        self.context.update_items(items)
    def render(self):
        self.redirect(self.url(self.context.__parent__, 'index'))

class TodoItemCheck(grok.View):
    grok.context(TodoItem)
    grok.name('check')

    def update(self):
        self.div_id = 'div_item_%s_%s' % \
            (self.context.__parent__.__name__, self.context.__name__)
        self.context.toggle_check()
    def render(self):
        return self.div_id

class TodoIndex(grok.View):
    grok.context(Todo)
    grok.name('index')
