import streamlit as st
import random
import openai
from typing import Dict, List
import json
import time

# Initialize OpenAI client (use dummy key here)
openai.api_key = "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"

class ContentAgent:
    """Agent responsible for generating marketing copy and content"""
    
    @staticmethod
    def generate_content(business_info: Dict) -> Dict:
        prompt = f"""Generate marketing content for a {business_info['business_type']} business in the {business_info['industry']} industry.
        Target customer base: {business_info['customer_base']}
        Geographic reach: {business_info['geography']}
        
        Please provide:
        1. A compelling headline
        2. A subheadline
        3. Three key value propositions
        4. A call to action
        
        Format as JSON with keys: headline, subheadline, value_props (array), cta"""
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            # Fallback content if API call fails
            print(f"Call to OpenAI Failed.. {e}")
            return {
                "headline": f"Transform Your {business_info['industry']} Business",
                "subheadline": "Innovative Solutions for Modern Challenges",
                "value_props": [
                    "Streamlined Operations",
                    "Enhanced Efficiency",
                    "Proven Results"
                ],
                "cta": "Start Your Journey"
            }

class DesignAgent:
    """Agent responsible for design decisions and styling"""
    
    @staticmethod
    def generate_design_specs(business_info: Dict) -> Dict:
        prompt = f"""Generate design specifications for a {business_info['industry']} website with {business_info['color_scheme']} theme.
        Include:
        1. Color palette (5 colors)
        2. Font recommendations
        3. Layout style
        
        Format as JSON with keys: colors (array), fonts (array), layout_style"""
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(response.choices[0].message.content)
        except:
            # Fallback design if API call fails
            return {
                "colors": ["#2C3E50", "#ECF0F1", "#3498DB", "#2980B9", "#E74C3C"],
                "fonts": ["Poppins", "Open Sans"],
                "layout_style": "modern-minimal"
            }

class FeatureAgent:
    """Agent responsible for suggesting relevant features and solutions"""
    
    @staticmethod
    def generate_features(business_info: Dict) -> List[Dict]:
        prompt = f"""Generate 3 key features/solutions for a {business_info['business_type']} in the {business_info['industry']} industry.
        Customer base: {business_info['customer_base']}
        
        For each feature, provide:
        1. Feature name
        2. Brief description
        3. Key benefit
        
        Format as JSON array with objects containing: name, description, benefit"""
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(response.choices[0].message.content)
        except:
            # Fallback features if API call fails
            return [
                {
                    "name": "Advanced Analytics",
                    "description": "Gain deep insights into your operations",
                    "benefit": "Make data-driven decisions"
                },
                {
                    "name": "Automated Workflow",
                    "description": "Streamline your business processes",
                    "benefit": "Save time and reduce errors"
                },
                {
                    "name": "24/7 Support",
                    "description": "Round-the-clock expert assistance",
                    "benefit": "Peace of mind and reliability"
                }
            ]

def generate_landing_page(business_info: Dict) -> str:
    # Initialize agents
    content_agent = ContentAgent()
    design_agent = DesignAgent()
    feature_agent = FeatureAgent()
    
    # Get content from agents
    content = content_agent.generate_content(business_info)
    design = design_agent.generate_design_specs(business_info)
    features = feature_agent.generate_features(business_info)
    
    ## Print responses to see what we are getting from the models
    print(f"content : {content}")
    print(f"design : {design}")
    print(f"features : {features}")

    # Generate HTML using agent-provided content
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{business_info['business_type']} - Welcome</title>
        <link href="https://fonts.googleapis.com/css2?family={design['fonts'][0].replace(' ', '+')}&family={design['fonts'][1].replace(' ', '+')}&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary-color: {design['colors'][0]};
                --secondary-color: {design['colors'][1]};
                --accent-color: {design['colors'][2]};
                --text-color: {design['colors'][3]};
                --highlight-color: {design['colors'][4]};
            }}
            
            body {{
                font-family: '{design['fonts'][1]}', sans-serif;
                margin: 0;
                padding: 0;
                background-color: var(--secondary-color);
                color: var(--text-color);
            }}
            
            h1, h2, h3, h4, h5, h6 {{
                font-family: '{design['fonts'][0]}', sans-serif;
            }}
            
            header {{
                background-color: var(--primary-color);
                color: white;
                padding: 3rem;
                text-align: center;
            }}
            
            .hero {{
                padding: 5rem 2rem;
                text-align: center;
                background-color: var(--secondary-color);
                position: relative;
                overflow: hidden;
            }}
            
            .features {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                padding: 4rem 2rem;
                background-color: white;
            }}
            
            .feature {{
                text-align: left;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }}
            
            .feature:hover {{
                transform: translateY(-5px);
            }}
            
            .cta {{
                background-color: var(--accent-color);
                color: white;
                padding: 1rem 2rem;
                border-radius: 30px;
                text-decoration: none;
                display: inline-block;
                margin-top: 2rem;
                font-weight: bold;
                transition: all 0.3s ease;
            }}
            
            .cta:hover {{
                background-color: var(--highlight-color);
                transform: scale(1.05);
            }}
            
            footer {{
                background-color: var(--primary-color);
                color: white;
                text-align: center;
                padding: 3rem;
                margin-top: 4rem;
            }}
            
            .benefit-tag {{
                display: inline-block;
                background-color: var(--highlight-color);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 20px;
                font-size: 0.9rem;
                margin-top: 1rem;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{content['headline']}</h1>
            <p>{content['subheadline']}</p>
        </header>
        
        <section class="hero">
            <h2>Why Choose Us?</h2>
            <div class="value-props">
                {' '.join(f'<p>{prop}</p>' for prop in content['value_props'])}
            </div>
            <a href="#contact" class="cta">{content['cta']}</a>
        </section>
        
        <section class="features">
    """
    
    # Add features dynamically
    for feature in features:
        html += f"""
            <div class="feature">
                <h3>{feature['name']}</h3>
                <p>{feature['description']}</p>
                <div class="benefit-tag">{feature['benefit']}</div>
            </div>
        """
    
    html += """
        </section>
        
        <footer>
            <p>Ready to transform your business?</p>
            <a href="#contact" class="cta">Contact Us Now</a>
        </footer>
    </body>
    </html>
    """
    
    return html

def main():
    st.title("AI-Powered Marketing Landing Page Generator")
    st.write("Create a customized landing page with AI-generated content")
    
    with st.form("landing_page_form"):
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
            ["Technology", "Healthcare", "Retail", "Finance", "Education", "Manufacturing", "Other"]
        )
        
        color_scheme = st.selectbox(
            "Color Scheme",
            ["Professional", "Vibrant", "Natural", "Elegant", "Modern", "Traditional"]
        )
        
        submit_button = st.form_submit_button("Generate Landing Page")
    
    if submit_button:
        with st.spinner("AI agents are creating your landing page..."):
            time.sleep(3)
            business_info = {
                "business_type": business_type,
                "customer_base": customer_base,
                "geography": geography,
                "industry": industry,
                "color_scheme": color_scheme
            }
            
            html_code = generate_landing_page(business_info)
            
            # Preview
            st.subheader("Preview")
            st.components.v1.html(html_code, height=600)
            
            # Code display
            with st.expander("View Generated HTML Code"):
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
