<<<<<<< HEAD
# SolarSupplyPrediction
This project predict the growth percentage of Solar Power by 2030 using the historical data from two different plants. We have used the ML models to train those data and evaluated using MSE. To make this usable, we built the end-to-end platform using Flask + Python as Backend and HTML, CSS, JavaScript as Frontend
=======
# Solar Supply Prediction

## Project Overview
This project is a solar power forecasting and analytics dashboard that predicts future solar energy output using historical generation data from two solar plants. It combines a Flask backend, machine learning models, and a frontend dashboard to present insights and future projections for solar generation.

The application reads CSV datasets containing solar plant operational data, trains predictive models using Random Forest Regressors, and exposes the results through REST API endpoints. The frontend fetches these results to display prediction values, annual trends, and plant comparison charts.

## Problem Statement
Solar energy generation depends on multiple variables such as temperature, irradiation, power output, and time-based production patterns. Without a proper forecasting mechanism, it becomes difficult to estimate how much electricity a plant may generate in the future and to compare plant performance over time.

This project addresses that gap by:
- analyzing historical solar generation data,
- training predictive models for DC power, AC power, daily yield, and total yield,
- exposing prediction results through API endpoints,
- and visualizing the findings in a web dashboard.

## Key Modules
### 1. Backend
The backend is implemented in Python using Flask.

Main responsibilities:
- load CSV datasets,
- clean and prepare data,
- train machine learning models,
- serve prediction and trend data through API routes,
- enable frontend access via CORS.

### 2. Machine Learning
The model uses scikit-learn RandomForestRegressor to predict future solar output values.

Predicted outputs include:
- DC Power
- AC Power
- Daily Yield
- Total Yield

### 3. Frontend Dashboard
The frontend is built using HTML, CSS, and JavaScript.

Main responsibilities:
- display overview information,
- render prediction values,
- show charts for different power and yield metrics,
- compare plant performance,
- display long-term trend tables.

## Architecture
The system follows a simple three-layer architecture:

1. Data Layer
   - CSV files containing solar generation data

2. Application Layer
   - Flask backend loads data and runs prediction logic
   - Machine learning models are trained and evaluated here

3. Presentation Layer
   - Browser-based frontend fetches JSON data from the backend
   - Chart.js renders visualizations

The interaction flow is:
- CSV data is loaded by the backend
- machine learning models are trained
- API endpoints return processed results in JSON format
- frontend JavaScript fetches those endpoints and displays charts and numbers

## Project Structure
```text
SOLAR POWER/
├── BACKEND/
│   ├── main.py
│   ├── Plant_1_Generation_Data.csv
│   └── Plant_2_Generation_Data.csv
├── FRONTEND/
│   ├── about.html
│   ├── frontpage.html
│   ├── index.html
│   ├── logo.jpg
│   ├── script.js
│   └── style.css
├── .venv/
├── README.md
├── TODO.md
└── .gitignore
```

## Setup Virtual Environment
It is recommended to create and activate a virtual environment before running the project.

### Create a virtual environment
```bash
cd "C:\Users\vishe\OneDrive\Documents\Project\SOLAR POWER"
python -m venv .venv
```

### Activate the virtual environment
On Windows PowerShell:
```powershell
. .\.venv\Scripts\Activate.ps1
```

### Install dependencies
```bash
python -m pip install --upgrade pip
python -m pip install flask flask-cors pandas scikit-learn numpy matplotlib
```

## Database (CSV files)
The project uses two CSV files stored in the BACKEND folder:

- Plant_1_Generation_Data.csv
- Plant_2_Generation_Data.csv

These files contain historical solar generation records and values such as:
- DC power
- AC power
- daily yield
- total yield
- date and time information
- plant metadata

The backend reads these datasets, cleans the column names, combines the records, and then gets the necessary features for forecasting.

## Running the Project
### 1. Start the backend
```bash
cd "C:\Users\vishe\OneDrive\Documents\Project\SOLAR POWER"
python BACKEND/main.py
```

This starts the Flask backend on:
```text
http://localhost:5000
```

### 2. Open the frontend
You can open the frontend directly in a browser:

```text
file:///C:/Users/vishe/OneDrive/Documents/Project/SOLAR POWER/FRONTEND/frontpage.html
```

or in VS Code using the Live Preview extension or by opening the HTML file directly.

### 3. Frontend-to-backend API
The frontend JavaScript calls endpoints like:
- /prediction
- /trends
- /yearly/dc
- /yearly/ac
- /comparison

These requests must reach the local backend at port 5000.

## Testing
The project currently contains minimal formal automated tests. Most validation is done by:
- running the Flask backend,
- checking startup output,
- verifying API routes return JSON,
- and confirming the browser loads the dashboard without frontend script errors.

Recommended manual checks:
1. Start the backend successfully.
2. Visit the API endpoints in a browser or using curl.
3. Confirm frontend loads and charts render.
4. Check browser console for errors.

Example API check:
```bash
curl http://localhost:5000/prediction
```

This should return JSON prediction data if the backend is running correctly.

## Limitation
This project has several limitations:

- The datasets are static CSV files, so the model is limited to historical data present in those files.
- The current model uses synthetic or derived environmental placeholders such as module temperature, ambient temperature, and irradiation values.
- The dataset does not contain a very large or highly diverse time series, which may affect prediction quality.
- There are no formal unit tests or continuous integration checks in place.
- The prediction logic is not connected to a production-grade database or deployment pipeline.
- The frontend is a static dashboard and will only work correctly if the Flask backend is running.

## Conclusion
This project serves as a practical demonstration of machine learning-based solar power forecasting integrated with a web dashboard. It highlights how historical solar production data can be processed, modeled, and displayed to help stakeholders understand past performance and estimate future energy output.

## License
This project is intended for educational and demonstration purposes unless stated otherwise by the repository owner.
>>>>>>> a8bc13e (Initial commit: Solar Supply Prediction)
