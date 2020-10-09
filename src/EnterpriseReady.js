import React from 'react';
import PiedPiperMiddleOutImg from './pied_piper_middle_out.jpg';

class EnterpriseReady extends React.Component {

  render() {
    return (
      <div>
        <p className="Level-description">
          <strong>Level 4</strong>: Build a scalable enterprise-ready underlying architecture for this
          application that would scale to handle the function in Level 2 and 3 for trillions and
          trillions of records while returning results in a reasonable amount of time.
        </p>
        <div>
          <h4>Coming Soon!</h4>
          <img className="Custom-img" src={PiedPiperMiddleOutImg} alt="middle out compression" width="50%" />
        </div>
      </div>
    )
  };
}

export default EnterpriseReady;
