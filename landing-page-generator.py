import streamlit as st
import random

def generate_landing_page(business_type, customer_base, geography, industry, color_scheme):
    # Define color schemes
    color_schemes = {
        'Professional': {'primary': '#2C3E50', 'secondary': '#ECF0F1', 'accent': '#3498DB'},
        'Vibrant': {'primary': '#FF4B2B', 'secondary': '#FFFFFF', 'accent': '#FFD700'},
        'Natural': {'primary': '#2ECC71', 'secondary': '#F5F5F5', 'accent': '#27AE60'},
        'Elegant': {'primary': '#6C5CE7', 'secondary': '#FFFFFF', 'accent': '#A29BFE'}
    }
    
    colors = color_schemes[color_scheme]
    
    # Customer base specific content
    cta_text = "Start Now" if customer_base == "Small (< 100)" else "Schedule Consultation" if customer_base == "Medium (100-1000)" else "Enterprise Solutions"
    
    # Geography specific content
    timezone_note = ""
    if geography == "Global":
        timezone_note = "<p>24/7 Support Across All Time Zones</p>"
    elif geography == "Regional":
        timezone_note = "<p>Dedicated Regional Support During Business Hours</p>"
    
    # Industry specific features
    industry_features = {
        "Technology": ["Cloud Integration", "API Access", "Real-time Analytics"],
        "Healthcare": ["HIPAA Compliant", "Patient Portal", "Medical Records Integration"],
        "Retail": ["Inventory Management", "POS Integration", "Customer Loyalty Programs"],
        "Finance": ["Secure Transactions", "Compliance Tools", "Risk Assessment"]
    }
    
    features = industry_features.get(industry, ["Custom Solutions", "24/7 Support", "Expert Consultation"])
    
    # Generate the HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{business_type} - Welcome</title>
        <style>
            :root {{
                --primary-color: {colors['primary']};
                --secondary-color: {colors['secondary']};
                --accent-color: {colors['accent']};
            }}
            
            body {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: var(--secondary-color);
                color: #333;
            }}
            
            header {{
                background-color: var(--primary-color);
                color: white;
                padding: 2rem;
                text-align: center;
            }}
            
            .hero {{
                padding: 4rem 2rem;
                text-align: center;
                background-color: var(--secondary-color);
            }}
            
            .features {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                padding: 4rem 2rem;
                background-color: white;
            }}
            
            .feature {{
                text-align: center;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            
            .cta {{
                background-color: var(--accent-color);
                color: white;
                padding: 1rem 2rem;
                border-radius: 4px;
                text-decoration: none;
                display: inline-block;
                margin-top: 2rem;
                font-weight: bold;
            }}
            
            footer {{
                background-color: var(--primary-color);
                color: white;
                text-align: center;
                padding: 2rem;
                margin-top: 4rem;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{business_type}</h1>
            <p>Transforming {industry} Through Innovation</p>
        </header>
        
        <section class="hero">
            <h2>Welcome to the Future of {industry}</h2>
            <p>Serving {customer_base} customers with specialized solutions</p>
            {timezone_note}
            <a href="#contact" class="cta">{cta_text}</a>
        </section>
        
        <section class="features">
    """
    
    # Add features dynamically
    for feature in features:
        html += f"""
            <div class="feature">
                <h3>{feature}</h3>
                <p>Discover how our {feature.lower()} can transform your business operations and drive growth.</p>
            </div>
        """
    
    html += """
        </section>
        
        <footer>
            <p>Contact us to learn more about our solutions</p>
            <a href="#contact" class="cta">Get Started</a>
        </footer>
    </body>
    </html>
    """
    
    return html

def main():
    st.title("Marketing Landing Page Generator")
    st.write("Create a customized landing page for your business")
    
    # Input fields
    business_type = st.text_input("Business Name/Type", "Your Business Name")
    
    customer_base = st.selectbox(
        "Customer Base Size",
        ["Small (< 100)", "Medium (100-1000)", "Enterprise (1000+)"]
    )
    
    geography = st.selectbox(
        "Geographic Reach",
        ["Local", "Regional", "Global"]
    )
    
    industry = st.selectbox(
        "Industry",
        ["Technology", "Healthcare", "Retail", "Finance", "Other"]
    )
    
    color_scheme = st.selectbox(
        "Color Scheme",
        ["Professional", "Vibrant", "Natural", "Elegant"]
    )
    
    if st.button("Generate Landing Page"):
        html_code = generate_landing_page(
            business_type,
            customer_base,
            geography,
            industry,
            color_scheme
        )
        
        # Preview
        st.subheader("Preview")
        st.components.v1.html(html_code, height=600)
        
        # Code display
        st.subheader("Generated HTML Code")
        st.code(html_code, language="html")
        
        # Download button
        st.download_button(
            label="Download HTML",
            data=html_code,
            file_name="landing_page.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()
