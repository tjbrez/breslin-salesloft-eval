import React from 'react';
import MaterialTable from 'material-table';

class AllPeople extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      peopleData: [],
      isLoading: true,
    }
  }

  componentDidMount() {
    console.log("fetching people...")
    fetch('/api/people')
      .then(results => results.json())
      .then(data => {
        this.setState({ peopleData: data, isLoading: false });
      }).catch(err => console.log(err))
  }

  render() {
    return (
      <div>
        <p className="Level-description">
          <strong>Level 1</strong>: Show a list of People records that are available via the API.  Display each Person’s name, email address, and job title.
        </p>
        <div className="Custom-table">
          <MaterialTable
            columns={[
              { title: 'Name', field: 'display_name' },
              { title: 'Email', field: 'email_address' },
              { title: 'Job Title', field: 'title' },
            ]}
            options={{
              search: true,
              pageSize: 10,
            }}
            data={this.state.peopleData}
            title="All People"
            isLoading={this.state.isLoading}
          />
        </div>
      </div>
    )
  };
}

export default AllPeople;
