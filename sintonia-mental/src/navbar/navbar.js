import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Navbar} from 'react-bootstrap';


function NavBar(){
    return (
    <Navbar>
        <Container>
            <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
            <div className="col-md-3 mb-2 mb-md-0">
                <a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="d-inline-flex link-body-emphasis text-decoration-none">
                    
                </a>
            </div>
                <ul className="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
                    <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2 link-secondary">Lar</a></li>
                    <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2">Características</a></li>
                    <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2">Preços</a></li>
                    <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2">Perguntas frequentes</a></li>
                    <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2">Sobre</a></li>
     
                </ul>

                <div className="col-md-3 text-end">
                    <button type="button" className="btn btn-outline-primary me-2">Conecte-se</button>
                    <button type="button" className="btn btn-primary">Inscrever-se</button>
                </div>
            </header>
        </Container>
    </Navbar>
    )
}

export default NavBar;
/*
<div className="container">
    <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
      <div className="col-md-3 mb-2 mb-md-0">
        <a href="/" className="d-inline-flex link-body-emphasis text-decoration-none">
          <svg className="bi" width="40" height="32" role="img" aria-label="Inicialização"><use xlink:href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=falsebootstrap"></use></svg>
        </a>
      </div>

      <ul className="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
        <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2 link-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Lar</font></font></a></li>
        <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Características</font></font></a></li>
        <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Preços</font></font></a></li>
        <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Perguntas frequentes</font></font></a></li>
        <li><a href="https://musical-dollop-rqgx7qj6wv7h947.github.dev/?autoStart=false" className="nav-link px-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sobre</font></font></a></li>
      </ul>

      <div className="col-md-3 text-end">
        <button type="button" className="btn btn-outline-primary me-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Conecte-se</font></font></button>
        <button type="button" className="btn btn-primary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Inscrever-se</font></font></button>
      </div>
    </header>
  </div>
*/