import React from '../bower_components/react/react-with-addons.js';
import _ from '../bower_components/underscore/underscore.js'
import $ from '../bower_components/jquery/dist/jquery.js';

let EntryBox = React.createClass({

  statics: {
    // from http://stackoverflow.com/questions/5686483/how-to-compute-number-of-syllables-in-a-word-in-javascript
    syllableCount(word) {
      if(!word) {return 0;}
      word = word.toLowerCase();                                     //word.downcase!
      if(!word || word.length <= 3) { return 1; }                             //return 1 if word.length <= 3
      word = word.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, '');   //word.sub!(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, '')
      word = word.replace(/^y/, '');                                 //word.sub!(/^y/, '')
      return word.match(/[aeiouy]{1,2}/g).length;                    //word.scan(/[aeiouy]{1,2}/).size
    },
    
    // http://grammar.yourdictionary.com/style-and-usage/rules-for-writing-haiku.html
    isHaiku(text) {
      let lines = text.split(/\n/);

      let lineCounts = _(lines).map(line => {
        return _(line.split(' '))
          .chain()
          .map(this.syllableCount)
          .reduce((sum, count) => sum + count, 0)
          .value()
      });

      if (lineCounts && lineCounts.length < 3)
        return false;

      return (lineCounts[0] === 5 && lineCounts[1] === 7 && lineCounts[2] === 5);
    },

    isLong(text) {
      return text.split(' ').length > 140;
    }
  },

  getInitialState() {
    return {
      value: 'Only haikus and 140 words +',
      canSubmit: false,
      submitted: false
    }
  },

  handleChange(event) {
    let newValue = event.target.value;
    this.setState({
      value: newValue,
      canSubmit: EntryBox.isLong(newValue) || EntryBox.isHaiku(newValue)
    });
  },

  submitMoan(e) {
    let data = {
      user: "anonymous",
      text: this.state.value
    };
    $.ajax({
        type: "POST",
        url: "/post/",
        processData: false,
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: () => this.setState({'submitted': true})});
  },

  render() { 
    return (
      <div>
        <div>
          <textarea type="text" value={this.state.value} onChange={this.handleChange} />
        </div>
        <div onClick={this.submitMoan} style={{"display": this.state.canSubmit ? "block" : "none"}}>Moan</div>
        {this.state.submitted ? 'Submitted' : null}
      </div>
    );
  }

})

export default EntryBox;
