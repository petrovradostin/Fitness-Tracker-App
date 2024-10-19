import React, { useEffect, useState } from 'react';
import axios from 'axios'; 

const WorkoutList = () => {
  const [workouts, setWorkouts] = useState([]); 

  
  useEffect(() => {
    axios.get('http://localhost:5000/api/workouts')
      .then(response => {
        setWorkouts(response.data); 
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
      });
  }, []); 

  return (
    <div>
      <h1>Workout List</h1>
      <ul>
        {workouts.map((workout, index) => (
          <li key={index}>{workout.name}</li> 
        ))}
      </ul>
    </div>
  );
};

export default WorkoutList;
