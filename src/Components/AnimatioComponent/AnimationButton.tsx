import React from "react";

interface AnimationButtonProps {
  name: string;
  type: string;
  color: string;
  activeAnimation: string | null;
  handleClick: (type: string) => void;
}

const AnimationButton: React.FC<AnimationButtonProps> = ({
  name,
  type,
  color,
  activeAnimation,
  handleClick,
}) => {
  return (
    <button
      type="button"
      style={{background: `var(${color})`}}
      className={`button-item ${
        activeAnimation === type ? type : ""
      }`}
      onClick={() => handleClick(type)}
    >
      {name}
    </button>
  );
};

export default AnimationButton;
