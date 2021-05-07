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
  console.log(event.target.dataset.name)
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
   var dataSource = [
    ["Alabama", 95.7, 0.0412, 0.0672, 62, 37, "Incorrect"],
    ["Alaska", 99.0, 0.0819, 0.0216, 53, 43, "Correct"],
    ["Arizona", 97.4, 0.0096, 0.0701, 49, 49, "Correct"],
    ["Arkansas", 97.5, -0.0194, 0.0479, 62, 35, "Incorrect"],
    ["California", 95.5, -0.0144, 0.1033, 33, 65, "Correct"],
    ["Colorado", 101.6, 0.0043, 0.1152, 42, 55, "Incorrect"],
    ["Connecticut", 103.1, -0.0123, 0.0647, 39, 59, "Correct"],
    ["Delaware", 100.4, -0.0687, 0.1641, 40, 59, "Correct"],
    ["Florida", 98.4, 0.0115, 0.0784, 51, 48, "Incorrect"],
    ["Georgia", 98.0, 0.0166, 0.0884, 49, 50, "Correct"],
    ["Hawaii", 95.6, 0.0066, 0.0465, 34, 64, "Correct"],
    ["Idaho", 101.4, -0.0207, 0.0654, 64, 33, "Incorrect"],
    ["Illinois", 99.9, -0.0327, 0.0902, 41, 57, "Correct"],
    ["Indiana", 101.7, 0.0844, 0.1575, 57, 41, "Incorrect"],
    ["Iowa", 103.2, -0.0513, 0.0850, 53, 45, "Incorrect"],
    ["Kansas", 102.8, 0.0395, 0.1311, 56, 42, "Incorrect"],
    ["Kentucky", 99.4, 0.0218, 0.0650, 62, 36, "Incorrect"],
    ["Louisiana", 95.3, 0.0667, 0.1860, 59, 40, "Incorrect"],
    ["Maine", 103.4, 0.0089, 0.1268, 44, 53, "Correct"],
    ["Maryland", 99.7, -0.0412, 0.0576, 32, 65, "Correct"],
    ["Massachusetts", 104.3, -0.0317, 0.0994, 32, 66, "Correct"],
    ["Michigan", 100.5, -0.0513, 0.0588, 48, 51, "Correct"],
    ["Minnesota", 103.7, -0.0025, 0.0934, 45, 52, "Correct"],
    ["Mississippi", 94.2, 0.0230, 0.0437, 57, 41, "Correct"],
    ["Missouri", 101.0, -0.0401, 0.0791, 57, 41, "Incorrect"],
    ["Montana", 103.4, -0.0509, 0.0526, 57, 41, "Incorrect"],
    ["Nebraska", 102.3, 0.0499, 0.0753, 58, 39, "Incorrect"],
    ["Nevada", 96.5, 0.0143, 0.1240, 48, 50, "Correct"],
    ["New Hampshire", 104.2, -0.0265, 0.0425, 45, 53, "Correct"],
    ["New Jersey", 102.8, -0.0085, 0.0783, 41, 57, "Correct"],
    ["New Mexico", 95.7, 0.0395, 0.1416, 44, 54, "Correct"],
    ["New York", 100.7, -0.0390, 0.0890, 38, 61, "Correct"],
    ["North Carolina", 100.2, 0.0064, 0.1005, 50, 49, "Incorrect"],
    ["North Dakota", 103.8, -0.0630, 0.0964, 65, 32, "Incorrect"],
    ["Ohio", 101.8, -0.0105, 0.0839, 53, 45, "Incorrect"],
    ["Oklahoma", 99.3, -0.0384, 0.0850, 65, 32, "Incorrect"],
    ["Oregon", 101.2, -0.0342, 0.0793, 40, 56, "Correct"],
    ["Pennsylvania", 101.5, -0.0710, 0.0910, 49, 50, "Correct"],
    ["Rhode Island", 99.5, 0.0111, 0.1014, 39, 59, "Correct"],
    ["South Carolina", 98.4, -0.0506, 0.0163, 55, 43, "Incorrect"],
    ["South Dakota", 102.8, 0.0864, 0.1721, 62, 36, "Incorrect"],
    ["Tennessee", 97.7, 0.0319, 0.1106, 61, 38, "Incorrect"],
    ["Texas", 100.0, -0.0141, 0.0775, 52, 46, "Incorrect"],
    ["Utah", 101.1, -0.0050, 0.0409, 58, 38, "Incorrect"],
    ["Vermont", 103.9, -0.1301, 0.0433, 31, 66, "Correct"],
    ["Virginia", 101.9, -0.0273, 0.1045, 44, 54, "Correct"],
    ["Washington", 101.9, -0.03551, 0.0962, 39, 58, "Correct"],
    ["West Virginia", 98.7, 0.0103, 0.0636, 69, 30, "Incorrect"],
    ["Wisconsin", 102.9, -0.0287, 0.1153, 49, 49, "Correct"],
    ["Wyoming", 102.4, 0.0146, 0.0520, 70, 27, "Incorrect"],
   ]

   var data
   var dataAllStates
   console.log(dataSource.length)
   if(stateName === 'All'){
    dataAllStates = ["USA", 98.0, -0.0178, 0.0713, 43, 57, '-']
   } else if(stateName === 'AL'){
    data = dataSource[0]
   } else if(stateName === 'AK'){
    data = dataSource[1]
   } else if(stateName === 'AZ'){
    data = dataSource[2]
   } else if(stateName === 'AR'){
    data = dataSource[3]
   } else if(stateName === 'CA'){
    data = dataSource[4]
   } else if(stateName === 'CO'){
    data = dataSource[5]
   } else if(stateName === 'CT'){
    data = dataSource[6]
   } else if(stateName === 'DE'){
    data = dataSource[7]
   } else if(stateName === 'FL'){
    data = dataSource[8]
   } else if(stateName === 'GA'){
    data = dataSource[9]
   } else if(stateName === 'HI'){
    data = dataSource[10]
   } else if(stateName === 'ID'){
    data = dataSource[11]
   } else if(stateName === 'IL'){
    data = dataSource[12]
   } else if(stateName === 'IN'){
    data = dataSource[13]
   } else if(stateName === 'IA'){
    data = dataSource[14]
   } else if(stateName === 'KS'){
    data = dataSource[15]
   } else if(stateName === 'KY'){
    data = dataSource[16]
   } else if(stateName === 'LA'){
    data = dataSource[17]
   } else if(stateName === 'ME'){
    data = dataSource[18]
   } else if(stateName === 'MD'){
    data = dataSource[19]
   } else if(stateName === 'MA'){
    data = dataSource[20]
   } else if(stateName === 'MI'){
    data = dataSource[21]
   } else if(stateName === 'MN'){
    data = dataSource[22]
   } else if(stateName === 'MS'){
    data = dataSource[23]
   } else if(stateName === 'MO'){
    data = dataSource[24]
   } else if(stateName === 'MT'){
    data = dataSource[25]
   } else if(stateName === 'NE'){
    data = dataSource[26]
   } else if(stateName === 'NV'){
    data = dataSource[27]
   } else if(stateName === 'NH'){
    data = dataSource[28]
   } else if(stateName === 'NJ'){
    data = dataSource[29]
   } else if(stateName === 'NM'){
    data = dataSource[30]
   } else if(stateName === 'NY'){
    data = dataSource[31]
   } else if(stateName === 'NC'){
    data = dataSource[32]
   } else if(stateName === 'ND'){
    data = dataSource[33]
   } else if(stateName === 'OH'){
    data = dataSource[34]
   } else if(stateName === 'OK'){
    data = dataSource[35]
   } else if(stateName === 'OR'){
    data = dataSource[36]
   } else if(stateName === 'PA'){
    data = dataSource[37]
   } else if(stateName === 'RI'){
    data = dataSource[38]
   } else if(stateName === 'SC'){
    data = dataSource[39]
   } else if(stateName === 'SD'){
    data = dataSource[40]
   } else if(stateName === 'TN'){
    data = dataSource[41]
   } else if(stateName === 'TX'){
    data = dataSource[42]
   } else if(stateName === 'UT'){
    data = dataSource[43]
   } else if(stateName === 'VT'){
    data = dataSource[44]
   } else if(stateName === 'VA'){
    data = dataSource[45]
   } else if(stateName === 'WA'){
    data = dataSource[46]
   } else if(stateName === 'WV'){
    data = dataSource[47]
   } else if(stateName === 'WI'){
    data = dataSource[48]
   } else if(stateName === 'WY'){
    data = dataSource[49]
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
                <option value="MD">Maryland</option>
                <option value="MA">Massachusetts</option>
                <option value="MI">Michigan</option>
                <option value="MN">Minnesota</option>
                <option value="MS">Mississippi</option>
                <option value="MO">Missouri</option>
                <option value="MT">Montana</option>
                <option value="NE">Nebraska</option>
                <option value="NV">Nevada</option>
                <option value="NH">New Hampshire</option>
                <option value="NJ">New Jersey</option>
                <option value="NM">New Mexico</option>
                <option value="NY">New York</option>
                <option value="NC">North Carolina</option>
                <option value="ND">North Dakota</option>
                <option value="OH">Ohio</option>
                <option value="OK">Oklahoma</option>
                <option value="OR">Oregon</option>
                <option value="PA">Pennsylvania</option>
                <option value="RI">Rhode Island</option>
                <option value="SC">South Carolina</option>
                <option value="SD">South Dakota</option>
                <option value="TN">Tennessee</option>
                <option value="TX">Texas</option>
                <option value="UT">Utah</option>
                <option value="VT">Vermont</option>
                <option value="VA">Virginia</option>
                <option value="WA">Washington</option>
                <option value="WV">West Virginia</option>
                <option value="WI">Wisconsin</option>
                <option value="WY">Wyoming</option>
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