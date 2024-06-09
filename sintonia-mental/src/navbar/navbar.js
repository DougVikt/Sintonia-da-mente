import React from "react";
import './navstyle.css';
import imagem from '../../src/imagens/logo3_semfundo.png';


const nav = document.querySelector('.fixed-top');
// funciona para ocultar o navbar
window.addEventListener('scroll', () => {
  if (window.scrollY > 200) { 
    nav.classList.add('hide-nav');// adiciona a classe
  } else {
    nav.classList.remove('hide-nav');// remove a classe
  }
});
function NavBar(){
  
    return (
    <>
        <nav className="navbar navbar-expand-md fixed-top m-0 p-0 sty-navbar">
          <button className="navbar-toggler ms-4" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
            <span className="navbar-toggler-icon"></span>
          </button>
            <div className="mb-0 mb-md-0 ms-4 ">
              <a className="navbar-brand" href="home">
                <img src={imagem} alt="logo sintonia mental" width="140" height="80"/>
              </a>
            </div>
            <div className="offcanvas offcanvas-start text-bg-dark " tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
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
              
            <div className="text-end me-5">
              <button type="button" className=" btiniciar">Iniciar</button>
            </div>
        </nav>
    </>
    )
}

export default NavBar;
