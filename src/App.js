import React from 'react';
import USAMap from "react-usa-map";
import './styles/styling.css'
import Progress from 'react-progressbar';


class App extends React.Component {
state={
  stateName: 'All'
}
 mapHandler = (event) => {
  this.setState({stateName: event.target.dataset.name})
};

calculateSentimentPercentage = (sentimentValue) => {
  var sentimentValuePercentage
  if(sentimentValue > 0){
    sentimentValuePercentage = sentimentValue * 100
  } else {
    sentimentValuePercentage = (sentimentValue - sentimentValue - sentimentValue) * 100
  }
  return sentimentValuePercentage
}

/* optional customization of filling per state and calling custom callbacks per state */
statesCustomConfig = () => {
  return {
      "AL": {
          fill: "#FF0000"
      },
      "AK": {
          fill: "#FF0000"
      },
      "AZ": {
          fill: "#0015BC"
      },
      "AR": {
          fill: "#FF0000"
      },
      "CA": {
          fill: "#0015BC"
      },
      "CO": {
          fill: "#0015BC"
      },
      "CT": {
          fill: "#0015BC"
      },
      "DE": {
          fill: "#0015BC"
      },
      "FL": {
          fill: "#FF0000"
      },
      "GA": {
          fill: "#0015BC"
      },
      "HI": {
          fill: "#0015BC"
      },
      "ID": {
          fill: "#FF0000"
      },
      "IL": {
          fill: "#0015BC"
      },
      "IN": {
          fill: "#FF0000"
      },
      "IA": {
          fill: "#FF0000"
      },
      "KS": {
          fill: "#FF0000"
      },
      "KY": {
          fill: "#FF0000"
      },
      "LA": {
          fill: "#FF0000"
      },
      "ME": {
          fill: "#0015BC"
      },
      "MD": {
          fill: "#0015BC"
      },
      "MA": {
          fill: "#0015BC"
      },
      "MI": {
          fill: "#0015BC"
      },
      "MN": {
          fill: "#0015BC"
      },
      "MS": {
          fill: "#FF0000"
      },
      "MO": {
          fill: "#FF0000"
      },
      "MT": {
          fill: "#FF0000"
      },
      "NE": {
          fill: "#FF0000"
      },
      "NV": {
          fill: "#0015BC"
      },
      "NH": {
          fill: "#0015BC"
      },
      "NJ": {
          fill: "#0015BC"
      },
      "NM": {
          fill: "#0015BC"
      },
      "NY": {
          fill: "#0015BC"
      },
      "NC": {
          fill: "#FF0000"
      },
      "ND": {
          fill: "#FF0000"
      },
      "OH": {
          fill: "#FF0000"
      },
      "OK": {
          fill: "#FF0000"
      },
      "OR": {
          fill: "#0015BC"
      },
      "PA": {
          fill: "#0015BC"
      },
      "RI": {
          fill: "#0015BC"
      },
      "SC": {
          fill: "#FF0000"
      },
      "SD": {
          fill: "#FF0000"
      },
      "TN": {
          fill: "#FF0000"
      },
      "TX": {
          fill: "#FF0000"
      },
      "UT": {
          fill: "#FF0000"
      },
      "VT": {
          fill: "#0015BC"
      },
      "VA": {
          fill: "#0015BC"
      },
      "WA": {
          fill: "#0015BC"
      },
      "WV": {
          fill: "#FF0000"
      },
      "WI": {
          fill: "#0015BC"
      },
      "WY": {
          fill: "#FF0000",
          clickHandler: (event) => console.log('Custom handler for NJ', event.target.dataset)
      },
  };
};

