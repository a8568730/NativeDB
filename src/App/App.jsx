import React from 'react'
import Transmit from 'react-transmit'
import Router from 'react-router'
import { Col, Row } from 'react-bootstrap'

class App extends React.Component {

  constructor () {
    super()
  }

  render () {
    return (
    <div>
          {React.cloneElement(this.props.children,
        {
        }
      )}
          <Row className='footer'>
          <Col md={12} >
            <p>copyright&copy;學姊</p>
            <p>all the records preserved by the owner</p>
          </Col>
        </Row>
        </div>
    )
  }
}

export default Transmit.createContainer(App, { queries: {} })
