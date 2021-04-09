import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

class Template:
    templates_name = ""
    context = None
    def __init__(self, templates_name="",context=None,*arg,**kwargs):
        self.templates_name = templates_name
        self.context = context

    def get_template(self):
        template_path = os.path.join(TEMPLATE_DIR, self.templates_name)
        if not os.path.exists(template_path):
            raise Exception("This path does not exist")
        template_string = ""
        with open(template_path, "r")as my_file:
            template_string = my_file.read()
        return template_string

    def render(self, context=None):
        render_ctx = None
        if self.context != None:
            render_ctx = self.context
        
        if not isinstance(render_ctx, dict):
            render_ctx = {}
        template_string = self.get_template()
        return template_string.format(**render_ctx)

    