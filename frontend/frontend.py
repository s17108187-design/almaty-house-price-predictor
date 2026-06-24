import streamlit as st
import requests

st.title("Almaty price house detector "
         "Хуета редкостаная которую надо допиливать и допиливать"
            "а ещё я ебал маму делать фронт")



housing_median_age = st.number_input("suka1")
total_rooms = st.number_input("su2ka")
total_bedrooms = st.number_input("suk3a")
total_floors = st.number_input("s4uka")
ceiling_height = st.number_input("su5ka")
total_area = st.number_input("su6ka")
metro_distance_km = st.number_input("s7uka")
building_type = st.selectbox("Тип дома" , ["панельный","кирпичный","монолитный","каркасно-монолитный"])
proximity = st.selectbox("Локация",["ЦЕНТР","БЛИЗ", "ЦЕНТРА", "СПАЛЬНЫЙ","ОКРАИНА" ,"ГОРЫ"])
district = st.selectbox("Район",["Алатауский", "Алмалинский",
                                        "Ауэзовский", "Бостандыкский",
                                        "Жетысуский", "Медеуский", "Наурызбайский",
                                        "Турксибский"])



if st.button("Predict!!!"):
    suka= {
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
    response = requests.post("http://127.0.0.1:8000/predict",json=suka)
    print(response.status_code)
    print(response.text)
    result = response.json()
    st.success(result)

