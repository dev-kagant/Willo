import pressure from './pressure.json';
import PressureChart from './Components/PressureChart'
import PressureStats from './Components/PressureStats'
import './index.css'

function App() {
  return (
    <div className="App">
      <div>
        <PressureChart data={pressure.pressure_points} />
      </div>
      <div>
        <PressureStats
          num_contractions={pressure.count_contractions}
          contraction_per_sec={pressure.contractions_per_sec}
        />
      </div>
    </div>
  );
}

export default App;
