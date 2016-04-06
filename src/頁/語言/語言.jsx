import React from 'react'
import { Link } from 'react-router'
import Transmit from 'react-transmit'
import superagent from 'superagent-bluebird-promise'
import Debug from 'debug'

import { ButtonToolbar, Button, 
    Navbar, Nav, NavItem, 
    Grid, Col, Row, 
    ListGroup, ListGroupItem, Badge } from 'react-bootstrap'

import { LinkContainer } from 'react-router-bootstrap'


import '../../static/css/語言.css'

var debug = Debug('nativeDB:語言')

class 語言 extends React.Component 
{
    //
    // mock
    //
    state = {
      lang:  ['妥妥語', '豬豬語'],
      word: [{'name': '單詞', 
                    'count': 20,
                    'list': ['妥', '豬']
                  },{'name': '雙詞', 
                    'count': 2,
                    'list': ['妥妥', '豬豬']
                  },{
                    'name': '故事', 
                    'count': 1,
                    'list': ['sui2 sui2 sui2']
                  }]
    };

  componentWillMount () { this.props.setQueryParams(this.props) }
  componentWillReceiveProps (nextProps) {
    if (nextProps.後端網址 === this.props.後端網址) return
    this.props.setQueryParams(nextProps)
  }

  constructor (props) {
    super(props)
  }

  renderGigianNav () {
    let gigian = this.props.params.gigian;
    let allGigian = this.state.lang.map((v, i) => <LinkContainer to={'/' + v} key={v}><NavItem eventKey={v} key={v} >{v}</NavItem></LinkContainer>);
    
    return (
        <Nav bsStyle="tabs" activeKey={gigian}>
        {allGigian}
        </Nav>
      )
  }

  renderSuShing () {
    let allSuShing = this.state.word.map((v, i) => <ListGroupItem key={v.name}  href={'#' + v.name}>{v.name} <Badge>{v.count}</Badge></ListGroupItem>);
    return (
        <ListGroup>
          {allSuShing}
        </ListGroup>
      )
  }

  renderJi () {
    let arr = [];
    this.state.word.forEach(v => {
      let list = v.list.map(word => <li>{word}</li>);
      let sushingBlock = <li><ol>list</ol></li>;
    })
    return (
        <ul style={{listStyleType:"none"}}>
        {}
        </ul>
      )
  }

  render () {
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

		{this.renderGigianNav()}
        <br/>
        <br/>

        <Row>
          <Col xs={3}>
             {this.renderSuShing()}
          </Col>

          <Col xs={9}>
            {this.renderJi()}
          </Col>
        </Row>
    </Grid>
    )
  }
}

export default Transmit.createContainer(語言, {
  queries: {}
})
