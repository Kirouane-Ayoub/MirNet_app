import streamlit as st 
import MirNet


with st.sidebar:
    st.image("icon.png")
    sa_ve = st.radio("Do You want to save Results ?" , ("Yes" , "No"))
    if sa_ve == "Yes" : 
        save = True
    else : 
        sa_ve = False

tab0 , tab1 = st.tabs(["Home" , "MIRNet"])

with tab0 : 
    st.header("Low-light image enhancement using MIRNet")
    st.image("mirnet_architecture.png")
    st.write("""
    With the goal of recovering high-quality image content from its degraded version, image restoration enjoys numerous applications,
    such as in photography, security, medical imaging, and remote sensing. In this example, we implement the MIRNet model for low-light
    image enhancement, a fully-convolutional architecture that learns an enriched set of features that combines contextual information 
    from multiple scales, while simultaneously preserving the high-resolution spatial details.
    """)
    st.image("mirnet_21_0.png")


with tab1 :
    file_u = st.file_uploader("Upload Your Low-light image : " , type=("png" , "jpg"))
    if file_u : 
        name = file_u.name 
    if st.button("Start"):
        with st.spinner("Wait For it ..."):
            output_image , low_light_img = MirNet.Mirnet(path=name , save=save)
            col1 , col2 = st.columns(2)
            with col1 : 
                st.write("Originale Image")
                st.image(low_light_img)
            with col2 : 
                st.write("The Enhanced Image")
                st.image(output_image)
            st.success("Done!" , icon="✅")
