import React from 'react';
import MaterialTable from 'material-table';

class CharCounts extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      countsData: [],
      isLoading: true,
    }
  }

  componentDidMount() {
    console.log("fetching character counts...")
    fetch('/api/people/char-counts')
      .then(results => results.json())
      .then(data => {
        this.setState({ countsData: data, isLoading: false });
      }).catch(err => console.log(err))
  }

  render() {
    return (
      <div>
        <p className="Level-description">
          <strong>Level 2</strong>: Create a button that, when clicked, displays a frequency count of all the
          unique characters in all the email addresses of all the People you have access to, sorted by frequency count.
        </p>
        <div className="Custom-table">
          <MaterialTable
            columns={[
              { title: 'Character', field: 'character' },
              { title: 'Count', field: 'count' },
            ]}
            options={{
              search: false,
              paging: false,
            }}
            data={this.state.countsData}
            title="Character Frequency Count"
            isLoading={this.state.isLoading}
          />
        </div>
      </div>
    )
  };
}

export default CharCounts;
