import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link as RouterLink } from "react-router-dom";
import { Jumbotron } from 'react-bootstrap';
import Button from '@material-ui/core/Button';
import Link from '@material-ui/core/Link';
import AllPeople from './AllPeople';
import CharCounts from './CharCounts';
import DuplicatePeople from './DuplicatePeople';
import EnterpriseReady from './EnterpriseReady';
import FavoriteBorderIcon from '@material-ui/icons/FavoriteBorder';
import './App.css';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lev1BtnVariant: window.location.pathname === "/" ? "contained" : "outlined",
      lev2BtnVariant: window.location.pathname === "/char-counts" ? "contained" : "outlined",
      lev3BtnVariant: window.location.pathname === "/duplicate-people" ? "contained" : "outlined",
      lev4BtnVariant: window.location.pathname === "/enterprise-ready" ? "contained" : "outlined",
    }
  }

  handleClick = (e) => {
    this.setState({
      lev1BtnVariant: e.currentTarget.id === "lev1Btn" ? "contained" : "outlined",
      lev2BtnVariant: e.currentTarget.id === "lev2Btn" ? "contained" : "outlined",
      lev3BtnVariant: e.currentTarget.id === "lev3Btn" ? "contained" : "outlined",
      lev4BtnVariant: e.currentTarget.id === "lev4Btn" ? "contained" : "outlined",
    });
  };


  render() {
    return (
      <div className="App" >
        <header className="App-header">
          <Jumbotron>
            Welcome to the Breslin SalesLoft Evaluation Project!<br />
            <Link href="https://github.com/tjbrez/breslin-salesloft-eval">View source code (https://github.com/tjbrez/breslin-salesloft-eval)</Link>
          </Jumbotron>
        </header>
        <Router>
          <div className="Nav-buttons">
            <RouterLink to="/">
              <Button id="lev1Btn" onClick={this.handleClick} variant={this.state.lev1BtnVariant} color="primary">Level 1: List All People</Button>
            </RouterLink>{' '}
            <RouterLink to="/char-counts">
              <Button id="lev2Btn" onClick={this.handleClick} variant={this.state.lev2BtnVariant} color="primary">Level 2: Character Counts</Button>
            </RouterLink>{' '}
            <RouterLink to="/duplicate-people">
              <Button id="lev3Btn" onClick={this.handleClick} variant={this.state.lev3BtnVariant} color="primary">Level 3: Duplicate People Records</Button>
            </RouterLink>{' '}
            <RouterLink to="/enterprise-ready">
              <Button id="lev4Btn" onClick={this.handleClick} variant={this.state.lev4BtnVariant} color="primary">Level 4: Enterprise Ready</Button>
            </RouterLink>
          </div>
          <div>
            <Switch>
              <Route exact path="/">
                <AllPeople />
              </Route>
              <Route path="/char-counts">
                <CharCounts />
              </Route>
              <Route path="/duplicate-people">
                <DuplicatePeople />
              </Route>
              <Route path="/enterprise-ready">
                <EnterpriseReady />
              </Route>
            </Switch>
          </div>
        </Router>
        <footer className="App-footer">
          Made with <FavoriteBorderIcon /> in Ohio
        </footer>
      </div>
    )
  }
}

export default App;
