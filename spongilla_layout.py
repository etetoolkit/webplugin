from ete3 import TreeStyle, TextFace, add_face_to_node, ImgFace, BarChartFace, faces,  AttrFace, SeqMotifFace, NodeStyle, NCBITaxa, PhyloTree

ncbi = None
orig_name = None
NCBIPATH = None
TABLEPATH = None

def init_layout(ncbipath, tablepath):
    global NCBIPATH, TABLEPATH
    NCBIPATH = ncbipath
    TABLEPATH = tablepath
    return

def custom_layout(node):
    global ncbi, NCBIPATH
    if not ncbi:
        ncbi = NCBITaxa(NCBIPATH)
    
    
    global orig_name, TABLEPATH
    if not orig_name:
        orig_name = {}
        with open(TABLEPATH) as tablefn:
            for line in tablefn:
                if line.strip() and not line.startswith("#"):
                    line_data = line.strip().split("\t")
                    name_in_tree=line_data[0]
                    name_to_show=line_data[2]
                    orig_name[name_in_tree]=name_to_show
    
        
    if node.is_leaf():
        
        total_name = (node.name)
        
        node_name = node.name.split('|')[0]
        name2taxid=ncbi.get_name_translator([node_name])
        taxid=name2taxid[node_name]
        lin = ncbi.get_lineage(int(taxid[0]))
        
        prot_info = (total_name.split('|')[2])#.split('.',1)[1]
        prot_id = prot_info.split('.', 1)[1]
        if len(prot_id) > 50:
            prot_id = prot_id[0:50]
        
        
        if prot_info in orig_name.keys():
            gene_name = orig_name[prot_info]
        
        else:
            gene_name = (total_name.split('|')[1])
        
        aligned_pname_face = TextFace(prot_id, fgcolor='grey', fsize=11)
        aligned_pname_face.margin_top = 0
        aligned_pname_face.margin_bottom = 0
        aligned_pname_face.margin_right = 20
        add_face_to_node(aligned_pname_face, node, column=1, position='branch-right')
        
        aligned_gname_face = TextFace(gene_name, fgcolor='black', fsize=11)
        aligned_gname_face.margin_top = 0
        aligned_gname_face.margin_bottom = 0
        aligned_gname_face.margin_left = 5
        add_face_to_node(aligned_gname_face, node, column=2, position='branch-right')
        
        seqFace = SeqMotifFace(node.sequence, gap_format="blank")
        seqFace.margin_left = 5
        add_face_to_node(seqFace, node, column=4, position="aligned")
        
        
        if  node_name.startswith("Homo"):
            # Add an static face that handles the node name
            N = TextFace(node_name, fsize=11, fgcolor="red")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Spongilla"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')
            
        elif  node_name.startswith("Sycon"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Amphimedon"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Oscarella"):
            N = TextFace(node_name, fsize=11, fgcolor="green")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Gallus"):
            N = TextFace(node_name, fsize=11, fgcolor="red")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Branchiostoma"):
            N = TextFace(node_name, fsize=11, fgcolor="red")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Trichoplax"):
            N = TextFace(node_name, fsize=11, fgcolor="orange")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node_name.startswith("Nematostella"):
            N = TextFace(node_name, fsize=11, fgcolor="orange")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Hydra"):
            N = TextFace(node_name, fsize=11, fgcolor="orange")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Drosophila"):
            N = TextFace(node_name, fsize=11, fgcolor="blue")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif  node_name.startswith("Crassostrea"):
            N = TextFace(node_name, fsize=11, fgcolor="blue")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0, position = 'branch-right')

        elif node.is_leaf():
            N = TextFace(node_name, fsize=11, fgcolor="black")
            N.margin_right= 20
            faces.add_face_to_node(N, node, column=0)
            
            
            
        if int('7742') in lin:
            N = TextFace('vertebrata', fsize=11, fgcolor="red")
            #N.margin_left = 20
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')
            
        if int('6040') in lin:
            N = TextFace('porifera', fsize=11, fgcolor="green")
            #N.margin_left = 20
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')  
          
        if int('6073') in lin:
            N = TextFace('cnidario', fsize=11, fgcolor="orange")
            #N.margin_left = 20
            N.background.color = "Linen"
            add_face_to_node(N, node, column=3, position = 'aligned')   
            
    
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
            

def spongilla_predraw(tree):
    taxa_list = ["Homo sapiens", "Crassostrea gigas", "Gallus gallus", "Branchiostoma floridae", "Drosophila melanogaster", "Hydra vulgaris", "Nematostella vectensis",
             "Trichoplax adhaerens", "Spongilla lacustris", "Oscarella carmela", "Amphimedon queenslandica", "Capsaspora owczarzaki", "Monosiga brevicollis",
             "Salpingoeca rosetta", "Sycon ciliatum"]
    
    R = tree.get_midpoint_outgroup()
    tree.set_outgroup(R)
    prune_list = []
    for leaf in tree:
        sci_name = leaf.name.split('|')[0]
        if sci_name in taxa_list:
               prune_list.append(leaf.name)
                
    #tree.prune(prune_list, preserve_branch_length=True)

           
        
def custom_treestyle():
    ts = TreeStyle()
    ts.layout_fn = custom_layout
    ts.show_leaf_name = False
    ts.branch_vertical_margin = 0
    ts.min_leaf_separation = 0
    return ts




