import React from "react";
import './navstyle.css';

function NavBar(){
    return (
    <>
        <nav className="navbar navbar-expand-lg fixed-top m-3 p-1">
          <button className="navbar-toggler" type="button" data-toggle="collapse"  data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
            <div className="d-flex mb-2 mb-md-0 ms-5">
              <a className="navbar-brand" href="#">
                <img src="" alt="Bootstrap" width="30" height="24"/>
              </a>
            </div>
            <div className="navbar-collapse collapse">
                <ul className="navbar-nav me-auto">
                  <li className="nav-item"><a href="#" className="nav-link link-secondary">Lar</a></li>
                  <li className="nav-item"><a href="#" className="nav-link">Características</a></li>
                  <li className="nav-item"><a href="#" className="nav-link">Preços</a></li>
                  <li className="nav-item"><a href="#" className="nav-link">Perguntas frequentes</a></li>
                  <li className="nav-item"><a href="#" className="nav-link">Sobre</a></li>
                </ul>
              </div>
            <div className="d-flex justify-content-end ms-auto text-end">
              <button type="button" className="me-5 btiniciar">Iniciar</button>
            </div>
        </nav>
    </>
    )
}

export default NavBar;
