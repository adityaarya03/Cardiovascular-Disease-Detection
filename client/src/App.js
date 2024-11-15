import React, { useState } from 'react';
import { predict } from './api';
import './index.css'

function App() {
  const [formData, setFormData] = useState({
    age: '',
    gender: '',
    chestpain: '',
    restingBP: '',
    serumcholestrol: '',
    fastingbloodsugar: '',
    restingrelectro: '',
    maxheartrate: '',
    exerciseangia: '',
    oldpeak: '',
    slope: '',
    noofmajorvessels: '',
  });
  const [predictionResult, setPredictionResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await predict(formData);

    // Calculate the average of all model predictions
    const averagePrediction = Object.values(result).reduce((sum, pred) => sum + pred, 0) / Object.keys(result).length;

    // Determine if there is a high risk of cardiovascular disease
    const hasCardiovascularDisease = averagePrediction >= 0.8;

    // Set the result to be displayed
    setPredictionResult({ average: averagePrediction, hasCardiovascularDisease });
  };

  return (
    <div className=" flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold mb-4">Cardiovascular Disease Prediction</h1>
      <form onSubmit={handleSubmit} className="w-full max-w-md bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div className="grid grid-cols-2 gap-4">
          <input className="p-2 border rounded" type="number" name="age" value={formData.age} onChange={handleChange} placeholder="Age" />
          <input className="p-2 border rounded" type="text" name="gender" value={formData.gender} onChange={handleChange} placeholder="Gender" />
          <input className="p-2 border rounded" type="text" name="chestpain" value={formData.chestpain} onChange={handleChange} placeholder="Chest Pain" />
          <input className="p-2 border rounded" type="number" name="restingBP" value={formData.restingBP} onChange={handleChange} placeholder="Resting BP" />
          <input className="p-2 border rounded" type="number" name="serumcholestrol" value={formData.serumcholestrol} onChange={handleChange} placeholder="Serum Cholesterol" />
          <input className="p-2 border rounded" type="number" name="fastingbloodsugar" value={formData.fastingbloodsugar} onChange={handleChange} placeholder="Fasting Blood Sugar" />
          <input className="p-2 border rounded" type="text" name="restingrelectro" value={formData.restingrelectro} onChange={handleChange} placeholder="Resting Electro" />
          <input className="p-2 border rounded" type="number" name="maxheartrate" value={formData.maxheartrate} onChange={handleChange} placeholder="Max Heart Rate" />
          <input className="p-2 border rounded" type="text" name="exerciseangia" value={formData.exerciseangia} onChange={handleChange} placeholder="Exercise Angina" />
          <input className="p-2 border rounded" type="number" name="oldpeak" value={formData.oldpeak} onChange={handleChange} placeholder="Old Peak" />
          <input className="p-2 border rounded" type="number" name="slope" value={formData.slope} onChange={handleChange} placeholder="Slope" />
          <input className="p-2 border rounded" type="number" name="noofmajorvessels" value={formData.noofmajorvessels} onChange={handleChange} placeholder="No of Major Vessels" />
        </div>
        <button type="submit" className="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded mt-4 hover:bg-blue-700">
          Predict
        </button>
      </form>
      {predictionResult && (
        <div className={`text-center p-4 w-full max-w-md rounded-lg shadow-md ${predictionResult.hasCardiovascularDisease ? 'bg-red-100 border-red-400 text-red-700' : 'bg-green-100 border-green-400 text-green-700'}`}>
          <h2 className="text-xl font-semibold">
            {predictionResult.hasCardiovascularDisease ? 'High Risk of Cardiovascular Disease' : 'Low Risk of Cardiovascular Disease'}
          </h2>
          <p className="mt-2">Average Prediction Score: {predictionResult.average.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
