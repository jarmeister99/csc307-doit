import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navigation from "./components/Navigation"
import Footer from "./components/Footer"
import Home from "./components/Home"
import Login from "./components/Login"
import Register from "./components/Register"
import EditTask from "./components/EditTask"
import Tasks from "./components/Tasks"


function MyApp() {
  return (
    <div id="MyApp">
      <Router>
        <Navigation />
        <Switch>
          <Route path="/" exact component={() => <Home />} />
          <Route path="/login" exact component={() => <Login />} />
          <Route path="/tasks" exact component={() => <Tasks />} />
          <Route path="/register" exact component={() => <Register />} />
          <Route path="/edittask" exact component={() => <EditTask />} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default MyApp;
