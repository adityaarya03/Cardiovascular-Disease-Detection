import React, { useState } from 'react';
import { predict } from './api';

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
  const [predictions, setPredictions] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await predict(formData);
    setPredictions(result);
  };

  return (
    <div>
      <h1>Cardiovascular Disease Prediction</h1>
      <form onSubmit={handleSubmit}>
        <input type="number" name="age" value={formData.age} onChange={handleChange} placeholder="Age" />
        <input type="text" name="gender" value={formData.gender} onChange={handleChange} placeholder="Gender" />
        <input type="text" name="chestpain" value={formData.chestpain} onChange={handleChange} placeholder="Chest Pain" />
        <input type="number" name="restingBP" value={formData.restingBP} onChange={handleChange} placeholder="Resting BP" />
        <input type="number" name="serumcholestrol" value={formData.serumcholestrol} onChange={handleChange} placeholder="Serum Cholesterol" />
        <input type="number" name="fastingbloodsugar" value={formData.fastingbloodsugar} onChange={handleChange} placeholder="Fasting Blood Sugar" />
        <input type="text" name="restingrelectro" value={formData.restingrelectro} onChange={handleChange} placeholder="Resting Electro" />
        <input type="number" name="maxheartrate" value={formData.maxheartrate} onChange={handleChange} placeholder="Max Heart Rate" />
        <input type="text" name="exerciseangia" value={formData.exerciseangia} onChange={handleChange} placeholder="Exercise Angina" />
        <input type="number" name="oldpeak" value={formData.oldpeak} onChange={handleChange} placeholder="Old Peak" />
        <input type="number" name="slope" value={formData.slope} onChange={handleChange} placeholder="Slope" />
        <input type="number" name="noofmajorvessels" value={formData.noofmajorvessels} onChange={handleChange} placeholder="No of Major Vessels" />
        <button type="submit">Predict</button>
      </form>
      {predictions && (
        <div>
          <h2>Predictions</h2>
          {Object.entries(predictions).map(([model, pred]) => (
            <p key={model}>{model}: {pred}</p>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
