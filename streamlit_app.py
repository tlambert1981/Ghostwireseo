import streamlit as st
import requests
import json
import base64

# --- GHOSTWIRE UI CONFIG ---
st.set_page_config(page_title="Ghostwire AEO", layout="centered", page_icon="⚡")

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
        <div style="font-size:32px; letter-spacing:.08em; color:#31f3ff; font-weight:700;">GHOSTWIRE AEO</div>
        <p style="font-size:14px; color:#8aa7ad; max-width: 30ch; margin: 0 auto;">Precision AI Search Visibility Intelligence for DFW Business Leaders.</p>
    </div>
    """, unsafe_allow_html=True)

# --- DATA ENGINE ---
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

# --- APP INTERFACE ---
st.markdown('<div style="background:rgba(10,14,18,.78); border:1px solid rgba(0,255,255,0.28); padding:25px; border-radius:20px; backdrop-filter:blur(10px);">', unsafe_allow_html=True)

target = st.text_input("TARGET DOMAIN", placeholder="example.com")
email = st.text_input("EMAIL ADDRESS", placeholder="you@example.com")

if target:
    res = get_aeo_data(target)
    if res:
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<p style='color:#8aa7ad; font-size:12px;'>AI CITATION PROBABILITY</p>", unsafe_allow_html=True)
            st.title(f"{int(res['citations'])}%")
        with col2:
            st.markdown("<p style='color:#8aa7ad; font-size:12px;'>ANNUAL REVENUE GAP</p>", unsafe_allow_html=True)
            st.title(f"${res['val']*12:,.0f}")
        
        st.markdown("---")
        st.subheader("🔓 Unlock Full AEO Intelligence Audit")
        st.write(f"To download the full 5-page PDF technical audit for **{target}**, please send payment.")
        
        # YOUR CASH APP PAYMENT BOX
        st.info("💎 **Price: $50.00**")
        st.link_button("Pay $50.00 via Cash App", "https://cash.app/$GhostwireAEO/50")
        st.caption("Please include your domain name in the Cash App note.")
        
        st.write("---")
        # THE MANUAL UNLOCK GATE
        unlock_code = st.text_input("ENTER UNLOCK CODE", type="password", placeholder="Enter the code sent to your email")
        
        # You can change 'GW2025' to any code you want
        if unlock_code == "GW2025":
            st.success("✅ Intelligence Report Unlocked.")
            st.button("📥 Download PDF Audit")
        elif unlock_code:
            st.error("Invalid Code. Access Denied.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-size:11px; margin-top:20px; color:#6f8c92; letter-spacing: .12em;">DEVELOPED BY TRAVIS LAMBERT | GHOSTWIRE AEO</div>', unsafe_allow_html=True)