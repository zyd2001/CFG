import subprocess
import networkx as nx
import tempfile, os

def view(G, prefix = ''):
    fd, dot = tempfile.mkstemp(prefix=prefix, suffix='.dot')
    os.close(fd)
    nx.nx_agraph.write_dot(G, dot)
    subprocess.Popen(['/usr/bin/xdot', '{}'.format(dot)])
