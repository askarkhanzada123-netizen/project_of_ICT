import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Engineering Tool", layout="centered")

# --- Student Identification ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.sidebar.markdown("### Developer Info")
st.sidebar.write("**Name:** Askar khan")
st.sidebar.write("**Roll Number:** 25-ME-231")

st.info(f"Developed by: **Askar khan** | Roll No: **25-ME-231**")
st.divider()

# --- App Logic ---
tab1, tab2 = st.tabs(["Unit Converter", "Material Density Checker"])

with tab1:
    st.header("⚙️ Unit Converter")
    category = st.selectbox("Select Dimension", ["Pressure", "Force", "Length"])
    
    col1, col2 = st.columns(2)
    
    if category == "Pressure":
        with col1:
            val = st.number_input("Enter Value", value=1.0, key="pres")
            unit = st.selectbox("From Unit", ["Pascal (Pa)", "Bar", "PSI"])
        
        # Convert all to Pa first
        pa = val
        if unit == "Bar": pa = val * 100000
        if unit == "PSI": pa = val * 6894.76
        
        with col2:
            st.write("**Converted Values:**")
            st.write(f"{pa:,.2f} Pa")
            st.write(f"{pa/100000:.4f} Bar")
            st.write(f"{pa/6894.76:.4f} PSI")

    elif category == "Force":
        with col1:
            val = st.number_input("Enter Value", value=1.0, key="force")
            unit = st.selectbox("From Unit", ["Newton (N)", "KiloNewton (kN)", "Pound-force (lbf)"])
        
        n = val
        if unit == "KiloNewton (kN)": n = val * 1000
        if unit == "Pound-force (lbf)": n = val * 4.44822
        
        with col2:
            st.write("**Converted Values:**")
            st.write(f"{n:,.2f} N")
            st.write(f"{n/1000:.4f} kN")
            st.write(f"{n/4.44822:.4f} lbf")

    elif category == "Length":
        with col1:
            val = st.number_input("Enter Value", value=1.0, key="len")
            unit = st.selectbox("From Unit", ["Millimeters (mm)", "Meters (m)", "Inches (in)"])
        
        mm = val
        if unit == "Meters (m)": mm = val * 1000
        if unit == "Inches (in)": mm = val * 25.4
        
        with col2:
            st.write("**Converted Values:**")
            st.write(f"{mm:,.2f} mm")
            st.write(f"{mm/1000:.4f} m")
            st.write(f"{mm/25.4:.4f} in")

with tab2:
    st.header("🧪 Material Density Checker")
    
    # Dictionary of standard engineering materials (kg/m^3)
    densities = {
        "Steel (Mild)": 7850,
        "Aluminum (6061)": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Stainless Steel": 8000
    }
    
    mat = st.selectbox("Select Material", list(densities.keys()))
    rho = densities[mat]
    
    st.metric(label=f"Density of {mat}", value=f"{rho} kg/m³")
    
    st.write("---")
    st.subheader("Mass Estimator")
    vol = st.number_input("Enter Volume of Component (m³)", value=0.01, format="%.4f")
    mass = rho * vol
    st.success(f"Estimated Mass: **{mass:.3f} kg**")
