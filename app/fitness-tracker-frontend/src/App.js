import React from 'react';
import WorkoutList from './components/WorkoutList'; 

const App = () => {
  return (
    <div>
      <h1>Fitness Tracker App</h1>
      <WorkoutList /> {/* Render the WorkoutList component */}
    </div>
  );
};

export default App;
