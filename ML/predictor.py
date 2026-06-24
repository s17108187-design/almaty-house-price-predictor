import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "model" / "2version_on_catboost_cat.pkl"
columns_path = BASE_DIR / "model" / "columns.pkl"

# model and columns (columns for district & proximity на будущее ебень не используй эту хуету при обучеии модели
#                                                                                       чтоб не трахатся как сейчас

model = joblib.load(model_path)
columns = joblib.load(columns_path)


def predict_cena(haip):
    row = dict.fromkeys(columns, 0)

    row["housing_median_age"] = haip["housing_median_age"]
    row["total_rooms"] = haip["total_rooms"]
    row["total_bedrooms"] = haip["total_bedrooms"]
    row["total_floors"] = haip["total_floors"]
    row["ceiling_height"] = haip["ceiling_height"]
    row["total_area"] = haip["total_area"]
    row["metro_distance_km"] = haip["metro_distance_km"]

    district_col = f"district_{haip['district']}"
    building_col = f"building_type_{haip['building_type']}"
    proximity_col = f"proximity_{haip['proximity']}"

    if district_col in row:
        row[district_col] = 1

    if building_col in row:
        row[building_col] = 1

    if proximity_col in row:
        row[proximity_col] = 1

    df = pd.DataFrame([row])


    prediction = model.predict(df)

    return float(prediction[0])

