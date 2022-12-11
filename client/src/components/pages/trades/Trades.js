import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

// Bootstrap imports
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'

import { getToken } from '../../../helpers/auth'


const Trades = () => {

  // ! State
  const [ trades, setTrades ] = useState([])
  const [ errors, setErrors ] = useState(null)

  // ! Executions
  useEffect(() => {
    const getData = async () => {
      try {
        const { data } = await axios.get('/api/trades', {
          headers: {
            Authorization: `Bearer ${getToken()}`,
          },
        })
        console.log(data)
        setTrades(data)
      } catch (err) {
        console.log(err)
        setErrors(err.response.data)
      }
    }
    getData()
  }, [])



  return (
    <div className="home-page">
      <Container className="trades-metrics-container mt-1"></Container>
      <Container className="trades-filter-container mt-2"></Container>
      <Container className="trades-title-container mt-1">
        <Row>
          <Col>status</Col>
          <Col>open date</Col>
          <Col>Symbol</Col>
          <Col>Side</Col>
          <Col>Return $</Col>
          <Col>Return %</Col>
          <Col>Setup</Col>
        </Row>
      </Container>
      <Container className="trades-list-container mt-1">
        {trades ?
          trades.map(trade => {
            const { id, symbol, side, setup } = trade
            return (
              <Row key={id}>
                <Col>status</Col>
                <Col>Date Open</Col>
                <Col>{symbol}</Col>
                <Col>{side}</Col>
                <Col>Return $</Col>
                <Col>Return %</Col>
                <Col>{setup}</Col>
              </Row>
            )
          })
          :
          errors ? <h2>Something went wrong! Please try again later!</h2> : <h2>Loading</h2>
        }
      </Container>
    </div>
  )
}

export default Trades