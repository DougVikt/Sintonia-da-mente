import react from "react";
import './element_carrossel.css';
import imagem1 from '../../imagens/mente1.jpg';
import imagem2 from '../../imagens/mente2.jpg';
import imagem3 from '../../imagens/mente3.jpg';


function Element_carrossel(){
    
    return (
        <>
        <div id="carrosselExampleSlidesFade" className="carousel slide carousel-fade sty-carrossel mt-3" data-bs-ride="carousel" data-bs-interval="9000" data-bs-transition-duration="9">
          <div className="carousel-inner p-0 m-0">
            <div className="carousel-item active sty-carrossel-item">
              <div className="row">
                <div className="col-sm-6 sty-div-image" >
                  <img src={imagem2} alt="{alt}" className="img-fluid w-100 sty-img" />
                </div>
                <div className="col-sm-6 p-5 text-start">
                  <h1 className="pt-5 sty-h1">bemvindo</h1>
                  <p className="sty-p">exp0licando</p>
                  <button className="sty-button btn ">saiba mais</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    )
}
export default Element_carrossel;


