 render(){
   const { stateName } = this.state
   var data
   var dataAllStates
   if(stateName === 'All'){
    dataAllStates = ["USA", 98.0, -0.0178, 0.0713, 43, 57, '-']
   } else if(stateName === 'FL'){
    data = ["Florida", 98.4, 0.0115, 0.0784, 51, 48, "Incorrect"]
   } else if(stateName === 'CA'){
    data = ["California", 95.5, -0.0144, 0.1033, 33, 65, "Correct"]
   } else if(stateName === 'TX'){
    data = ["Texas", 100, -0.0141, 0.0775, 52, 46, "Incorrect"]
   } else if(stateName === 'MN'){
    data = ["Minnesota", 103.7, -0.0025, 0.0934, 45, 53, "Correct"]
   } else if(stateName === 'OH'){
    data = ["Ohio", 101.8, -0.0105, 0.0839, 53, 45, "Incorrect"]
   } else if(stateName === 'MT'){
    data = ["Montana", 103.4, -0.0509, 0.0526, 57, 40, "Incorrect"]
   } else if(stateName === 'UT'){
    data = ["Utah", 101.1, -0.0050, 0.0409, 58, 38, "Incorrect"]
   } else if(stateName === 'MO'){
    data = ["Missouri", 101.0, -0.0401, 0.0791, 57, 41, "Incorrect"]
   } else {
    data = ["USA", 98.0, -0.0178, 0.0713, 43, 57, '-']
   }
  return (
    <div>
      <div>
        <h1 style={{textAlign: 'center', color: '#151515', paddingTop: '20px', marginTop: '-10px'}}>Sentiment Analysis on the US Election </h1>
      </div>
      <div style={{textAlign: 'center'}}>
        <div style={{textAlign: 'center', display: 'flex', justifyContent: 'center'}}>
          <div style={{textAlign: 'center', width: '80%', display: 'inline flow-root list-item'}}>
            <h2 style={{color: '#151515'}}>Interactive Map of America</h2>
            <h2 style={{color: '#151515'}}>Click each State for a breakdown of that State</h2>
            <USAMap customize={this.statesCustomConfig()} onClick={this.mapHandler} />
          </div>
          <div style={{textAlign: 'center', justifyContent: 'center', width: '80%', display: 'inline flow-root', paddingRight: 5}}>
            <div>
              <h2>Select a State for a breakdown of the results</h2>
              <select
                className="browser-default custom-select"
                value={stateName}
                onChange={e => this.setState({ stateName: e.target.value })}
              >
                <option value="">Select a State</option>
                <option value="AL">Alabama</option>
                <option value="AK">Alaska</option>
                <option value="AZ">Arizona</option>
                <option value="AR">Arkansas</option>
                <option value="CA">California</option>
                <option value="CO">Colorado</option>
                <option value="CT">Connecticut</option>
                <option value="DE">Delaware</option>
                <option value="DC">District of Columbia</option>
                <option value="FL">Florida</option>
                <option value="GA">Georgia</option>
                <option value="HI">Hawaii</option>
                <option value="ID">Idaho</option>
                <option value="IL">Illinois</option>
                <option value="IN">Indiana</option>
                <option value="IA">Iowa</option>
                <option value="KS">Kansas</option>
                <option value="KY">Kentucky</option>
                <option value="LA">Louisiana</option>
                <option value="ME">Maine</option>
                <option value="MN">Minnesota</option>
                <option value="MT">Montana</option>
                <option value="MO">Missouri</option>
                <option value="TX">Texas</option>
                <option value="UT">Utah</option>
              </select>
            </div>
            <br />
            <h2 style={{color: '#151515'}}>A breakdown of the data</h2>
            <div style={{textAlign: 'center', width: '100%'}}>
              <table>
                <tr>
                    <th>State</th>
                    <th>IQ</th>
                    <th>Trump Sentiment</th>
                    <th>Biden Sentiment</th>
                    <th>Trumps Actual Results</th>
                    <th>Bidens Actual Results</th>
                    <th>Prediction Off Sentiment Analysis</th>
                </tr>
                {stateName !== "All" ?
                <tr>
                    <th>{data[0]}</th>
                    <th>{data[1]}</th>
                    <th>{data[2] * 100}%</th>
                    <th>{data[3] * 100}%</th>
                    <th><Progress color="#FF0000" completed={data[4]} /><p>{data[4]}%</p></th>
                    <th><Progress color="#0015BC" completed={data[5]} /><p>{data[5]}%</p></th>
                    <th>{data[6]}</th>
                </tr>
                :
                <tr>
                    <th>{dataAllStates[0]}</th>
                    <th>{dataAllStates[1]}</th>
                    <th>{dataAllStates[2] * 100}%</th>
                    <th>{dataAllStates[3] * 100}%</th>
                    <th><Progress color="#FF0000" completed={dataAllStates[4]} /><p>{dataAllStates[4]}%</p></th>
                    <th><Progress color="#0015BC" completed={dataAllStates[5]} /><p>{dataAllStates[5]}%</p></th>
                    <th>{dataAllStates[6]}</th>
                </tr>
                }
              </table> 
            </div>
            <br />
            <br />
            <div>
              {stateName !== 'All' ?
                <div>
                  <Progress color="#FF0000" completed={this.calculateSentimentPercentage(data[2])} /><p style={{fontWeight: 'bolder'}}>Trump Sentiment Value: {data[2] * 100}% - {data[2] > 0 ? "Positive" : "Negative"}</p>
                  <br />
                  <Progress color="#0015BC" completed={this.calculateSentimentPercentage(data[3])} /><p style={{fontWeight: 'bolder'}}>Biden Sentiment Value: {data[3] * 100}% - {data[3] > 0 ? "Positive" : "Negative"}</p>
                  <br />
                  <Progress color="#FF0000" completed={data[4]} /><p style={{fontWeight: 'bolder'}}>Trump Actual Results: {data[4]}%</p>
                  <br />
                  <Progress color="#0015BC" completed={data[5]} /><p style={{fontWeight: 'bolder'}}>Biden Actual Results: {data[5]}%</p>
                </div>
              :
              <div>
                <Progress color="#FF0000" completed={this.calculateSentimentPercentage(dataAllStates[2])} /><p style={{fontWeight: 'bolder'}}>Trump Sentiment Value: {dataAllStates[2] * 100}% - {dataAllStates[2] > 0 ? "Positive" : "Negative"}</p>
                <br />
                <Progress color="#0015BC" completed={this.calculateSentimentPercentage(dataAllStates[3])} /><p style={{fontWeight: 'bolder'}}>Biden Sentiment Value: {dataAllStates[3] * 100}% - {dataAllStates[3] > 0 ? "Positive" : "Negative"}</p>
                <br />
                <Progress color="#FF0000" completed={dataAllStates[4]} /><p style={{fontWeight: 'bolder'}}>Trump Actual Results: {dataAllStates[4]}%</p>
                <br />
                <Progress color="#0015BC" completed={dataAllStates[5]} /><p style={{fontWeight: 'bolder'}}>Biden Actual Results: {dataAllStates[5]}%</p>
              </div>
              }
            </div>
          </div>
        </div>
      </div>
    </div>
  );
 }
}

export default App;