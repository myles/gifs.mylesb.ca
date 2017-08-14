import React from 'react';
import { Link } from 'react-router-dom'

import { css } from 'glamor';

let AppStyle = css({
  margin: 0
});

let AppHeaderStyle = css({
  textAlign: 'center'
});

let AppHeaderTitleStyle = css({
  fontSize: '2em'
});

let AppHeaderLinkStyle = css({
  textDecoration: 'none',
  color: 'blue',
  ':hover': {
    textDecoration: 'underline',
    color: 'red'
  }
})

class App extends React.Component {
  render() {
    return (
      <div className={AppStyle}>
        <div className={AppHeaderStyle}>
          <h1 className={AppHeaderTitleStyle}>
            <Link to='/' className={AppHeaderLinkStyle}>
              Myles' Gifs
            </Link>
          </h1>
        </div>

        <div className="App-body">
          {this.props.children}
        </div>

        <div className="App-footer">
          <p>Made by <a href="https://mylesb.ca/">Myles Braithwaite</a> with &heart; in Toronto.</p>
        </div>
      </div>
    );
  }
}

export default App;
