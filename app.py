import streamlit as st
from world_generator import generate_world
from lore_generator import generate_lore
from species_generator import generate_species
from utils import load_config

st.set_page_config(page_title='DREAMFORGE', layout='wide')
st.title('🌌 DREAMFORGE — Generative World Builder')

cfg = load_config()

seed = st.text_area('Seed prompt', value='A mist-covered archipelago where floating cities harvest storms.')
extra = st.text_area('Extra notes (optional)', value='Low technology, focus on trade and storms.')

if st.button('Generate World'):
    with st.spinner('Generating world (model may be downloaded on first run)...'):
        world = generate_world(seed)
        lore = generate_lore(seed)
        species = generate_species(seed)

    st.subheader('World Overview')
    st.markdown(world)

    st.subheader('Lore & Timeline')
    st.markdown(lore)

    st.subheader('Species & Ecosystems')
    st.markdown(species)

    st.download_button('Download world (md)', world, file_name='dreamforge_world.md')
