import React, { useState , useLayoutEffect} from "react";
import './navstyle.css';
import imagem from '../../src/imagens/sm2.svg';




function NavBar(){
    const [nav, setNav] = useState(null);
    let scroll = 0;
  // useLayoutEffect é executado a função após o componente ter sido renderizado
    useLayoutEffect(() => {
      // Obter o elemento nav pelo ID
      const navElement = document.getElementById('nav');
      setNav(navElement);
    }, []);
  
    useLayoutEffect(() => {
      if (nav) {
        window.addEventListener('scroll', () => {
          // Obter a posição da barra de rolagem
          const scrollTop = window.scrollY;
          if (scrollTop > scroll) {
            // Rolar para baixo
            nav.style.top = '-100px';
          } else {
            // Rolar para cima
            nav.style.top = '0px';
          }
          if (scrollTop === 0) {
            nav.style.opacity = "100%" 
          }
          else{
            nav.style.opacity = "70%"
          }
         scroll = scrollTop;
        });
      }
    }, [nav]);
  
    return (
    <>
        <nav id="nav" className="navbar navbar-expand-md fixed-top m-0  p-1 sty-navbar">
          <button className="navbar-toggler ms-4 bg-secondary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
            <span className="navbar-toggler-icon"></span>
          </button>
            <div className="mb-0 mb-md-0  sty-image">
              <a className="navbar-brand" href="index.html">
                <img className="img-fluid" src={imagem} alt="logo sintonia mental" width="90" height="90"/>
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
                      <a href="#iniciar" className="nav-link sty-link-nav px-5">Iniciar</a>
                    </li>
                    <li className="nav-item">
                      <a href="#depoimentos" className="nav-link sty-link-nav px-5">Depoimentos</a>
                    </li>
                    <li className="nav-item">
                      <a href="#sobre" className="nav-link sty-link-nav px-5">Sobre</a>
                      </li>
                  </ul>
              </div>
            </div>
              
            <div className="text-end me-5">
              <button type="button" className=" btiniciar" href="#iniciar">Iniciar</button>
            </div>
        </nav>
    </>
    )
}

export default NavBar;
