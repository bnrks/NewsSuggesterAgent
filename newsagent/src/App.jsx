import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import NewsForm from "./components/NewsForm";
function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <NewsForm />
    </>
  );
}

export default App;
