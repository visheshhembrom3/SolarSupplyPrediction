import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# -----------------------------------------
# 1. LOAD DATASETS
# -----------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
df1 = pd.read_csv(os.path.join(script_dir, "Plant_1_Generation_Data.csv"))
df2 = pd.read_csv(os.path.join(script_dir, "Plant_2_Generation_Data.csv"))

# -----------------------------------------
# 2. CLEAN COLUMN NAMES
# -----------------------------------------
df1.columns = df1.columns.str.lower().str.replace(" ", "_")
df2.columns = df2.columns.str.lower().str.replace(" ", "_")

# -----------------------------------------
# 3. MERGE BOTH DATASETS
# -----------------------------------------
data = pd.concat([df1, df2], ignore_index=True)

# -----------------------------------------
# 4. CREATE ENVIRONMENTAL PLACEHOLDERS
# -----------------------------------------
data['module_temperature'] = data['dc_power'] * 0.05 + 20
data['ambient_temperature'] = data['dc_power'] * 0.03 + 15
data['irradiation'] = data['dc_power'] * 0.001 + 1

# -----------------------------------------
# 5. FEATURES AND TARGET
# -----------------------------------------
features = ["plant_id", "ambient_temperature", "module_temperature", "irradiation"]
X = data[features]
y_dc = data["dc_power"]
y_ac = data["ac_power"]
y_daily = data["daily_yield"]
y_total = data["total_yield"]

# -----------------------------------------
# 6. TRAIN / TEST SPLIT
# -----------------------------------------
X_train, X_test, y_train_dc, y_test_dc = train_test_split(
    X, y_dc, test_size=0.2, random_state=42
)
X_train_ac, X_test_ac, y_train_ac, y_test_ac = train_test_split(
    X, y_ac, test_size=0.2, random_state=42
)
X_train_daily, X_test_daily, y_train_daily, y_test_daily = train_test_split(
    X, y_daily, test_size=0.2, random_state=42
)
X_train_total, X_test_total, y_train_total, y_test_total = train_test_split(
    X, y_total, test_size=0.2, random_state=42
)

# -----------------------------------------
# 7. RANDOM FOREST MODELS
# -----------------------------------------
model_dc = RandomForestRegressor()
model_dc.fit(X_train, y_train_dc)

pred_dc = model_dc.predict(X_test)
mse_dc = mean_squared_error(y_test_dc, pred_dc)
print("Random Forest MSE for DC:", mse_dc)

model_ac = RandomForestRegressor()
model_ac.fit(X_train_ac, y_train_ac)

pred_ac = model_ac.predict(X_test_ac)
mse_ac = mean_squared_error(y_test_ac, pred_ac)
print("Random Forest MSE for AC:", mse_ac)

model_daily = RandomForestRegressor()
model_daily.fit(X_train_daily, y_train_daily)

pred_daily = model_daily.predict(X_test_daily)
mse_daily = mean_squared_error(y_test_daily, pred_daily)
print("Random Forest MSE for Daily Yield:", mse_daily)

model_total = RandomForestRegressor()
model_total.fit(X_train_total, y_train_total)

pred_total = model_total.predict(X_test_total)
mse_total = mean_squared_error(y_test_total, pred_total)
print("Random Forest MSE for Total Yield:", mse_total)

# -----------------------------------------
# 9. FUTURE PREDICTION INPUT
# -----------------------------------------
future_data = pd.DataFrame(
    [[4135001, 28, 60, 5.2]],
    columns=features
)

future_dc = model_dc.predict(future_data)[0]
future_ac = model_ac.predict(future_data)[0]
future_daily = model_daily.predict(future_data)[0]
future_total = model_total.predict(future_data)[0]
print("\nPredicted Future DC Power:", future_dc)
print("Predicted Future AC Power:", future_ac)
print("Predicted Future Daily Yield:", future_daily)
print("Predicted Future Total Yield:", future_total)

# -----------------------------------------
# 9. YEAR-WISE AVERAGE CALCULATION + PLOT
# -----------------------------------------
def compute_yearly_average(df, date_column, value_column):
    df[date_column] = pd.to_datetime(df[date_column], format='mixed')
    df["Year"] = df[date_column].dt.year
    return df.groupby("Year")[value_column].mean()

def plot_yearly_average(df, date_column, value_column, plant_name):
    yearly_avg = compute_yearly_average(df, date_column, value_column)

    plt.figure(figsize=(10, 5))
    plt.plot(yearly_avg.index, yearly_avg.values, marker="o", linewidth=2)
    plt.title(f"{plant_name} — Yearly Average {value_column}")
    plt.xlabel("Year")
    plt.ylabel(f"Average {value_column}")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

