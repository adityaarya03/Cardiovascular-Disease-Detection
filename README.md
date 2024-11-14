Efficient Prediction of Cardiovascular Disease Using Machine Learning Algorithms With Relief and LASSO Feature Selection Techniques And IOT An Overview of Advanced Feature Selection in Predictive Models And A Comprehensive Approach for Early Diagnosis and Risk Prediction.

Below are the detailed steps and commands for running the app on both macOS and Windows, assuming that you’ve already set up the project folder structure and saved the model files.
---

### 1. **Set Up the Flask Backend**

#### macOS
1. Open a terminal and navigate to the Flask backend folder:
   ```bash
   cd path/to/your/Project-Root/Flask-server
   ```
2. **Create a virtual environment** (if not already created):
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```
4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Flask server**:
   ```bash
   python app.py
   ```
   By default, the server will run on `http://127.0.0.1:5000`.

#### Windows
1. Open Command Prompt or PowerShell and navigate to the Flask backend folder:
   ```cmd
   cd path\to\your\Project-Root\Flask-server
   ```
2. **Create a virtual environment** (if not already created):
   ```cmd
   python -m venv venv
   ```
3. **Activate the virtual environment**:
   ```cmd
   venv\Scripts\activate
   ```
4. **Install the required packages**:
   ```cmd
   pip install -r requirements.txt
   ```
5. **Run the Flask server**:
   ```cmd
   python app.py
   ```
   By default, the server will run on `http://127.0.0.1:5000`.

---

### 2. **Set Up the React Frontend**

#### macOS and Windows
1. Open a new terminal (or Command Prompt/PowerShell on Windows) and navigate to the React app folder:
   ```bash
   cd path/to/your/Project-Root/Client
   ```
2. **Install the React dependencies**:
   ```bash
   npm install
   ```
3. **Start the React development server**:
   ```bash
   npm start
   ```
   The React app will open in your default browser at `http://localhost:3000`.

---

### 3. **Test the Application**

Once both servers are running:

1. Open a browser and go to `http://localhost:3000`.
2. Fill in the input fields with test data and click the "Predict" button.
3. The predictions should appear below the form, showing results from each model.

---

### **Stopping the Servers**

- **For Flask**: Press `Ctrl+C` in the terminal where Flask is running.
- **For React**: Press `Ctrl+C` in the terminal where the React development server is running.

---

### **Additional Notes**

- Make sure that the Flask server (`http://127.0.0.1:5000`) is running before using the React frontend.
- If you make changes to the code in the Flask or React app, restart the respective server(s) to see the updates.

Following these steps will get your application running on both macOS and Windows. Let me know if you encounter any issues!
