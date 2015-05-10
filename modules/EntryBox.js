import React from '../bower_components/react/react-with-addons.js';

let EntryBox = React.createClass({

  statics: {
    isHaiku(text) {
    },

    isLong(text) {
      return text.split(" ").length > 140;
    }
  },

  getInitialState() {
    return {
      value: "Only haikus and 140 words +",
      canSubmit: false
    }
  },

  handleChange(event) {
    let newValue = event.target.value;
    this.setState({
      value: newValue,
      canSubmit: EntryBox.isLong(newValue) || EntryBox.isHaiku(newValue)
    });
  },

  doSomething() {
    console.log("Hello world");
  },

  render() { 
    return (
      <div>
        <div>
          <textarea type="text" value={this.state.value} onChange={this.handleChange} />
        </div>

        <button type="button" disabled={!this.state.canSubmit}>Moooaaaaannnn</button>
      </div>
    );
  }

})

export default EntryBox;
