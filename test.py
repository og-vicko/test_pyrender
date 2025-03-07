import streamlit as st
import trimesh
import pyrender
import time 

st.write("Hello world")
time.sleep(5)
fuze_trimesh = trimesh.load('examples/models/coffee_cup_obj.obj')
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
scene = pyrender.Scene()
scene.add(mesh)
st.pydeck_chart(pyrender.Viewer(scene, use_raymond_lighting=True))