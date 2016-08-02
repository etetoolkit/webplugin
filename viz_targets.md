# targets

## Priority level 1
* shows clean square trees, economical with space
   * use space_test.nwk, display in < 8 vertical inches
   *ETE: The size of every ETE graphical element can be customize (Faces). Also the margins of each face*

* capacity up to 500 easily displayed
   * use capacity_test.nwk, display and navigate in < 2 seconds
   *ETE: it will depend on the complexity of the layout, but current tests are about 1 sec.*

* ability to display images on tips
   * use viz_sample7.nwk with thumbnails in images/
   *ETE: Possible using ImgFace. Can link a URL, but it will slow down the rendering. Better use local copy of the images.*

* ability to display terminal node information and link-outs
   * use viz_sample7.nwk with links in URL column of viz_sample7_data.csv
   *ETE: Not fully implemented in the demo, but possible.*

* control tip alignment
   * use space_test.nwk, show with and without tips aligned to the right
   *ETE: Check `add_face_to_node(..., position='aligned')` and `TreeStyle.draw_guiding_lines`*

* control line thickness and color
   * use viz_sample7.nwk with thin or thick lines
   *ETE: Check `node.img_style["hz_line_width"]` and related*

* export high-resolution graphics image
   * use capacity_test.nwk, save in resolution high enough to enlarge so that names are easily readable.  For successful example, see capacity_test.svg; unsuccessful example is capacity_test.jpg (resolution too low).   
   *ETE: PDF, SVG and PNG currently supported. Simply call tree.render("file.[png|svg|pdf]", ...)*

* supports a way to highlight clade
   * indicate "Cervidae" in viz_sample7.nwk
   *ETE: shown in the demo. You can place random text or graphics on top of branches.*
   * use vertical bar or curly brace, or enclose in colored rectangle
   *ETE: also possible. The demo simply changes the background color of the clade*

* supports a way to distinguish multiple clades
   * indicate "Cervidae" and "Bovidae" in viz_sample7.nwk
   *ETE: shown in the demo. You can place random text or graphics on top of branches.*

* align tips with data table
   * show viz_sample7.nwk with categorical data in trophic habit column of viz_sample7_data.csv
   *ETE: data should be preloaded in the script, so it can accessed by the layout functions. Information can be represented as a series of aligned text faces. Check example here: http://etetoolkit.org/static/img/gallery/birds400x400.png*

   * show viz_sample7.nwk with numeric data in body mass column of viz_sample7_data.csv
   *ETE: check examples here for inspiration http://etetoolkit.org/static/img/gallery/*

## Priority level 2 features
* ladderize
   * show ladder_test.nwk with and without ladderization
   *ETE: already in the ETE API. simply call tree.ladderize()*

* ability to associate information with internal node
   * show "Cervidae" label on ancestral Cervidae node
   *ETE: ETE reads NHX format, so any annotation can be transformed into a graphical element*
   * can be static or dynamic (float-over)
   *ETE: floating faces possible, althoug they dont always look good. Check `add_face_to_node(..., position="[float|float-behind]")`*

* ability to associate information with branch
   * show label "7 events" on branch leading to Cervidae  
   *ETE: same as before. Although ETE does not distinguish between node and branch attributes (except for node.support, which is always a branch feature.)*
   * can be static or dynamic (float-over)
   *ETE: see above*

* export vector graphics image
   * use capacity_test.nwk, see capacity_test.svg .    
   *ETE: `tree.render("test.svg", tree_style=ts)`*

* collapse clades
   * use viz_sample7.nwk, collapse Carnivora
   *ETE: possible dynamically while rendering. Set `node.img_style['draw_descendants'] = False`*

* re-order clades
   * use viz_sample7.nwk, swap Cervidae and Bovidae
   *ETE: `check node.swap_children()` or `node.sort_descendants(), tree.sort_descendants()`*

## Priority level 3 features
* export annotated tree in portable tree format (e.g., NeXML, NHX, PhyloXML)
  *ETE: NHX well supported. NexML and PhyloXML only decent support for reading.*
   * (needs community standard)

* some way to view larger trees (dynamic expansion, fish-eye, fractal, etc)
*ETE*: not possible at the moment, but we have several experiments.
* ability to serve as arbitrary controller
* ability to combine phylogeny with geographic locations on a map
