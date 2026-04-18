# Smart-Plantation
The Smart Plantation Platform integrates IoT, Blockchain, and Machine Learning to optimize farming. Using ESP32 sensors, it monitors soil moisture, temperature, and rain in real-time. The system features automated irrigation, crop yield prediction, pest detection, and CSV data export. Developed with React, Node.js, and Python for smart agriculture.


# 🌱 Smart Plantation Platform

A state-of-the-art, IoT-driven agriculture platform integrated with **Machine Learning** for precision farming and **Blockchain-like data integrity** for secure sensor logging. This platform offers real-time monitoring, automated irrigation, and intelligent crop insights.

---

## 🚀 Key Features

### 📡 Real-time IoT Monitoring
Monitors critical environmental parameters every 5 seconds:
- **Temperature & Humidity** (DHT22)
- **Soil Moisture**
- **Light Intensity** (LDR)
- **Water Level** (Float Switch)
- **Rain Intensity**

### 🔐 Blockchain Data Integrity
- Implements a cryptographic hashing mechanism (SHA256).
- Every data block contains the hash of the previous block, creating an immutable ledger of sensor readings.
- Prevents data tampering and ensures reliable research records.

### 💧 Precision Irrigation Control
- **Manual Mode**: Toggle the water pump directly from the dashboard.
- **Auto Mode**: Self-regulating system that triggers the pump based on soil moisture thresholds.
- **Scheduling**: Set specific start times and durations for irrigation.

### 🧠 AI/ML Intelligent Insights
- **Ideal Yield Prediction**: Predicts potential crop yield based on climate and soil data.
- **Fertilizer Recommendation**: Suggests the optimal fertilizer type to close the gap between actual and ideal yields.
- **Pest Detection**: 
    - **Data-based**: Risk assessment using environmental trends.
    - **Image-based**: Convolutional Neural Network (CNN) model to identify pests from uploaded crop images.

### 📊 Data Management
- Normalized visual trends via interactive charts.
- **Export to CSV**: Download historical sensor data for offline analysis.

---

## 🛠️ Tech Stack

- **Frontend**: React (Vite), Tailwind CSS, Recharts, Lucide React, Leaflet.
- **Backend*: Node.js, Express, MongoDB (Mongoose).
- **Machine Learning**: Python 3, TensorFlow/Keras, Scikit-Learn, Joblib, Numpy.
- **Hardware**: ESP32, DHT22, LDR, Soil Moisture Sensor, Rain Sensor, Relay Module.

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- **Node.js** (v18+)
- **MongoDB** (Local or Atlas)
- **Python** (v3.10+)
- **Arduino IDE** (for ESP32 upload)

### 2. Backend Setup
```bash
cd backend
npm install
```
- Ensure **MongoDB** is running on `mongodb://localhost:27017/smartplant`.
- Start the server:
```bash
node server.js
```

### 3. Machine Learning Setup
Install the required Python libraries:
```bash
pip install tensorflow numpy joblib scikit-learn pillow
```
*Note: Ensure your Python executable is in your system PATH as the backend spawns python processes.*

### 4. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
- The dashboard will be available at `http://localhost:5173`.

### 5. Hardware Setup (ESP32)
1. Open `ardu_code/ardu_code.ino` in Arduino IDE.
2. Install required libraries: `DHT`, `Crypto`, `ArduinoJson`.
3. Update specific constants in the code:
   - `ssid`: Your WiFi name.
   - `password`: Your WiFi password.
   - `serverName`: The IP address of your machine running the backend (e.g., `http://192.168.1.5:5000/api/sensors`).
4. Upload to your ESP32.

---

## 📁 Project Structure

- `/ardu_code`: ESP32 source code and hashing logic.
- `/backend`: Node.js server, API routes, and ML integration scripts.
- `/backend/ml`: Python scripts for prediction models.
- `/backend/models`: MongoDB schemas.
- `/frontend`: React application and dashboard components.
- `/paper`: Research documentation and related files.

---

## 📝 License
This project is licensed under the ISC License.
