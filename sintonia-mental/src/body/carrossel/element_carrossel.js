import react from "react";
import './element_carrossel.css';
import imagem1 from '../../imagens/mente1.jpg';
import imagem2 from '../../imagens/mente2.jpg';
import imagem3 from '../../imagens/mente3.jpg';


function Element_carrossel(){
    
    return (
        <>
            <div id="carrosselExampleSlidesFade" className="carousel slide carousel-fade sty-carrossel mb-3" data-bs-ride="carousel" data-bs-interval="9000" data-bs-transition-duration="9">
                <div className="carousel-inner">
                    <div className="carousel-item active">
                        <div className ="sty-carrossel">
                            <img src={imagem1} className="d-block" alt="{alt}"/>
                            <div>
                                <h1>bemvindo</h1>
                            </div>
                        </div>
                    </div>
                    <div className="carousel-item">
                        <div className ="sty-carrossel">
                            <img src={imagem2} className="" alt=""/>
                            <div>
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


















