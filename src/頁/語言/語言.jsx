import React from 'react'
import { Link } from 'react-router'
import Transmit from 'react-transmit'
import superagent from 'superagent-bluebird-promise'
import Debug from 'debug'

import { Col, Row } from 'react-bootstrap'
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
  render () {
    var _json = ['妥妥語', '豬豬語']

    var _link = _json.map((v, i) => <a href='#' key={i}>{v}</a>)

	var _gigian = this.props.params.gigian

    return (
    <div>
    	<div class="bar-stripe"></div>
		{_gigian}
    </div>
    )
  }
}

export default Transmit.createContainer(語言, {
  queries: {}
})
