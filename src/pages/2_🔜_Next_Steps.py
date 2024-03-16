import streamlit as st
import os 

st.set_page_config(page_icon="🔜")

st.title("Next Steps")


st.markdown(
    """
    ## Next Steps

    We are aware that this model is not perfect and obviously can never capture the full breadth of why car accidents are caused and what leads to them being severe. However, we will try our hardest to strive towards perfection, and build as accurate a model as possible. 

    The first step in doing so is to gather more data towards improving our model. We have already tried several types of classification models, so we think that our underlying code is currently close to optimal. However, if we truly want to extend the model's use to regions where it can make an impact, we need to gather data from these areas. 

    As a first step towards this notion, we have contacted the City of San Diego's Traffic Police Department, asking them to kindly share road data with us. Hopefully, this will be our first stepping stone into building a working, usable service for the citizens of San Diego.
    """
)

path = os.path.dirname(__file__)

st.image(path + '/email_draft.jpeg', caption='Our Email to SDPD')
