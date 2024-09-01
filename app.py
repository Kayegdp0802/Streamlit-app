import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(page_title="Katrina Dela Peña's Portfolio", page_icon=":star:", layout="wide")

# Apply custom CSS for styling
st.markdown("""
    <style>
    .main {background-color: #AAB396;}
    .sidebar .sidebar-content {background-color: #e0f7fa; padding: 1rem;}
    .stButton>button {background-color: #00796b; color: white; border-radius: 8px; padding: 0.5rem 1rem;}
    .stTextInput>div>input, .stTextArea>div>textarea {border: 2px solid #00796b; border-radius: 8px; padding: 0.5rem;}
    .stMarkdown {font-family: 'Arial', sans-serif;}
    h1, h2, h3 {color: #00796b;}
    .footer {text-align: center; padding: 7rem; color: #00796b;}
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.title("Katrina Dela Peña's Portfolio")

# Create a sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select a page", ["Autobiography", "Portfolio", "Contact"])

# Autobiography page
if page == "Autobiography":
    st.header("About Me")
    st.image("profilepicture.jpg", width=250, use_column_width=False, caption="Katrina Dela Peña")  # Adjust image size
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
    """, unsafe_allow_html=True)

# Portfolio page
elif page == "Portfolio":
    st.header("Portfolio")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="portfolio-section">', unsafe_allow_html=True)
        st.subheader("Project 1: CIT-U Event Management Platform")
        st.write("""
        Welcome to the Cebu Institute of Technology University (CIT-U) Event Management Platform,
        your gateway to the exciting world of events! We offer a specialized platform for event
        management that caters to the unique needs and interests of our university community.
        The platform allows users to create, manage, and participate in events, providing a seamless
        experience for students, faculty, and staff.
        """)
        st.image("project1.png", caption="CIT-U Event Management Platform", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="portfolio-section">', unsafe_allow_html=True)
        st.subheader("Project 2: Visual Bookmarking Platform")
        st.write("""
        Designed and built a visual bookmarking platform website using HTML, CSS, and JavaScript
        that allows users to discover, save, and organize content visually, similar to Pinterest,
        enabling a personalized and intuitive way to manage and explore creative ideas.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

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
    contact_name = st.text_input("Your Name", placeholder="Enter your name")
    contact_email = st.text_input("Your Email", placeholder="Enter your email")
    contact_message = st.text_area("Your Message", placeholder="Write your message here")
    if st.button("Send Message"):
        st.write("Thank you for your message! I'll get back to you soon.")

# Footer
st.markdown("""
    <div class="footer">
    <p>Katrina Dela Peña | IT Student</p>
    <p>Connect with me on <a href="https://github.com/Kayegdp0802" target="_blank" style="color: #00796b;">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)
