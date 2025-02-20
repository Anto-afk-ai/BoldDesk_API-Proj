import React, { useEffect, useRef } from "react";
import "./HomePage.css";
import {
  AxesDirective,
  AxisDirective,
  CircularGaugeComponent,
  PointersDirective,
  PointerDirective,
  FontModel,
  GaugeTheme,
  IThemeStyle,
} from "@syncfusion/ej2-react-circulargauge";

const HomePage = () => {
  const fontModel: FontModel = {
    size: "18",
    color: "Red",
    fontWeight: "400",
    fontStyle: "Underline",
    fontFamily: "Cambria",
  };
  const componentRef = useRef<CircularGaugeComponent>(null);

  const gaugeTheme : GaugeTheme = 'Material3';
  const themeStyle : IThemeStyle = {
      backgroundColor: 'red',
      titleFontColor: '#ffffff',
      tooltipFillColor: 'black',
      tooltipFontColor: "#ffffff",
      tooltipFontSize: "14",
      lineColor: "black",
      labelColor: "#ffffff",
      majorTickColor: "red",
      minorTickColor: "white",
      pointerColor: "white",
      needleColor: "black",
      needleTailColor: "red",
      capColor: "white"
  } 

  function removePopup() {
    const matchingDivs = Array.from(document.querySelectorAll("div")).filter(
      (div) => {
        return div.innerText.includes(
          "This application was built using a trial"
        );
      }
    );
    matchingDivs[0]?.parentElement?.removeChild(matchingDivs[0]);
  };

  useEffect(()=>{
    if (componentRef.current) 
         componentRef.current.themeStyle = themeStyle
    removePopup();
  },[]);

  return (
    <div className="home-page">
      <CircularGaugeComponent theme={gaugeTheme} ref={componentRef}>
        <AxesDirective>
          <AxisDirective>
            <PointersDirective>
              <PointerDirective
                textStyle={fontModel}
                needleStartWidth={5}
                value={35}
              ></PointerDirective>
            </PointersDirective>
          </AxisDirective>
        </AxesDirective>
      </CircularGaugeComponent>
    </div>
  );
};

export default HomePage;
