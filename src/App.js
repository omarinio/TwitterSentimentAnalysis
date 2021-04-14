import React from 'react';
import BarChart from './Charts/BarChart'
import AmericaMap from './Charts/AmericaMap'
import ReactTooltip from "react-tooltip";


class App extends React.Component {
 state={
   content: "",
   setContent: ""
 }
 render(){
  const {content, setContent} = this.state
  return (
    <div style={{backgroundColor: '#FAFAFA'}}>
      <div>
        <h1 style={{textAlign: 'center', color: '#151515', paddingTop: '20px', marginTop: '-10px'}}>Sentinent Analysis on the US Election </h1>
      </div>
      <div style={{textAlign: 'center'}}>
        <h2 style={{color: '#151515'}}>Interactive Map of America</h2>
        <h3 style={{color: '#151515'}}>Hover over each state for a breakdown of that state</h3>
        <div style={{textAlign: 'center', width: '80%', display: 'inline flow-root list-item'}}>
          <AmericaMap setTooltipContent={setContent}/>
          <ReactTooltip>{content}</ReactTooltip>
        </div>
      </div>
    </div>
  );
 }
}

export default App;