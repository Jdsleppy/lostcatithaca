import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';

import Map from './pages/Map';
import About from './pages/About';


export default function App() {
  return (
    <Router>
      <div className="layout">
        <ul className="navlinks">
          <li>
            <Link to="/">Map</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>

        <Switch>
          <Route exact path="/">
            <Map />
          </Route>
          <Route path="/about">
            <About />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

