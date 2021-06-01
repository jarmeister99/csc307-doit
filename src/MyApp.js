import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navigation from "./components/Navigation"
import Footer from "./components/Footer"
import Home from "./components/Home"
import Login from "./components/Login"
import Register from "./components/Register"
import EditTask from "./components/EditTask"
import Tasks from "./components/Tasks"
import AddTask from "./components/AddTask"
import MonthView from "./components/MonthView"


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
          <Route path="/addtask" exact component={() => <AddTask />} />
          <Route path="/monthview" exact component={() => <MonthView />} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default MyApp;
