import { useState } from "react";
import "./animations.css";
import AnimationButton from "./AnimationButton";

const animations = [
  { name: "Fade In/Out", type: "fade", color: " --fade-color" },
  { name: "Slide In/Out", type: "slide", color: "--slide-color" },
  { name: "Scale (Zoom)", type: "scale", color: "--scale-color" },
  { name: "Rotate", type: "rotate", color: "--rotate-color" },
  { name: "Bounce", type: "bounce", color: "--bounce-color" },
  { name: "Shake", type: "shake", color: "--shake-color" }
];

const AnimationDemo = () => {
  const [activeAnimation, setActiveAnimation] = useState<string | null>(null);

  const handleClick = (animation: string) => {
    setActiveAnimation(animation);
    setTimeout(() => setActiveAnimation(null), 1000); // Reset animation
  };

  return (
    <div className="container">
      <h1 className="header">CSS Animation Types</h1>
      {animations.map(({ name, type, color }) => (
        <AnimationButton
          key={type}
          name={name}
          type={type}
          color={color}
          activeAnimation={activeAnimation}
          handleClick={handleClick}
        />
      ))}
    </div>
  );
};

export default AnimationDemo;
