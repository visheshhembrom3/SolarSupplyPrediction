// Fetch data from backend API
async function fetchData(url) {
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

// Hide all sections
function hideAllSections() {
    document.querySelectorAll('main section')
        .forEach(section => section.classList.remove('active'));
}

// Show selected section
function showSection(id) {
    hideAllSections();
    document.getElementById(id).classList.add('active');
}

// Load prediction data
fetchData('http://localhost:5000/prediction').then(data => {
    if (data) {
        document.getElementById('predicted-dc').textContent =
            data.predicted_dc.toFixed(2);
        document.getElementById('predicted-ac').textContent =
            data.predicted_ac.toFixed(2);
        document.getElementById('predicted-daily').textContent =
            data.predicted_daily.toFixed(2);
        document.getElementById('predicted-total').textContent =
            data.predicted_total.toFixed(2);
        document.getElementById('growth-2030').textContent =
            data.growth_2030.toFixed(2);
    }
});

// Load trends table
fetchData('http://localhost:5000/trends').then(data => {
    if (data) {
        const tbody = document.querySelector('#trendTable tbody');
        data.data.forEach(row => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${row.year}</td>
                <td>${row.growth}</td>
                <td>${row.ac_growth}</td>
                <td>${row.trend}</td>
            `;
            tbody.appendChild(tr);
        });
    }
});

// CHART INSTANCE STORAGE (avoid duplicate charts)
let charts = {};

function destroyChart(name) {
    if (charts[name]) {
        charts[name].destroy();
        charts[name] = null;
    }
}

// Button listeners
document.getElementById('btn-overview').addEventListener('click', () => {
    showSection('overview');
});

document.getElementById('btn-prediction').addEventListener('click', () => {
    showSection('prediction');
});

document.getElementById('btn-dc-chart').addEventListener('click', async () => {
    showSection('dc-chart');
    destroyChart("dc");

    const data = await fetchData('http://localhost:5000/yearly/dc');
    if (data) {
        charts.dc = new Chart(document.getElementById('dcPowerChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Average DC Power',
                    data: data.values,
                    borderColor: 'rgb(0, 115, 230)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-ac-chart').addEventListener('click', async () => {
    showSection('ac-chart');
    destroyChart("ac");

    const data = await fetchData('http://localhost:5000/yearly/ac');
    if (data) {
        charts.ac = new Chart(document.getElementById('acPowerChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Average AC Power',
                    data: data.values,
                    borderColor: 'rgb(255, 60, 60)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-daily-chart').addEventListener('click', async () => {
    showSection('daily-chart');
    destroyChart("daily");

    const data = await fetchData('http://localhost:5000/yearly/daily');
    if (data) {
        charts.daily = new Chart(document.getElementById('dailyYieldChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Average Daily Yield',
                    data: data.values,
                    borderColor: 'rgb(80, 140, 255)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-total-chart').addEventListener('click', async () => {
    showSection('total-chart');
    destroyChart("total");

    const data = await fetchData('http://localhost:5000/yearly/total');
    if (data) {
        charts.total = new Chart(document.getElementById('totalYieldChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Average Total Yield',
                    data: data.values,
                    borderColor: 'rgb(255, 180, 0)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-comparison').addEventListener('click', async () => {
    showSection('comparison');
    destroyChart("compare");

    const data = await fetchData('http://localhost:5000/comparison');
    if (data) {
        charts.compare = new Chart(document.getElementById('comparisonChart'), {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [
                    {
                        label: 'Plant 1',
                        data: data.plant1,
                        backgroundColor: 'rgba(0, 120, 255, 0.7)'
                    },
                    {
                        label: 'Plant 2',
                        data: data.plant2,
                        backgroundColor: 'rgba(255, 80, 80, 0.7)'
                    }
                ]
            }
        });
    }
});

document.getElementById('btn-trends').addEventListener('click', () => {
    showSection('trends');
});

document.getElementById('btn-future-dc-chart').addEventListener('click', async () => {
    showSection('future-dc-chart');
    destroyChart("futureDc");

    const data = await fetchData('http://localhost:5000/future/dc');
    if (data) {
        charts.futureDc = new Chart(document.getElementById('futureDcChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Projected Future DC Power',
                    data: data.values,
                    borderColor: 'rgb(0, 200, 100)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-future-ac-chart').addEventListener('click', async () => {
    showSection('future-ac-chart');
    destroyChart("futureAc");

    const data = await fetchData('http://localhost:5000/future/ac');
    if (data) {
        charts.futureAc = new Chart(document.getElementById('futureAcChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Projected Future AC Power',
                    data: data.values,
                    borderColor: 'rgb(255, 100, 100)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-future-daily-chart').addEventListener('click', async () => {
    showSection('future-daily-chart');
    destroyChart("futureDaily");

    const data = await fetchData('http://localhost:5000/future/daily');
    if (data) {
        charts.futureDaily = new Chart(document.getElementById('futureDailyChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Projected Future Daily Yield',
                    data: data.values,
                    borderColor: 'rgb(100, 100, 255)',
                    fill: false
                }]
            }
        });
    }
});

document.getElementById('btn-future-total-chart').addEventListener('click', async () => {
    showSection('future-total-chart');
    destroyChart("futureTotal");

    const data = await fetchData('http://localhost:5000/future/total');
    if (data) {
        charts.futureTotal = new Chart(document.getElementById('futureTotalChart'), {
            type: 'line',
            data: {
                labels: data.years,
                datasets: [{
                    label: 'Projected Future Total Yield',
                    data: data.values,
                    borderColor: 'rgb(255, 200, 0)',
                    fill: false
                }]
            }
        });
    }
});

// Dark mode toggle functionality
const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.body;

// Load saved theme preference
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    body.classList.add('dark-mode');
    darkModeToggle.textContent = '☀️';
}

// Toggle dark mode
darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    const isDarkMode = body.classList.contains('dark-mode');
    darkModeToggle.textContent = isDarkMode ? '☀️' : '🌙';
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
});

// show overview first
showSection('overview');
