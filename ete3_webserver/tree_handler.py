from ete3 import Tree

class WebTreeHandler(object):

    actions = []

    def __init__(self, newick):
        self.tree = Tree(newick)
        # Initialze node internal IDs
        for index, n in enumerate(self.tree.traverse('preorder')):
            n._nid = index

    def redraw(self):
        base64_img, img_map = self.tree.render("%%return.PNG")

        html_img = """<img src="data:image/gif;base64,%s">""" %(base64_img)

        return html_img

    def layout_fn(self):
        pass

    def action_root(self, target):
        outgroup = target & target
        self.tree.set_outgroup(outgroup)


class TreeAction(object):
    def __init__(self, name, desc=''):
        self.name = name
        self.desc = ''

    def is_valid(self, node):
        pass

    def run(self, node, faceid):
        pass
