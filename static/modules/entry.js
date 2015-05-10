import EntryBox from './EntryBox.js';
import MoanList from './MoanList.js';
import React from '../bower_components/react/react.js';
import $ from '../bower_components/jquery/dist/jquery.js';

let App = React.createClass({
  render() {
    return (
      <div>
        <MoanList />
        <EntryBox />
      </div>
    );
  }
})

$(document).ready(() => React.render(<App />, document.body))
