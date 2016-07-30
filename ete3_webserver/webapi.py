import time
import gzip
import logging as log
from StringIO import StringIO
from bottle import (run, get, post, request, route, response, abort, hook,
                    error, HTTPResponse)


LOADED_TREES = {}
COMPRESS_DATA = True
COMPRESS_MIN_BYTES = 10000

def web_return(html, response):
    if COMPRESS_DATA and len(html) >= COMPRESS_MIN_BYTES:
        chtmlF = StringIO()
        z = gzip.GzipFile(fileobj=chtmlF, mode='w')
        z.write(html)
        z.close()
        chtmlF.seek(0)
        html = chtmlF.read()
        log.info('returning compressed %0.3f KB' %(len(html)/1024.))
        response.set_header( 'Content-encoding', 'gzip')
        response.set_header( 'Content-length', len(html))
    else:
        log.info('returning %0.3f KB' %(len(html)/1024.))
    return html


# THESE ARE THE WEB SERVICES PROVIDING DATA TO THE WEB AND API
@error(405)
def method_not_allowed(res):
    if request.method == 'OPTIONS':
        new_res = HTTPResponse()
        new_res.headers['Access-Control-Allow-Origin'] = '*'
        new_res.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
        new_res.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        return new_res
    res.headers['Allow'] += ', OPTIONS'
    return request.app.default_error_handler(res)

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'

@route('/status')
def server_status():
    return web_return('alive', response)

# WEB API FUNCTIONALITY
@post('/get_tree_image')
def get_tree_image():
    ''' Requires a POST param "newick" containing the tree to be loaded. '''

    if request.json:
        source_dict = request.json
    else:
        source_dict = request.POST
    newick = source_dict.get('newick', '').strip()

    if not newick:
        return web_return('No tree provided', response)

    print newick
    h = WebTreeHandler(newick)
    LOADED_TREES[h.__hash__] = h

    # Renders initial tree

    img = h.redraw()
    return web_return(img, response)

@route('/update_tree/<treeid>/<nodeid>/<action>')
def test_change(treeid, nodeid, action):
    t = TREES[treeid]
    nodeid = int(nodeid)
    found = False
    for target_node in t.traverse():
        if nodeid == target_node.__id:
            found = True
            break
    if not found:
        return webr_eturn('<b>Node not found</b>', response)


@route('/action/<nodeid>/faceid/<action>')
def run_action(treeid, nodeid, action):
    action_fn = handler.gettattr(action, nodeid)
    new_img, status, data = action(params)
    return new_img

def list_actions(treeid, nodeid, faceid):
    pass

from ete3 import Tree
class WebTreeHandler(object):
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

if __name__ == "__main__":
    run(host="localhost", port=8989, server='cherrypy')
