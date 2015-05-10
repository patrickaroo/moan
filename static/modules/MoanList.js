import React from '../bower_components/react/react-with-addons.js';
import _ from '../bower_components/underscore/underscore.js'
import $ from '../bower_components/jquery/dist/jquery.js';

let MoanItem = React.createClass({
  propTypes: {
    moan: React.PropTypes.object,
  },

  render() {
    return (<div>
      Moan {this.props.moan.id}: {this.props.moan.text} 
    </div>);
  }
});

let MoanList = React.createClass({

  getInitialState() {
    return {
      moans: []
    };
  },

  componentWillMount() {
    $.get('/posts', null, response => {
      this.setState({moans: response.results});
    });
  },

  render() {
    return (
      <div>
        {_(this.state.moans).map(moan => 
          <MoanItem moan={moan} />)}
      </div>
    );
  }
});


export default MoanList;
