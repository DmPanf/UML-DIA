from tkinter import *
from tkinter import ttk
import tkinter as tk
import rdflib
from rdflib import *
#import plotly.graph_objects as go
from rdflib import URIRef, Graph, Namespace
from rdflib.plugins.parsers.notation3 import N3Parser
import re, os

root = Tk()
root.title("Treeview Structure")
#root.geometry("1200x680+50+20")

# file_location = os.path.dirname(os.path.abspath(__file__))
KB_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "KnowledgeBase_v01.n3")

g = rdflib.Graph()
result = g.parse(file=open(KB_path, mode="r"), format="text/n3")


treeview = ttk.Treeview(root)
#text1 = tk.Text(root, height = 20, width = 75)

#proc0
qres0 = g.query(
    """SELECT DISTINCT ?label ?class
       WHERE {
          ?class rdf:type classes:Process .
          ?class rdfs:label ?label .
       }""")

for row in qres0:
    a = str(row.asdict()['label'].toPython())
    aa = str(row.asdict()['class'].toPython())
    #print("%s is %s" % row)
    print(f"Label | {a}")
    print('=======process ind======')
    print(f"Address | {aa}\n")
    parent = treeview.insert('', 'end' ,a, text = a, values=(), open = True )

#proc01, proc02, proc03
qres1 = g.query(
    """SELECT DISTINCT ?label ?class
       WHERE {
          ?class prop:SubProcess ind:proc0 .
          ?class rdfs:label ?label .
       }""")

for row in qres1:
    b = str(row.asdict()['label'].toPython())
    bb = str(row.asdict()['class'].toPython())
    #print("%s is %s" % row)
    print(f"Label | {b}")
    print('=====process ind of sub process of proc0=====')
    print(f"Address | {bb}\n")
    treeview.insert(parent=parent, index='end', iid=b, text=b, values=("NODE_A0"), open = False) # iid - "Lable" which is used to inherite next instance

#proc11, proc12
qres2 = g.query(
    """SELECT DISTINCT ?label ?class
       WHERE {
          ?class prop:SubProcess ind:proc01 .
          ?class rdfs:label ?label .
       }""")

for row in qres2:
    c = str(row.asdict()['label'].toPython())
    cc = str(row.asdict()['class'].toPython())
    #print("%s is %s" % row)
    print(f"Label | {c}")
    print('=====process ind of sub process of proc01=====')
    print(f"Address | {cc}\n")
    treeview.insert('Data preparation', index='end', iid=c, text=c, values=("NODE_A1"), open = False) # iid - "Lable" which is used to inherite next instance

# proc21, proc22, proc23, proc24
qres3 = g.query(
    """SELECT DISTINCT ?label ?class
       WHERE {
          ?class prop:SubProcess ind:proc02 .
          ?class rdfs:label ?label .
       }""")

for row in qres3:
    d = str(row.asdict()['label'].toPython())
    dd = str(row.asdict()['class'].toPython())
    #print("%s is %s" % row)
    print(f"Label | {d}")
    print('=====process ind of sub process of proc02=====')
    print(f"Address | {dd}\n")
    treeview.insert("Intelligent System Architecture",'end', iid=d, text = d, values=("NODE_A2"), open = False) # iid - "Lable" which is used to inherite next instance

proclabel=[a, b, c, d]

treeview.config(column = ('Details'))
treeview.config(height = 10)
treeview.column('#0', width = 300)
treeview.column('Details', width = 300)

treeview.heading('#0', text = 'Process Names')
treeview.heading('Details', text = 'Details')


#text1.config(height=10)
treeview.pack()
#treeview.pack(fill='x')
#text1.pack()
#text1.pack(fill='x')
#btn1.pack()

root.mainloop()
