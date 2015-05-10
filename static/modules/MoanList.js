import React from '../bower_components/react/react-with-addons.js';
import $ from '../bower_components/jquery/dist/jquery.js';

let MoanList = React.createClass({

  getInitialState() {
    return {
      moans: []
    };
  },

  componentWillMount() {
    $.get('/posts', null, response => {
      // let results = 
      this.setState({moans: response.results});
    });
  },

  render() {
    return (<div>{this.state.moans}</div>);
  }
});


export default MoanList;
