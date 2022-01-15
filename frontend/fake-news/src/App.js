import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Col, Row, Form, Button } from "react-bootstrap";

// function FilterSelection(){

// }

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
                // onChange={this.FilterSelection(1)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Title"
                // onChange={this.FilterSelection(2)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Thread Title"
                // onChange={this.FilterSelection(3)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Author"
                // onChange={this.FilterSelection(4)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Website URL"
                // onChange={this.FilterSelection(5)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Country"
                // onChange={this.FilterSelection(6)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Language"
                // onChange={this.FilterSelection(7)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>

              <Form.Check
                type="switch"
                id="custom-switch"
                label="Article Type"
                // onChange={this.FilterSelection(8)}
              />
              <>
                <Form.Label className="weight-range-label">
                  Field Weight
                </Form.Label>
                <Form.Range disabled />
              </>
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
