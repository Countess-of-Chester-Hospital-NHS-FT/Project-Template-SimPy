import streamlit as st

st.title("Example Non-Elective Flow Simulation App")
st.header("(template)")

st.markdown("""
Welcome to an example discrete event simuation app. The app and
underlying model are being developed by the Data & Analytics team
at the Countess of Chester Hospital. This app is designed to help understand ...
. Please note that this is an example and results should not be used in decision making. 
We welcome any feedback on the tool.
""")

st.write("Head to the 'Run Simulation' page to get started.")

st.markdown("""
            
##### Example questions the model can provide evidence for:
            
(Replace with your own questions)
* Given x beds, how far does admitted length of stay have to reduce to meet 
particular waiting time targets for those queuing in ED? (Evidence based target)
* If we open 15 beds but keep admitted length of stay the same, what is the 
impact on ED waiting times and the various targets? (Evidence for a particular 
management strategy)

""")

st.markdown("""
##### Model diagram

The model simulates the system as illustrated in the flowchart below. For more
detail on how the model works see the 'More Information' page
""")

st.image("img/model_diagram.png")

