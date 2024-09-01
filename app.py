import streamlit as st
from PIL import Image

# Set the title of the app
st.set_page_config(page_title="Katrina Dela Peña's Portfolio", page_icon=":star:", layout="wide")

st.title("My Autobiography & Portfolio")

# Create a sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select a page", ["Autobiography", "Portfolio", "Contact"])

# Autobiography page
if page == "Autobiography":
    st.header("About Me")
    st.image("profilepicture.jpg", width=250, use_column_width=False)  # Adjust image size
    st.write("""
    Hello! I'm Katrina Dela Peña, an enthusiastic IT student with a deep passion for technology and innovation.
    I’m dedicated to exploring the vast world of information technology and am constantly expanding my knowledge and skills.
    From an early age, I was captivated by the power of technology, which led me to pursue a career in IT. 
    Throughout my studies, I’ve been focusing on areas like software development, network security, and data analytics.
    """)
    
    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, C
    - **Web Development:** HTML, CSS, React
    - **Database:** MySQL
    """)

# Portfolio page
elif page == "Portfolio":
    st.header("Portfolio")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Project 1: CIT-U Event Management Platform")
        st.write("""
        Welcome to the Cebu Institute of Technology University (CIT-U) Event Management Platform,
        your gateway to the exciting world of events! We offer a specialized platform for event
        management that caters to the unique needs and interests of our university community.
        The platform allows users to create, manage, and participate in events, providing a seamless
        experience for students, faculty, and staff.
        """)
        st.image("project1.png", caption="CIT-U Event Management Platform", use_column_width=True)  

    with col2:
        st.subheader("Project 2: Visual Bookmarking Platform")
        st.write("""
        Designed and built a visual bookmarking platform website using HTML, CSS, and JavaScript
        that allows users to discover, save, and organize content visually, similar to Pinterest,
        enabling a personalized and intuitive way to manage and explore creative ideas.
        """)
      

# Contact page
elif page == "Contact":
    st.header("Contact Me")
    st.write("If you'd like to get in touch, feel free to reach out through the following channels:")

    st.markdown("""
    - **Email:** [delapenakatrina822@gmail.com](mailto:delapenakatrina822@gmail.com)
    - **GitHub:** [github.com/Kayegdp0802](https://github.com/Kayegdp0802)
    """)

    # Contact form
    st.subheader("Send me a message")
    contact_name = st.text_input("Your Name")
    contact_email = st.text_input("Your Email")
    contact_message = st.text_area("Your Message")
    if st.button("Send Message"):
        st.write("Thank you for your message! I'll get back to you soon.")

# Footer
st.sidebar.markdown("""
---
Katrina Dela Peña | IT Student
""")
