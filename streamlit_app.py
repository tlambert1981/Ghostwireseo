import streamlit as st
import requests
import json
import base64

# --- GHOSTWIRE UI ---
st.set_page_config(page_title="Ghostwire AEO", layout="centered")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top, rgba(49,243,255,.10), transparent 35%), #050608 !important;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #24dfe9, #34ffff) !important;
        color: #001015 !important;
        font-weight: 800 !important;
        border-radius: 14px !important;
        box-shadow: 0 0 24px rgba(49,243,255,.22) !important;
        width: 100% !important;
        border: none !important;
    }
    input { background-color: rgba(0,0,0,0.35) !important; color: #e9f7f8 !important; border-radius: 14px !important; }
    label p { font-size: 12px !important; text-transform: uppercase !important; color: #b8d7db !important; letter-spacing: .08em; }
    </style>
    <div style="text-align: center; margin-bottom: 30px;">
        <div style="font-size:28px; letter-spacing:.08em; color:#31f3ff; font-weight:700;">GHOSTWIRE AEO</div>
        <p style="font-size:13px; color:#8aa7ad; max-width: 26ch; margin: 0 auto;">Precision AI Search Visibility Intelligence.</p>
    </div>
    """, unsafe_allow_html=True)

def get_aeo_data(domain):
    try:
        login = st.secrets["DFO_LOGIN"]
        password = st.secrets["DFO_PASS"]
        auth = base64.b64encode(f"{login}:{password}".encode()).decode()
        url = "https://api.dataforseo.com/v3/dataforseo_labs/google/domain_rank_overview/live"
        payload = json.dumps([{"target": domain, "location_code": 2840, "language_code": "en"}])
        headers = {'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        metrics = response.json()['tasks'][0]['result'][0]['metrics']['organic']
        return {"val": metrics['cost'], "citations": metrics['pos_1_3']}
    except:
        return None

st.markdown('<div style="background:rgba(10,14,18,.78); border:1px solid rgba(0,255,255,0.28); padding:25px; border-radius:20px;">', unsafe_allow_html=True)
target = st.text_input("TARGET DOMAIN", placeholder="example.com")
email = st.text_input("EMAIL ADDRESS", placeholder="you@example.com")

if st.button("RUN AUDIT — $50"):
    if target:
        with st.spinner("Decrypting AI Rankings..."):
            res = get_aeo_data(target)
            if res:
                st.markdown("---")
                col1, col2 = st.columns(2)
                col1.metric("AI CITATION %", f"{int(res['citations'])}%")
                col2.metric("REVENUE GAP (EST)", f"${res['val']*12:,.0f}")
                st.link_button("Unlock Full Intelligence Report", "https://buy.stripe.com/your_link")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-size:11px; margin-top:20px; color:#6f8c92;">DEVELOPED BY TRAVIS LAMBERT</div>', unsafe_allow_html=True)