import React from "react";
import './navstyle.css';
import imagem from '../../src/imagens/logo3_semfundo.png';


function NavBar(){
  
    return (
    <>
        <nav className="navbar navbar-expand-md fixed-top m-0 p-0 sty-navbar">
          <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
            <span className="navbar-toggler-icon"></span>
          </button>
            <div className="mb-0 mb-md-0 ms-5 ">
              <a className="navbar-brand" href="home">
                <img src={imagem} alt="logo sintonia mental" width="80" height="80"/>
              </a>
            </div>
            <div className="offcanvas offcanvas-start text-bg-dark py-3" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
              <div className="offcanvas-header">
                <h5 className="offcanvas-title" id="offcanvasDarkNavbarLabel">MENU</h5>
                <button type="button" className="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div className="offcanvas-body px-0">
                  <ul className="navbar-nav  mx-auto">
                    <li className="nav-item">
                      <a href="#" className="nav-link sty-link-nav px-5">Iniciar</a>
                    </li>
                    <li className="nav-item">
                      <a href="#" className="nav-link sty-link-nav px-5">Depoimentos</a>
                    </li>
                    <li className="nav-item">
                      <a href="#" className="nav-link sty-link-nav px-5">Sobre</a>
                      </li>
                  </ul>
              </div>
            </div>
              
            <div className="d-flex justify-content-end ms-auto text-end">
              <button type="button" className="me-5 btiniciar">Iniciar</button>
            </div>
        </nav>
    </>
    )
}

export default NavBar;
