import React, { Component } from "react";
import Dashboard from "./Dashboard";

import {
  BrowserRouter as Router,
  Route,
  Switch,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p>ANASAYFAYA HOŞGELDİN İBİNE ANAN</p>
          </Route>
          <Route path="/accounts/profile/" component={Dashboard} />
          
        </Switch>
      </Router>
    );
  }
}
