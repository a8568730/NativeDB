import React from 'react'
import { Link } from 'react-router'
import Transmit from 'react-transmit'
import superagent from 'superagent-bluebird-promise'
import Debug from 'debug'

import {Navbar, ButtonToolbar, Button, Nav, NavItem, Grid, Col, Row, ListGroup, ListGroupItem } from 'react-bootstrap'
import '../../static/css/語言.css'

var debug = Debug('nativeDB:語言')

class 語言 extends React.Component 
{
    //
    // mock
    //
    state = {
      lang:  ['妥妥語', '豬豬語'],
      word: ['單詞','雙詞','故事']
    };

  componentWillMount () { this.props.setQueryParams(this.props) }
  componentWillReceiveProps (nextProps) {
    if (nextProps.後端網址 === this.props.後端網址) return
    this.props.setQueryParams(nextProps)
  }

  constructor (props) {
    super(props)
  }

  render () {
    var allGigian = this.state.lang.map((v, i) => <NavItem eventKey={v} key={v}  href={'/' + v}>{v}</NavItem>);
    var allSuShing = this.state.word.map((v, i) => <ListGroupItem key={v}  href={'#' + v}>{v}</ListGroupItem>);

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
		<Nav bsStyle="tabs" activeKey={gigian}>
			{allGigian}
		</Nav>

        <br/>
        <br/>

        <Row>
          <Col xs={3}>
             <ListGroup>
             {allSuShing}
            </ListGroup>
          </Col>

          <Col xs={9}>
            <ul style={{listStyleType:"none"}}>
            </ul>
          </Col>
        </Row>
    </Grid>
    )
  }
}

export default Transmit.createContainer(語言, {
  queries: {}
})
