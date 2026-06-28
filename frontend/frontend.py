import streamlit as st
import requests



st.set_page_config(
    page_title="Almaty House Price Predictor",
    page_icon="🏠",
    layout="wide"
)



st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
}

div[data-testid="stMetric"]{
    border:1px solid #444;
    border-radius:15px;
    padding:20px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
# 🏠 Almaty House Price Predictor

Estimate apartment prices using a Machine Learning model trained on apartment data from Almaty.

---
""")

st.subheader("📋 Apartment Parameters")



col1, col2 = st.columns(2)

with col1:

    housing_median_age = st.number_input(
        "🏗 House age (years)",
        min_value=1,
        max_value=52,
        value=10
    )

    total_rooms = st.number_input(
        "🚪 Total rooms",
        min_value=1,
        value=3
    )

    total_bedrooms = st.number_input(
        "🛏 Bedrooms",
        min_value=1,
        value=2
    )

    total_area = st.number_input(
        "📐 Total area (m²)",
        min_value=10.0,
        value=60.0
    )

    ceiling_height = st.number_input(
        "📏 Ceiling height (m)",
        min_value=2.0,
        value=2.7
    )

with col2:

    total_floors = st.number_input(
        "🏢 Total floors",
        min_value=1,
        value=9
    )

    metro_distance_km = st.number_input(
        "🚇 Distance to metro (km)",
        min_value=0.0,
        value=1.5
    )

    building_type = st.selectbox(
        "🏠 Building type",
        [
            "панельный",
            "кирпичный",
            "монолитный",
            "каркасно-монолитный"
        ]
    )

    proximity = st.selectbox(
        "📍 Location",
        [
            "ЦЕНТР",
            "БЛИЗ ЦЕНТРА",
            "СПАЛЬНЫЙ",
            "ОКРАИНА",
            "ГОРЫ"
        ]
    )

    district = st.selectbox(
        "🗺 District",
        [
            "Алатауский",
            "Алмалинский",
            "Ауэзовский",
            "Бостандыкский",
            "Жетысуский",
            "Медеуский",
            "Наурызбайский",
            "Турксибский"
        ]
    )

st.divider()



predict = st.button("💰 Predict Apartment Price")

# ---------------- REQUEST ---------------- #

if predict:

    payload = {
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "total_floors": total_floors,
        "ceiling_height": ceiling_height,
        "total_area": total_area,
        "metro_distance_km": metro_distance_km,
        "building_type": building_type,
        "proximity": proximity,
        "district": district
    }

    with st.spinner("🤖 Predicting apartment price..."):

        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload
            )

            result = response.json()

            price = result["prediction"]

            st.success("Prediction completed successfully!")

            st.metric(
                label="💰 Estimated Apartment Price",
                value=f"{price:,.0f} ₸"
            )

        except Exception as e:
            st.error(f"❌ Error while connecting to backend:\n\n{e}")

st.divider()

st.info("""
### ℹ About the Model

- **Model:** CatBoost Regressor
- **Dataset:** Apartments in Almaty
- **Purpose:** Estimate apartment prices based on key property characteristics.

> This prediction is intended for informational purposes only and may differ from actual market prices.
""")
