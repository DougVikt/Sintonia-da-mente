import react from "react";
import './element_carrossel.css';
import imagem1 from '../../imagens/mente1.jpg';
import imagem2 from '../../imagens/mente2.jpg';
import imagem3 from '../../imagens/mente3.jpg';


function Element_carrossel(){
    
    return (
        <>
        <div id="carrosselExampleSlidesFade" className="carousel slide carousel-fade sty-carrossel mb-3" data-bs-ride="carousel" data-bs-interval="9000" data-bs-transition-duration="9">
          <div className="carousel-inner d-flex flex-row container p-0 m-0">
            <div className="carousel-item active w-100">
              <div className="row p-0 ">
                <div className="col-sm-6 " >
                  <img src={imagem1} alt="{alt}" className="img-fluid w-100 " />
                </div>
                <div className="col-sm-6 ">
                  <h1>bemvindo</h1>
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    )
}
export default Element_carrossel;


















