import gzip
import logging as log
#from StringIO import StringIO
from io import StringIO, BytesIO
from bottle import (run, get, post, request, route, response, abort, hook,
                    error, HTTPResponse)

from .tree_handler import WebTreeHandler, NodeActions, TreeStyle, NCBITaxa



LOADED_TREES = {}
COMPRESS_DATA = True
COMPRESS_MIN_BYTES = 10000
TREE_HANDLER = WebTreeHandler

def web_return(html, response):
    if COMPRESS_DATA and len(html) >= COMPRESS_MIN_BYTES:
        #chtmlF = StringIO()
        chtmlF = BytesIO()
        z = gzip.GzipFile(fileobj=chtmlF, mode='w')
        
        z.write(bytes(html,'utf-8'))
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
    alg = source_dict.get('alg', '').strip()
    treeid = source_dict.get('treeid', '').strip()
    
    taxid = source_dict.get('taxid', '').strip()

    if not newick or not treeid:
        return web_return('No tree provided', response)


    h = TREE_HANDLER(newick, alg, taxid, treeid, DEFAULT_ACTIONS, DEFAULT_STYLE)
    LOADED_TREES[h.treeid] = h

    # Renders initial tree
    img = h.redraw()
    return web_return(img, response)

@post('/get_actions')
def get_action():
    if request.json:
        source_dict = request.json
    else:
        source_dict = request.POST
        

    treeid = source_dict.get('treeid', '').strip()
    nodeid = source_dict.get('nodeid', '').strip()
    if treeid and nodeid:
        html = "<ul class='ete_action_list'>"
        h = LOADED_TREES[treeid]
        for aindex, aname in h.get_avail_actions(nodeid):
            html += """<li><a  onClick="run_action('%s', '%s', '%s', '%s');" >%s</a></li>""" %(treeid, nodeid, '', aindex, aname)
        html += "</ul>"
    return web_return(html, response)

@post('/run_action')
def run_action():
    if request.json:
        source_dict = request.json
    else:
        source_dict = request.POST
        
    treeid = source_dict.get('treeid', '').strip()
    nodeid = source_dict.get('nodeid', '').strip()
    faceid = source_dict.get('faceid', '').strip()
    aindex = source_dict.get('aindex', '').strip()

    if treeid and nodeid and aindex:
        h = LOADED_TREES[treeid]
        h.run_action(aindex, nodeid)
        img = h.redraw()

    return web_return(img, response)

DEFAULT_ACTIONS = None
DEFAULT_STYLE = None

def start_server(node_actions=None, tree_style=None, host="localhost", port=8989):
    global DEFAULT_STYLE, DEFAULT_ACTIONS
    
    #if ncbi:
    #    NCBI = ncbi
    #else:
    #    NCBI = connect_ncbitaxa()
    
    if node_actions:
        DEFAULT_ACTIONS = node_actions
    else:
        DEFAULT_ACTIONS = NodeActions()

    if tree_style:
        DEFAULT_STYLE = tree_style
    else:
        DEFAULT_STYLE = TreeStyle()

    run(host=host, port=port)
