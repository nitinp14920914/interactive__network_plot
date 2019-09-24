
'''Nitin k.chauhan under Lynngroup3.0'''
# usage $python plot.py input_edgelist_file output_file
#output will be created as .html open it in browser

#python3
#pip install pyvis
#pip install networkx

from pyvis.network import Network
import networkx as nx
import sys

g=Network(height=1080,width=1920) #can specify your screen resolution
g.toggle_hide_edges_on_drag(False)
g.barnes_hut()
#input
g.from_nx(nx.read_edgelist(sys.argv[1])) # convert graph component in networkx
#output
g.show(str(sys.argv[2])+".html")


