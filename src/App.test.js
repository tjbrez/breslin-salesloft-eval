import React from 'react';
import { render, screen, cleanup } from '@testing-library/react';
import userEvent from '@testing-library/user-event'
import App from './App';
import { Router } from 'react-router-dom';
import { createMemoryHistory } from 'history'

afterEach(() => {
  cleanup;
});

jest.mock("./AllPeople", () => {
  return function DummyAllPeople(props) {
    return (
      <div data-testid="AllPeople">AllPeople is loaded</div>
    );
  };
});

jest.mock("./CharCounts", () => {
  return function DummyCharCounts(props) {
    return (
      <div data-testid="CharCounts">CharCounts is loaded</div>
    );
  };
});

jest.mock("./DuplicatePeople", () => {
  return function DummyDuplicatePeople(props) {
    return (
      <div data-testid="DuplicatePeople">DuplicatePeople is loaded</div>
    );
  };
});

jest.mock("./EnterpriseReady", () => {
  return function DummyEnterpriseReadyprops(props) {
    return (
      <div data-testid="EnterpriseReady">EnterpriseReady is loaded</div>
    );
  };
});

test('default renders app with AllPeople component', () => {
  const { getByText } = render(<App />);
  expect(getByText(/Welcome to the Breslin SalesLoft Evaluation Project!/i)).toBeInTheDocument();
  expect(screen.queryByText(/AllPeople is loaded/i)).toBeInTheDocument()
  expect(screen.queryByText(/CharCounts is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/DuplicatePeople is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/EnterpriseReady is loaded/i)).not.toBeInTheDocument()
});

test('char counts Link loads CharCounts component', () => {
  const history = createMemoryHistory()
  render(
    <Router history={history}>
      <App />
    </Router>
  );

  const leftClick = { button: 0 }
  userEvent.click(screen.getByText(/Level 2: Character Counts/i), leftClick)

  expect(screen.queryByText(/AllPeople is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/CharCounts is loaded/i)).toBeInTheDocument()
  expect(screen.queryByText(/DuplicatePeople is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/EnterpriseReady is loaded/i)).not.toBeInTheDocument()

});

test('duplicates Link loads DuplicatePeople component', () => {
  const history = createMemoryHistory()
  render(
    <Router history={history}>
      <App />
    </Router>
  );

  const leftClick = { button: 0 }
  userEvent.click(screen.getByText(/Level 3: Duplicate People Records/i), leftClick)

  expect(screen.queryByText(/AllPeople is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/CharCounts is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/DuplicatePeople is loaded/i)).toBeInTheDocument()
  expect(screen.queryByText(/EnterpriseReady is loaded/i)).not.toBeInTheDocument()

});


test('enterprise ready Link loads EnterpriseReady component', () => {
  const history = createMemoryHistory()
  render(
    <Router history={history}>
      <App />
    </Router>
  );

  const leftClick = { button: 0 }
  userEvent.click(screen.getByText(/Level 4: Enterprise Ready/i), leftClick)

  expect(screen.queryByText(/AllPeople is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/CharCounts is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/DuplicatePeople is loaded/i)).not.toBeInTheDocument()
  expect(screen.queryByText(/EnterpriseReady is loaded/i)).toBeInTheDocument()

});
