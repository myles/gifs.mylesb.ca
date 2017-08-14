import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import App from './App';
import List from './views/List';
import Detail from './views/Detail';

import './index.css';

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route exact path='/' component={List} />
      <Route path='/:slug' component={Detail} />
      <Route component={List} />
    </Switch>
  </BrowserRouter>,

  document.getElementById('root')
);
