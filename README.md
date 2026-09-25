# Solar Supply Prediction

A Flask and JavaScript dashboard for exploring historical solar generation data from two plants. The backend trains Random Forest models for power and yield values, exposes results through a Flask API, and displays charts and trends in the browser.

## Features

- Predicts DC power, AC power, daily yield, and total yield.
- Shows yearly averages and comparisons between the two plants.
- Displays illustrative projections and growth trends through 2030.
- Provides a browser dashboard with light and dark themes.

## Project Architecture

The application loads the historical plant data, prepares model features, serves predictions and summaries through Flask, and presents the results in a browser dashboard.

```text
┌──────────────────────────────────────────────┐
│ Plant generation data                        │
│ Plant_1_Generation_Data.csv + Plant_2_...csv │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│ Data loading and preparation                 │
│ BACKEND/main.py · pandas · NumPy              │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│ Random Forest prediction models              │
│ DC power · AC power · daily yield · total    │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│ Flask API                                     │
│ BACKEND/main.py · JSON endpoints              │
└──────────────────────┬───────────────────────┘
                       ↕ HTTP / JSON
┌──────────────────────────────────────────────┐
│ Browser dashboard                             │
│ FRONTEND HTML · script.js · Chart.js          │
└──────────────────────────────────────────────┘
```

## Project Structure

```text
SolarSupplyPrediction/
├── BACKEND/
│   ├── main.py                       # Flask API, data processing, and prediction models
│   ├── Plant_1_Generation_Data.csv   # Historical generation data for plant 1
│   └── Plant_2_Generation_Data.csv   # Historical generation data for plant 2
├── FRONTEND/
│   ├── frontpage.html                # Landing page
│   ├── index.html                    # Main dashboard
│   ├── about.html                    # Project information page
│   ├── script.js                     # API calls, dashboard behavior, and charts
│   ├── style.css                     # Page layout, styling, and themes
│   └── logo.jpg                      # Project logo
├── SOLAR POWER/                      # Earlier uploaded copy of the project files
│   ├── BACKEND/                      # Duplicate backend files and data
│   ├── FRONTEND/                     # Duplicate frontend files and assets
│   └── TODO.md                       # Earlier project notes
├── README.md                         # Project overview and setup instructions
└── TODO.md                           # Project tasks and notes
```

The top-level `BACKEND/` and `FRONTEND/` folders are the current project layout. `SOLAR POWER/` is an earlier uploaded copy retained in the repository.

## Requirements

Python 3.10 or newer. Install the backend packages from the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Flask Flask-Cors matplotlib numpy pandas scikit-learn
```

## Run Locally

Start the backend from the repository root:

```powershell
python BACKEND/main.py
```

The API runs at `http://localhost:5000`. Open `FRONTEND/frontpage.html` in a browser to begin, then use the dashboard to view predictions and charts.

## API Routes

The Flask backend provides routes for predictions, yearly summaries, plant comparisons, and growth projections. See `BACKEND/main.py` for the current route names and request formats.

## Notes

Some projection values are illustrative estimates based on the available historical data and model assumptions. They should not be treated as guaranteed future generation.
