import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Col, Row, Form, Button } from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <p>Fake News Search Engine</p>
      </header>
      <Container fluid="md">
        <Row className="mx-0 search-box">
          <Col>
            {/* search box */}
            <Form>
              <Form.Group className="mb-3" controlId="searchWords">
                <Form.Label>What do you want to search for?</Form.Label>
                <Form.Control type="text" placeholder="Enter search words" />
                <Form.Text className="text-muted">
                  Try something like "USA Elections 2016".
                </Form.Text>
              </Form.Group>

              <Button variant="primary" type="submit">
                Search
              </Button>
            </Form>
          </Col>
        </Row>
        <Row className="mx-0">
          <Col xs={3} className="search-filters">
            {/* search filters */}
            <h2>Search Filters</h2>

            <Form>
              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Text"
              />
              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Title"
              />
              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Thread Title"
              />
              <Form.Check type="switch" id="custom-switch" label="Author" />
              <Form.Check
                type="switch"
                id="custom-switch"
                label="Website URL"
              />
              <Form.Check type="switch" id="custom-switch" label="Country" />
              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Language"
              />
              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Type"
              />
            </Form>
          </Col>
          <Col xs={9}>
            <Row>
              <h2>
                <b>Search Results</b>
              </h2>
              {/* Search results */}
            </Row>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
