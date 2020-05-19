from ete3 import TreeStyle, TextFace, add_face_to_node, ImgFace, BarChartFace, faces,  AttrFace, SeqMotifFace, NodeStyle, NCBITaxa

#Image customization is performed through four elements:
    #a) TreeStyle, setting general options about the image (shape, rotation, etc.),
    #b) NodeStyle, which defines the specific aspect of each node (size, color, background, line type, etc.),
    #c) node faces.Face which are small pieces of extra graphical information that can be added to nodes(text labels, images, graphs, etc.)
    #d) a layout function, a normal python function that controls how node styles and faces are dynamically added to nodes.

def custom_layout(node):
    
    if node.is_leaf():
        #FACES IN LEAFS
        #Add face with node.name
        total_name = (node.name)
        aligned_name_face = TextFace(total_name, fgcolor='gray', fsize=11)
        add_face_to_node(aligned_name_face, node, column=0, position='branch-right')
        
        #if tree has an alignment, add a face with alignment
        if node.sequence:
            seqFace = SeqMotifFace(node.sequence, gap_format="blank")
            add_face_to_node(seqFace, node, column=1, position="aligned")
        
        
    else:
        #FACES IN INTERNAL NODES
        #Draws nodes as small blue squares of diameter equal to 3 pixels
        node.img_style['size'] = 3
        node.img_style['shape'] = 'square'
        
        #if internal node has a name, add a face
        if node.name:
            name_face = TextFace(node.name, fgcolor='brown', fsize=10)
            name_face.margin_bottom = 1
            add_face_to_node(name_face, node, column=0, position='branch-top')
        
        #if internal node has support (ej. boostrap), add a face
        if node.support:
            support_face = TextFace(node.support, fgcolor='indianred', fsize=8)
            support_face.margin_bottom = 1
            add_face_to_node(support_face, node, column=0, position='branch-bottom')

def custom_treestyle():
    #Add treestyle
    ts = TreeStyle()
    #use custom layout fuction
    ts.layout_fn = custom_layout
    #don't show leaf names (leaf names can be customized  in custom layout)
    ts.show_leaf_name = False
    return ts
  


