import React, { useEffect } from "react";
import "./HomePage.css";

const HomePage = () => {
  const url : string = '';

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

  function animateElement(element: any) {
    return new Promise(evolve => {
        element.style.transition = 'color 2s ease';
        element.style.color = 'red';
  
      element?.addEventListener('transitionend', () => {
        evolve('Animation completed');
      }, { once: true });
    });
  };
  
  const handleClick = () =>{
    const element = document.querySelector('#myElement');
    animateElement(element)
      .then(message => {
        console.log(message);
      })
      .catch(error => {
        console.error('Error during animation:', error);
      });
  };
  

  useEffect(() => {
    removePopup();
  }, []);

  return (
    <div className="home-page">
      <div id="myElement">
        My Component
      </div>
      <button onClick={handleClick}>Click To Animate</button>
    </div>
  );
};

export default HomePage;
