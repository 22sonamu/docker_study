//App.js
import React from "react";
import Counter from "./Counter";


const App = () => {

  const res = fetch(
    "backend:8081"
  ).then((res) => res.json());

  console.log(res.json().toString());
  
  const initData = res.slice(0, 20).map((it) => {
    return {
      count : it.count
    };
  });

  return <Counter initCount = { initData.count } ></Counter>;
};

export default App;