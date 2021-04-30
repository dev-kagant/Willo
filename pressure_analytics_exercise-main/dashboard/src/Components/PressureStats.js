import React from 'react';

function PressureStats(props) {
    const { num_contractions, contraction_per_sec } = props


    return (
        <div className="stats">
            <div>
                <h3>Number of Contractions</h3>
                <p>{num_contractions}</p>
            </div>
            <div>
                <h3>Contractions Per Second</h3>
                <p>{contraction_per_sec}</p>
            </div>
        </div>
    )
}

export default PressureStats;
