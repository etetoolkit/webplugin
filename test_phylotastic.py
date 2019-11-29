from ete3_webserver import NodeActions, start_server
from ete3 import TreeStyle, TextFace, add_face_to_node, ImgFace, BarChartFace, faces,  AttrFace, SeqMotifFace, NodeStyle, NCBITaxa

# Custom ETE Tree styles and web actions

def connect_ncbitaxa():
    ncbi = NCBITaxa("/data/collaborations/spongilla_web/webplugin_py2/ete3_webserver/taxa.sqlite")
    return(ncbi)

def show_action_root(node):
    if node.up:
        return True
    return False

def run_action_root(tree, node):
    tree.set_outgroup(node)

def show_action_highlight(node):
    # Any node can be highlighted
    return True

def run_action_highlight(tree, node,taxid):
    node.img_style['bgcolor'] = 'pink'
    node.img_style['size'] = 8
    node.img_style['hz_line_width'] = 4

def show_action_change_style(node):
    return True

def run_action_change_style(tree, node, taxid):
    if tree.tree_style == ts:
        tree.tree_style = ts2
    else:
        tree.tree_style = ts
        
def show_action_delete_node(node):
    return True

def run_action_delete_node(tree,node,taxid):
    remove_node=node.detach()


def show_action_prune(node):    
    return True

select_taxids = set()
names = []

def run_action_prune(tree,node,taxid):
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


def custom_layout(node):
    
    ncbi=connect_ncbitaxa()
    
    if node.is_leaf():
        
        total_name = (node.name)
        #node.name=(node.name.split('|')[0])
        
        node_name = node.name.split('|')[0]
        name2taxid=ncbi.get_name_translator([node_name])
        taxid=name2taxid[node_name]
        lin = ncbi.get_lineage(int(taxid[0]))

        
        #seq_name = (total_name.split('.', 1)[-1])
        seq_name = (total_name.split('|')[1])
        other_info = (total_name.split('|')[2]) 
        
        aligned_name_face = TextFace(seq_name, fgcolor='brown', fsize=11)
        aligned_name_face.margin_top = 0
        aligned_name_face.margin_bottom = 0
        aligned_name_face.margin_left = 5
        add_face_to_node(aligned_name_face, node, column=2, position='aligned')
        
               
        if int('7742') in lin:
            N = TextFace('vertebrata', fsize=11, fgcolor="red")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')
            
        if int('6040') in lin:
            N = TextFace('porifera', fsize=11, fgcolor="green")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')  
          
        if int('6073') in lin:
            N = TextFace('cnidario', fsize=11, fgcolor="orange")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')    
        
        if int('33317') in lin:
            N = TextFace('protostomia', fsize=11, fgcolor="blue")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')    
        
        if int('10197') in lin:
            N = TextFace('Ctenophora', fsize=11, fgcolor="indigo")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')   
        
        if int('10226') in lin:
            N = TextFace('Ctenophora', fsize=11, fgcolor="sienna")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned') 
            
        if int('6157') in lin:
            N = TextFace('Platyhelminthes', fsize=11, fgcolor="olive")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned') 
            
        if int('7735') in lin:
            N = TextFace('Cephalochordata', fsize=11, fgcolor="skyblue")
            N.margin_left = 5
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned') 
        
             
        tax, seqs_info = other_info.split('.', 1)
        try:
            tax = int(tax)
        except:
            tax = tax
            
        
        if tax in lin:
            aligned_name_face = TextFace(seqs_info, fgcolor='grey', fsize=11)
            aligned_name_face.margin_top = 0
            aligned_name_face.margin_bottom = 0
            aligned_name_face.margin_left = 5
            add_face_to_node(aligned_name_face, node, column=4, position='aligned')
            
        else:
            aligned_name_face = TextFace(other_info, fgcolor='red', fsize=11)
            aligned_name_face.margin_top = 0
            aligned_name_face.margin_bottom = 0
            aligned_name_face.margin_left = 5
            add_face_to_node(aligned_name_face, node, column=4, position='aligned')
            
        
        
        seqFace = SeqMotifFace(node.sequence, gap_format="blank")
        add_face_to_node(seqFace, node, column=5, position="aligned")
        
        node.img_style['size'] = 0
        #try:
        #    g_sym=gene_sym[sci_name]
        #    predNameFace = faces.TextFace(g_sym,fgcolor = "navy" , fsize=28)
        #    add_face_to_node(predNameFace, node, column=3, position="branch-right" )
        #except:
        #    predNameFace = faces.TextFace(' ',fgcolor="navy", fsize=28)
        #    add_face_to_node(predNameFace, node, column=3, position="branch-right")
            
            
        if node_name.startswith("Homo"):
            # Add an static face that handles the node name
            N = TextFace(node_name, fsize=11, fgcolor="red")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Spongilla"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            add_face_to_node(N, node, column=0, position = 'branch-right')
            
        elif node_name.startswith("Sycon"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Amphimedon"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Oscarella"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Gallus"):
            N = TextFace(node_name, fsize=11, fgcolor="red")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Branchiostoma"):
            N = TextFace(node_name, fsize=11, fgcolor="red")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Trichoplax"):
            N = TextFace(node_name, fsize=11, fgcolor="orange")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Nematostella"):
            N = TextFace(node_name, fsize=11, fgcolor="orange")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Hydra"):
            N = TextFace(node_name, fsize=11, fgcolor="orange")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Drosophila"):
            N = TextFace(node_name, fsize=11, fgcolor="blue")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Crassostrea"):
            N = TextFace(node_name, fsize=11, fgcolor="blue")
            add_face_to_node(N, node, column=0, position = 'branch-right')

        else:
            name_face = TextFace(node_name, fgcolor='#333333', fsize=11)
            name_face.margin_top = 0
            name_face.margin_bottom = 0
            add_face_to_node(name_face, node, column=0, position='branch-right')
            
        
    else:
        node.img_style['size'] = 3
        node.img_style['shape'] = 'square'
        
        if node.name:
            name_face = TextFace(node.name, fgcolor='grey', fsize=10)
            name_face.margin_bottom = 1
            add_face_to_node(name_face, node, column=0, position='branch-top')
        if node.support:
            support_face = TextFace(node.support, fgcolor='indianred', fsize=8)
            support_face.margin_bottom = 1
            add_face_to_node(support_face, node, column=0, position='branch-bottom')
            

        
orig_name={} 
for line in open("/data/collaborations/spongilla/conversion_3.tsv"):
    if line.strip() and not line.startswith("#"):
        prot_name=line.split("\t")[0]
        ori_name=line.split("\t")[1]
        orig_name[prot_name]=ori_name
        
gene_sym={}
for line in open("/data/collaborations/spongilla/subset_trees/mmseqs_swissprot/gene_sym.tsv"):
    line=line.rstrip()
    prot_name=line.split('\t')[0]
    g_sym=line.split('\t')[1]
    gene_sym[prot_name]=g_sym

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
actions.add_action('Prune tree', show_action_prune, run_action_prune)

start_server(node_actions=actions, tree_style=ts)
