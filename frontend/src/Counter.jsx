
//Counter.jsx
import React, { useState , useEffect} from "react";

const Counter = () => {
  
  const [count, setCount] = useState();

  useEffect(() => {
    //db에서 count get
		const fetchData = async() => {
          const res = await fetch('/get');
          const result = res.json();
          return result;
        }	
        fetchData().then(res => setCount(parseInt(res.count)));
    }, []);


  const onIncrease = () => {
    setCount(prevCount => prevCount + 1);
    //DB 업데이트
    fetch("/update/" + (count+1).toString(), {
      headers: {
        Accept: "application / json",
      },
      method: "GET",
    })
    .then(res => res.json())
    .then(data => {
      
    });
  };
  const onDecrease = () => {
    setCount(prevCount => prevCount - 1);
    //DB 업데이트
    fetch("/update/" + (count-1).toString(), {
      headers: {
        Accept: "application / json",
      },
      method: "GET",
    })
    .then(res => res.json())
    .then(data => {
      
    });
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