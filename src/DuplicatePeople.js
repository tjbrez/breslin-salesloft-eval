import React from 'react';
import MaterialTable from 'material-table';

class DuplicatePeople extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      duplicatesData: [],
      isLoading: true,
    }
  }

  componentDidMount() {
    console.log("fetching duplicate people...")
    fetch('/api/people/duplicates')
      .then(results => results.json())
      .then(data => {
        this.setState({ duplicatesData: data, isLoading: false });
      }).catch(err => console.log(err))
  }

  render() {
    return (
      <div>
        <p className="Level-description">
          <strong>Level 3</strong>: Create a button that would show us a list of suggested possible duplicate People.
        </p>
        <div className="Custom-table">
          <MaterialTable
            columns={[
              { title: 'Person 1 Id', field: 'person1_id' },
              { title: 'Person 1 Name', field: 'person1_name' },
              { title: 'Person 1 Email', field: 'person1_email' },
              { title: 'Person 2 Id', field: 'person2_id' },
              { title: 'Person 2 Name', field: 'person2_name' },
              { title: 'Person 2 Email', field: 'person2_email' },
            ]}
            options={{
              search: false,
              paging: false,
            }}
            data={this.state.duplicatesData}
            title="Possible Duplicate People Records"
            isLoading={this.state.isLoading}
          />
        </div>
      </div>
    )
  };
}

export default DuplicatePeople;
