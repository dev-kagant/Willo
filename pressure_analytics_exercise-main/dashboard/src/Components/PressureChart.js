import React from 'react';
import { Line } from 'react-chartjs-2';

import './Pressure.css'

const PressureChart = (props) => {
    const ms = [];
    const pressure = [];
    for (let i = 0; i < props.data.length; i++) {
        ms.push(props.data[i].ms + "ms")
        pressure.push(props.data[i].pressure)
    }

    const data = {
        labels: ms,
        datasets: [
            {
                label: 'Pressure (kPa)',
                data: pressure,
                borderColor: ['rgba(3, 30, 210, 0.35)'],
                backgroundColor: ['rgba(3, 30, 210, 0.35)'],
                pointBackgroundColor: 'rgba(3, 30, 210, 0.70)',
                pointBorderColor: 'rgba(3, 30, 210, 0.35)',
            }
        ]
    }

    let options = {
        scales: {
            yAxes:
            {
                ticks: {
                    min: 70,
                    max: 110,
                    stepSize: 2,
                }
            },
        },
    }

    return (
        <div className="chart">
            <h1>Pressure by Milliseconds</h1>
            <Line data={data} options={options} />
        </div>
    )
}

export default PressureChart;