# -----------------------------------------
# 10. YEARLY AVERAGES COMPUTED (available via API)
# -----------------------------------------
# Plots removed to avoid blocking; data served via Flask routes

# -----------------------------------------
# 11. PLANT AVERAGES COMPUTED (available via API)
# -----------------------------------------
# Bar graph removed; data served via Flask routes

# -----------------------------------------
# 12. LONG-TERM TREND (2025–2030)
# -----------------------------------------
years = np.array([2025, 2026, 2027, 2028, 2029, 2030])
growth = np.array([4.2, 5.1, 5.4, 4.8, 3.2, 2.5])
ac_growth = np.array([3.8, 4.7, 5.0, 4.4, 2.8, 2.1])  # Placeholder AC growth values

trend = pd.DataFrame({
    "Year": years,
    "Estimated Mean DC Power Growth (%)": growth,
    "Estimated Mean AC Power Growth (%)": ac_growth,
    "Trend": [
        "Rising",
        "Rising Faster",
        "Peak",
        "Slight Slowdown",
        "Plateau Forming",
        "Stable & Mature"
    ]
})

print("\n===== SOLAR OUTPUT TREND UNTIL 2030 =====")
print(trend)

# -----------------------------------------
# 13. CURRENT AVERAGES AND FUTURE PROJECTIONS
# -----------------------------------------
current_avg_dc = data["dc_power"].mean()
current_avg_ac = data["ac_power"].mean()
current_avg_daily = data["daily_yield"].mean()
current_avg_total = data["total_yield"].mean()

future_dc_projection = [future_dc * (1 + g/100) for g in growth]
future_ac_projection = [future_ac * (1 + g/100) for g in growth]
future_daily_projection = [future_daily * (1 + g/100) for g in growth]
future_total_projection = [future_total * (1 + g/100) for g in growth]

# -----------------------------------------
# FLASK APP
# -----------------------------------------
app = Flask(__name__)
CORS(app)

@app.route('/prediction')
def get_prediction():
    growth_2030 = growth[5]  # 2030 is index 5 in years array
    return jsonify({
        'predicted_dc': future_dc,
        'predicted_ac': future_ac,
        'predicted_daily': future_daily,
        'predicted_total': future_total,
        'growth_2030': growth_2030
    })

@app.route('/yearly/dc')
def get_yearly_dc():
    yearly_avg = compute_yearly_average(data.copy(), "date_time", "dc_power")
    return jsonify({'years': yearly_avg.index.tolist(), 'values': yearly_avg.values.tolist()})

@app.route('/yearly/ac')
def get_yearly_ac():
    yearly_avg = compute_yearly_average(data.copy(), "date_time", "ac_power")
    return jsonify({'years': yearly_avg.index.tolist(), 'values': yearly_avg.values.tolist()})

@app.route('/yearly/daily')
def get_yearly_daily():
    yearly_avg = compute_yearly_average(data.copy(), "date_time", "daily_yield")
    return jsonify({'years': yearly_avg.index.tolist(), 'values': yearly_avg.values.tolist()})

@app.route('/yearly/total')
def get_yearly_total():
    yearly_avg = compute_yearly_average(data.copy(), "date_time", "total_yield")
    return jsonify({'years': yearly_avg.index.tolist(), 'values': yearly_avg.values.tolist()})

@app.route('/comparison')
def get_comparison():
    cols = ["dc_power", "ac_power", "daily_yield", "total_yield"]
    avg1 = df1[cols].mean()
    avg2 = df2[cols].mean()
    return jsonify({
        'labels': cols,
        'plant1': avg1.tolist(),
        'plant2': avg2.tolist()
    })

@app.route('/future/dc')
def get_future_dc():
    return jsonify({'years': years.tolist(), 'values': future_dc_projection})

@app.route('/future/ac')
def get_future_ac():
    return jsonify({'years': years.tolist(), 'values': future_ac_projection})

@app.route('/future/daily')
def get_future_daily():
    return jsonify({'years': years.tolist(), 'values': future_daily_projection})

@app.route('/future/total')
def get_future_total():
    return jsonify({'years': years.tolist(), 'values': future_total_projection})

@app.route('/trends')
def get_trends():
    return jsonify({
        'data': [
            {'year': int(y), 'growth': float(g), 'ac_growth': float(ac), 'trend': t}
            for y, g, ac, t in zip(years, growth, ac_growth, trend['Trend'])
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)

