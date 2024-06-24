import react from "react";
import './element_carrossel.css';
import imagem1 from '../../imagens/mente1.jpg';
import imagem2 from '../../imagens/mente2.jpg';
import imagem3 from '../../imagens/mente3.jpg';


function Element_carrossel(){
    
    return (
        <>
        <div id="carrosselExampleSlidesFade" className="carousel slide carousel-fade sty-carrossel mb-3" data-bs-ride="carousel" data-bs-interval="9000" data-bs-transition-duration="9">
          <div className="carousel-inner d-flex">
            <div className="carousel-item active ">
              <div className="card row h-100 d-flex">
                <div className="col-6 w-50 " >
                    <img src={imagem1} alt="{alt}" className="img-fluid" />
                  </div>
                  <div className="col-6 flex-grow-1">
                    <div className="card-body w-50 ">
                      <h1>bemvindo</h1>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    )
}
export default Element_carrossel;


















