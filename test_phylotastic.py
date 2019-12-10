##

import sys

from ete3_webserver import NodeActions, start_server
from ete3 import TreeStyle, TextFace, add_face_to_node, ImgFace, BarChartFace, faces,  AttrFace, SeqMotifFace, NodeStyle, NCBITaxa
from ete_layout import connect_ncbitaxa, custom_layout


# Custom ETE Tree styles and web actions

##
# Actions to show

def show_action_root(node):
    if node.up:
        return True
    return False

def show_action_highlight(node):
    # Any node can be highlighted
    return True

def show_action_change_style(node):
    return True

def show_action_delete_node(node):
    return True

def show_action_prune(node):    
    return True

##
# Run actions

def run_action_root(tree, node, taxid):
    tree.set_outgroup(node)
    return
    
def toggle_highlight_node(node, prev_highlighted):
    
    if prev_highlighted:
        node.img_style['bgcolor'] = 'white'
        node.img_style['size'] = 0
        node.img_style['hz_line_width'] = 0
    else:
        node.img_style['bgcolor'] = 'pink'
        node.img_style['size'] = 8
        node.img_style['hz_line_width'] = 4

    node.highlighted = not prev_highlighted
    print(node.highlighted)
    
    return

def run_action_highlight(tree, node, taxid):

    if not "highlighted" in node.features:
        node.add_feature("highlighted", False)
        
    prev_highlighted = node.highlighted
    
    toggle_highlight_node(node, prev_highlighted)
    
    for child in node.traverse():
        if not "highlighted" in child.features:
            child.add_feature("highlighted", False)
        toggle_highlight_node(child, prev_highlighted)
        
    return

def run_action_change_style(tree, node, taxid):
    if tree.tree_style == ts:
        tree.tree_style = ts2
    else:
        tree.tree_style = ts
        
def run_action_delete_node(tree, node, taxid):
    parent = node.up
    remove_node = node.detach()
    
    if len(parent.get_children()) == 0:
        run_action_delete_node(tree, parent, taxid)
        
    return

def run_action_prune(tree,node,taxid):
    select_taxids = set()
    names = []
    
    ncbi=connect_ncbitaxa()
    tax = taxid.rstrip().split(",")
    for el in tax:
        select_taxids.add(int(el))
    for leaf in tree.get_leaves():
        name2taxid = ncbi.get_name_translator([leaf.name.split('|')[0]])
        taxid = name2taxid[leaf.name.split('|')[0]]
        if taxid[0] in select_taxids:
            names.append(leaf.name)
        
    tree.prune(names)



    
# Server configuration

ts = TreeStyle()
ts.layout_fn = custom_layout
ts.show_leaf_name = False
ts.branch_vertical_margin = 0
ts.min_leaf_separation = 0


ts2 = TreeStyle()

ts_coll = TreeStyle()

actions = NodeActions()

actions.add_action('Root here', show_action_root, run_action_root)
actions.add_action('Highlight', show_action_highlight, run_action_highlight)
actions.add_action('Change style', show_action_change_style, run_action_change_style)
actions.add_action('Delete node', show_action_delete_node, run_action_delete_node)
#actions.add_action('Prune tree', show_action_prune, run_action_prune)

start_server(node_actions=actions, tree_style=ts)
