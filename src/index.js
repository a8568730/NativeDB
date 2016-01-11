import React from 'react'
import { render } from 'react-dom'
import Router, { Route, IndexRoute } from 'react-router'
import App from './App/App'
import 首頁 from './頁/首頁/首頁'
import createBrowserHistory from 'history/lib/createBrowserHistory'
import './app.css'

import Debug from 'debug'
Debug.enable('ing7:*')

const root = document.getElementById('app')

// if (window.location.pathname === '/') {
// render(<HuanGing/>, root)
// } else {
let history = createBrowserHistory()
render(
  <Router history={history}>
      <Route path='/' component={首頁}>
        <IndexRoute component={首頁}/>
        <Route path='講(/:khiunn/:ku)' component={首頁}/>
      </Route>
    </Router>, root)
  // }
