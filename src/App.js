import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Jumbotron, Button } from 'react-bootstrap';
import AllPeople from './AllPeople';
import CharCounts from './CharCounts';
import DuplicatePeople from './DuplicatePeople';
import './App.css';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lev1BtnVariant: window.location.pathname === "/" ? "primary" : "outline-primary",
      lev2BtnVariant: window.location.pathname === "/char-counts" ? "primary" : "outline-primary",
      lev3BtnVariant: window.location.pathname === "/duplicate-people" ? "primary" : "outline-primary",
    }
  }

  handleClick = (e) => {
    this.setState({
      lev1BtnVariant: e.target.id === "lev1Btn" ? "primary" : "outline-primary",
      lev2BtnVariant: e.target.id === "lev2Btn" ? "primary" : "outline-primary",
      lev3BtnVariant: e.target.id === "lev3Btn" ? "primary" : "outline-primary",
    });
  };


  render() {
    return (
      <div className="App" >
        <header className="App-header">
          <Jumbotron>
            Welcome to the Breslin SalesLoft Evalution Project!<br />
            <a href="https://github.com/tjbrez/breslin-salesloft-eval">View source code (https://github.com/tjbrez/breslin-salesloft-eval)</a>
          </Jumbotron>
        </header>
        <Router>
          <div className="Nav-buttons">
            <Link to="/" onClick={this.handleClick}>
              <Button id="lev1Btn" variant={this.state.lev1BtnVariant}>Level 1: List All People</Button>
            </Link>{' '}
            <Link to="/char-counts" onClick={this.handleClick}>
              <Button id="lev2Btn" variant={this.state.lev2BtnVariant}>Level 2: Character Counts</Button>
            </Link>{' '}
            <Link to="/duplicate-people" onClick={this.handleClick}>
              <Button id="lev3Btn" variant={this.state.lev3BtnVariant}>Level 3: Duplicate People Records</Button>
            </Link>{' '}
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
            </Switch>
          </div>
        </Router>
      </div>
    )
  }
}

export default App;
