import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import reportWebVitals from './reportWebVitals';

const AppInternal = function () {
  const [content, setContent] = useState(<></>);

  useEffect(() => {
    if (window.pywebview) {
      setContent(<App />);
    } else {
      const handleReady = () => setContent(<App />);
      window.addEventListener("pywebviewready", handleReady);

      return () => window.removeEventListener("pywebviewready", handleReady);
    }
  }, []);

  return content;
};

const element = document.getElementById('app');
// Render AppInternal as a JSX component tag, not a plain function call
ReactDOM.render(<AppInternal />, element);

export default AppInternal;

reportWebVitals();
