from ete3 import TreeStyle, TextFace, add_face_to_node, ImgFace, BarChartFace, faces,  AttrFace, SeqMotifFace, NodeStyle, NCBITaxa

def connect_ncbitaxa():
    # ncbi = NCBITaxa("/data/collaborations/spongilla_web/webplugin_py2/ete3_webserver/taxa.sqlite")
    ncbi = NCBITaxa("./taxa.sqlite")
    return(ncbi)

def custom_layout(node):
    
    ncbi=connect_ncbitaxa()
    
    if node.is_leaf():
        
        total_name = (node.name)
        if not total_name or total_name == "":
            sys.stderr.write("Name of node is null or empty when creating custom layout.\n")
            return

        #seq_name = (total_name.split('.', 1)[-1])
        seq_name = (total_name.split('|')[1])
        other_info = (total_name.split('|')[2]) 
        
        aligned_name_face = TextFace(seq_name, fgcolor='brown', fsize=11)
        aligned_name_face.margin_top = 0
        aligned_name_face.margin_bottom = 0
        aligned_name_face.margin_left = 5
        add_face_to_node(aligned_name_face, node, column=2, position='aligned')
        
        #node.name=(node.name.split('|')[0])
        node_name = node.name.split('|')[0]
        if not node_name or node_name.strip() == "":
            sys.stderr.write("Node name is null or empty when creating custom layout.\n")
            return
        
        name2taxid=ncbi.get_name_translator([node_name])
        taxid=name2taxid[node_name]
        lin = ncbi.get_lineage(int(taxid[0]))
               
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
            
    return
            
def custom_treestyle():
    ts = TreeStyle()
    ts.layout_fn = custom_layout
    ts.show_leaf_name = False
    ts.branch_vertical_margin = 0
    ts.min_leaf_separation = 0
    return ts
