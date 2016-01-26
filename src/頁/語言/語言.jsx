import React from 'react'
import { Link } from 'react-router'
import Transmit from 'react-transmit'
import superagent from 'superagent-bluebird-promise'
import Debug from 'debug'

import {Navbar, ButtonToolbar, Button, Nav, NavItem, Grid, Col, Row } from 'react-bootstrap'
import '../../static/css/語言.css'

var debug = Debug('nativeDB:語言')

class 語言 extends React.Component {

  componentWillMount () { this.props.setQueryParams(this.props) }
  componentWillReceiveProps (nextProps) {
    if (nextProps.後端網址 === this.props.後端網址) return
    this.props.setQueryParams(nextProps)
  }

  constructor (props) {
    super(props)
    this.state = {}
  }

  handleSelect () {
  	console.log('sui2')
  }

  render () {
    var _json = ['妥妥語', '豬豬語']

    var allGigian = _json.map((v, i) => <NavItem eventKey={v} href={'/' + v}>{v}</NavItem>)

	var gigian = this.props.params.gigian

    return (
    <Grid>
	     <Navbar>
		    <Navbar.Header>
		      <Navbar.Brand>
		        <p>海外漢語方言資料庫   Database of Chinese languages in Singapore and Malaysia</p>
		      </Navbar.Brand>
		    </Navbar.Header>
	     </Navbar>
		<div className="bar-stripe"></div>
		<Nav bsStyle="tabs" activeKey={gigian} onSelect={this.handleSelect}>
			{allGigian}
		</Nav>
    </Grid>
    )
  }
}

export default Transmit.createContainer(語言, {
  queries: {}
})
