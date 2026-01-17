import streamlit as st

def apply_custom_style():
    """Injects custom CSS to style the Streamlit app."""
    st.markdown("""
        <style>
        /* Main Container & Background */
        .stApp {
            background: linear-gradient(to bottom right, #0e1117, #161b22);
            color: #fafafa;
        }
        
        /* Headers */
        h1, h2, h3 {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-weight: 700;
            color: #ffffff;
        }
        
        /* Metric Cards */
        div[data-testid="metric-container"] {
            background-color: #262730;
            border: 1px solid #464b5f;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
            transition: transform 0.2s;
        }
        
        div[data-testid="metric-container"]:hover {
            transform: scale(1.02);
            border-color: #00cc96;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #00cc96;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 24px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #00a87d;
            box-shadow: 0 4px 15px rgba(0,204,150,0.4);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #161b22;
            border-right: 1px solid #30363d;
        }

        /* Sidebar Navigation Text */
        section[data-testid="stSidebar"] .stMarkdown, 
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div {
            color: #ffffff !important;
        }
        
        /* Sidebar Links */
        button[kind="header"] {
           background-color: transparent !important;
           color: #ffffff !important;
        }

        div[data-testid="stSidebarNav"] a, div[data-testid="stSidebarNav"] span {
            color: #ffffff !important;
        }

        /* Prevent link decoration issues */
        a {
            text-decoration: none;
        }

        /* Custom Dividers */
        hr {
            border-color: #30363d;
        }
        </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Renders the common sidebar elements."""
    with st.sidebar:
        st.header("🔍 Smart Scout")
        st.markdown("---")
        # Automatic sidebar navigation handles page links now
        st.info("**Tip:** Use the filters on each page to narrow down your search.")
        st.markdown("---")
        st.caption("Built with ❤️ by Kishohar")
