import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link as RouterLink } from "react-router-dom";
import { Jumbotron } from 'react-bootstrap';
import Button from '@material-ui/core/Button';
import Link from '@material-ui/core/Link';
import AllPeople from './AllPeople';
import CharCounts from './CharCounts';
import DuplicatePeople from './DuplicatePeople';
import FavoriteBorderIcon from '@material-ui/icons/FavoriteBorder';
import './App.css';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      lev1BtnVariant: window.location.pathname === "/" ? "contained" : "outlined",
      lev2BtnVariant: window.location.pathname === "/char-counts" ? "contained" : "outlined",
      lev3BtnVariant: window.location.pathname === "/duplicate-people" ? "contained" : "outlined",
    }
  }

  handleClick = (e) => {
    this.setState({
      lev1BtnVariant: e.target.id === "lev1Btn" ? "contained" : "outlined",
      lev2BtnVariant: e.target.id === "lev2Btn" ? "contained" : "outlined",
      lev3BtnVariant: e.target.id === "lev3Btn" ? "contained" : "outlined",
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
            <RouterLink to="/" onClick={this.handleClick}>
              <Button id="lev1Btn" variant={this.state.lev1BtnVariant} color="primary">Level 1: List All People</Button>
            </RouterLink>{' '}
            <RouterLink to="/char-counts" onClick={this.handleClick}>
              <Button id="lev2Btn" variant={this.state.lev2BtnVariant} color="primary">Level 2: Character Counts</Button>
            </RouterLink>{' '}
            <RouterLink to="/duplicate-people" onClick={this.handleClick}>
              <Button id="lev3Btn" variant={this.state.lev3BtnVariant} color="primary">Level 3: Duplicate People Records</Button>
            </RouterLink>{' '}
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
        <footer className="App-footer">
          Made with <FavoriteBorderIcon /> in Ohio
        </footer>
      </div>
    )
  }
}

export default App;
