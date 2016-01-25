import React from 'react'
import { Link } from 'react-router'
import Transmit from 'react-transmit'
import superagent from 'superagent-bluebird-promise'
import Debug from 'debug'

import { Jumbotron, Grid, Col, Row } from 'react-bootstrap'
import '../../static/css/首頁.css'

var debug = Debug('nativeDB:首頁')

class 首頁 extends React.Component {

  componentWillMount () { this.props.setQueryParams(this.props) }
  componentWillReceiveProps (nextProps) {
    if (nextProps.後端網址 === this.props.後端網址) return
    this.props.setQueryParams(nextProps)
  }

  constructor (props) {
    super(props)
    this.state = {}
  }
  render () {
    var _json = ['妥妥語', '豬豬語']

    var _link = _json.map((v, i) => <a href={'/' + v} key={i}>{v}</a>)

    return (
         <Jumbotron>

          <Grid className='container'>
            <Row className='headtitle'>
              <h2>海外漢語方言資料庫&nbsp;&nbsp;<small>Database of Chinese languages in Singapore and Malaysia</small></h2>
            </Row>

            <Row ng-controller='LangController' id='lang'>
              <div>
                {_link}
              </div>
            </Row>
            </Grid>
        </Jumbotron>
    )
  }
}

export default Transmit.createContainer(首頁, {
  queries: {}
})
