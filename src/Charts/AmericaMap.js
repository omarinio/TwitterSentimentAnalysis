import React, { useState, useEffect } from "react";
import { ComposableMap, Geographies, Geography, ZoomableGroup } from "react-simple-maps";
import { scaleQuantize } from "d3-scale";
import { csv } from "d3-fetch";

const geoUrl = "https://cdn.jsdelivr.net/npm/us-atlas@3/counties-10m.json";

const colorScale = scaleQuantize()
  .domain([1, 10])
  .range([
    "#A9E2F3",
    "#81DAF5",
    "#58D3F7",
    "#2ECCFA",
    "#00BFFF",
    "#01A9DB",
    "#0489B1",
    "#086A87",
    "#0B4C5F"
  ]);

const AmericaMap = ({setTooltipContent}) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // https://www.bls.gov/lau/
    csv("/unemployment-by-county-2017.csv").then(counties => {
      setData(counties);
    });
  }, []);

  return (
    <>
      <ComposableMap data-tip="" projection="geoAlbersUsa">
        <ZoomableGroup zoom={1}>
            <Geographies geography={geoUrl}>
            {({ geographies }) =>
                geographies.map(geo => {
                const cur = data.find(s => s.id === geo.id);
                return (
                    <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    fill={colorScale(cur ? cur.unemployment_rate : "#EEE")}
                    // onMouseEnter={() => {
                    //     const { NAME, POP_EST } = geo.properties;
                    //     setTooltipContent(`${NAME} — ${rounded(POP_EST)}`);
                    //   }}
                    //   onMouseLeave={() => {
                    //     setTooltipContent("");
                    //   }}
                    //   style={{
                    //     default: {
                    //       fill: "#D6D6DA",
                    //       outline: "none"
                    //     },
                    //     hover: {
                    //       fill: "#F53",
                    //       outline: "none"
                    //     },
                    //     pressed: {
                    //       fill: "#E42",
                    //       outline: "none"
                    //     }
                    //   }}
                    />
                );
                })
            }
            </Geographies>
        </ZoomableGroup>
      </ComposableMap>
    </>
  );
};

export default AmericaMap;
