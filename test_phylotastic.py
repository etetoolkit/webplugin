from ete3_webserver import NodeActions, start_server
from ete3 import TreeStyle, TextFace, add_face_to_node, ImgFace, BarChartFace

# Custom ETE Tree styles and web actions

def show_action_root(node):
    if node.up:
        return True
    return False
def run_action_root(tree, node):
    tree.set_outgroup(node)

def show_action_highlight(node):
    # Any node can be highlighted
    return True

def run_action_highlight(tree, node):
    node.img_style['bgcolor'] = 'pink'
    node.img_style['size'] = 8
    node.img_style['hz_line_width'] = 4


def custom_layout(node):
    if node.is_leaf():
        aligned_name_face = TextFace(node.name, fgcolor='olive', fsize=14)
        add_face_to_node(aligned_name_face, node, column=2, position='aligned')
        name_face = TextFace(node.name, fgcolor='#333333', fsize=11)
        add_face_to_node(name_face, node, column=2, position='branch-right')
        node.img_style['size'] = 0

        if node.name in tip2info:
            # For some reason img urls are very slow!
            #img_face = ImgFace(tip2info[node.name][0], is_url=True)
            #add_face_to_node(img_face, node, column=4, position='branch-right')
            habitat_face = TextFace(tip2info[node.name][2], fsize=11, fgcolor='white')
            habitat_face.background.color = 'steelblue'
            habitat_face.margin_left = 3
            habitat_face.margin_top = 3
            habitat_face.margin_right = 3
            habitat_face.margin_bottom = 3
            add_face_to_node(habitat_face, node, column=3, position='aligned')
    else:
        node.img_style['size'] = 4
        node.img_style['shape'] = 'square'
        if node.name:
            name_face = TextFace(node.name, fgcolor='grey', fsize=10)
            name_face.margin_bottom = 2
            add_face_to_node(name_face, node, column=0, position='branch-top')
        if node.support:
            support_face = TextFace(node.support, fgcolor='indianred', fsize=10)
            add_face_to_node(support_face, node, column=0, position='branch-bottom')

tip_info_csv = """
Rangifer_tarandus,http://eol.org/pages/328653/overview,109.09,herbivore
Cervus_elaphus,http://eol.org/pages/328649/overview,240.87,herbivore
Bos_taurus,http://eol.org/pages/328699/overview,618.64,herbivore
Ovis_orientalis,http://eol.org/pages/311906/overview,39.1,herbivore
Suricata_suricatta,http://eol.org/pages/311580/overview,0.73,carnivore
Cistophora_cristata,http://eol.org/pages/328632/overview,278.9,omnivore
Mephitis_mephitis,http://eol.org/pages/328593/overview,2.4,omnivore"""
tip2info = {}
for line in tip_info_csv.split('\n'):
    if line:
        name, url, mass, habit = map(str.strip, line.split(','))
        tip2info[name] = [url, mass, habit]


# Server configuration

ts = TreeStyle()
ts.layout_fn = custom_layout
ts.show_leaf_name = False
actions = NodeActions()

actions.add_action('Root here', show_action_root, run_action_root)
actions.add_action('Highlight', show_action_highlight, run_action_highlight)

start_server(node_actions=actions, tree_style=ts)
