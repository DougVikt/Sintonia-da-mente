import react from "react";
import './element_carrossel.css';
import imagem1 from '../../imagens/mente1.jpg';
import imagem2 from '../../imagens/mente2.jpg';
import imagem3 from '../../imagens/mente3.jpg';

function ItemCarrossel(classe , imagem){
    return(
    <div className ={classe}>
        <img src={imagem} className="d-block" alt="..."/>
    </div>
);}
function Element_carrossel(){
    return (
        <>
            <div id="carrosselExampleSlidesOnly" className="carousel slide sty-carrossel mb-3" data-bs-ride="carousel">
                <div className="carousel-inner">
                    <div className="carousel-item active">
                        <ItemCarrossel classe="sty-carrossel" imagem={imagem1}/>
                    </div>
                    <div className="carousel-item">
                        <div className="sty-carrossel">
                            <img src={imagem2} className="d-block" alt="..."/>
                        </div>
                    </div>
                    <div className="carousel-item">
                        <div className="sty-carrossel">
                            <img src={imagem3} className="d-block" alt="..."/>
                        </div>
                    </div>
                </div>

            </div>
        </>
    )
}
export default Element_carrossel;


















