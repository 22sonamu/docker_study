
//Counter.jsx
import React, { useState, useEffect } from "react";

const Counter = (props) => {

  const [count, setCount] = useState(props.initCount);

  const onIncrease = () => {
    setCount(prevCount => prevCount + 1);
  };
  const onDecrease = () => {
    setCount(prevCount => prevCount - 1);
  };
  return (
    <>
      <h1>{count}</h1>
      <button onClick={onIncrease}>+1</button>
      <button onClick={onDecrease}>-1</button>
    </>
  );
};

export default Counter;