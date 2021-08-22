import streamlit
from classify_page import load_model, show_classify_page

path_to_model = None
show_classify_page(load_model(path_to_model))