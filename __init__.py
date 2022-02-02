import os

import streamlit as st
import streamlit.components.v1 as components

st.title("Test slidering")

# metode untuk release dan development
# false pada saat development
# true pada saat release

_RELEASE = False

if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _discrete_slider = components.declare_component(
        "discrete_slider",
        path=build_dir
    )
else:
    _discrete_slider = components.declare_component(
        "discrete_slider",
        url="http://localhost:3001"
    )

_discrete_slider = components.declare_component(
    "discrete_slider",
    url='http://localhost:3001/'
)

def discrete_slider(options,key=None):
    return _discrete_slider(options=options, default=0, key=key)


selected_value = discrete_slider(["twas", "brillig", "and", "the", "slithey", "toves"])
st.write(f"You selected: '{selected_value}'")


