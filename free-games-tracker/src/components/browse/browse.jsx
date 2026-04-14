import "./styles.css"
import { SiEpicgames } from "react-icons/si"
import { FaSteam } from "react-icons/fa"
import { FaPlaystation } from "react-icons/fa"
import { FaXbox } from "react-icons/fa"
import { SiGogdotcom } from "react-icons/si"
import { SiPrime } from "react-icons/si";
//import testData from "../../resources/test.json"
//import emptyData from "../../resources/empty.json"
import data from "../../resources/data.json"



export default function Browse() {
    return (
        <>
            <div id="free-games-cnt">
                <div id="free-games">
                    <div className="market">
                        <a className="market-name" href="https://store.epicgames.com/en-US" target="_blank" rel="noopener noreferrer">
                            <SiEpicgames size="2rem" />
                            <h2>Epic Games</h2>
                        </a>

                        <div className="games">
                            {data.filter(game => game.market === "epic_games").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <a className="market-name" href="https://store.steampowered.com/" target="_blank" rel="noopener noreferrer">
                            <FaSteam size="2rem" />
                            <h2>Steam</h2>
                        </a>

                        <div className="games">
                            {data.filter(game => game.market === "steam").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <a className="market-name" href="https://www.gog.com/" target="_blank" rel="noopener noreferrer">
                            <SiGogdotcom size="2rem" />
                            <h2 className="market-text">GOG Games</h2>
                        </a>

                        <div className="games">
                            {data.filter(game => game.market === "gog").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <a className="market-name" href="https://store.playstation.com/en-us/view/25d9b52a-7dcf-11ea-acb6-06293b18fe04/bc428b4a-f1b7-11ea-aadc-062143ad1e8d" target="_blank" rel="noopener noreferrer">
                            <FaPlaystation size="2rem" />
                            <h2 className="market-text">PlayStation Plus</h2>
                        </a>

                        <div className="games">
                            {data.filter(game => game.market === "playstation").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>

                    <div className="market">
                        <a className="market-name" href="https://gaming.amazon.com/home" target="_blank" rel="noopener noreferrer">
                            <SiPrime size="2rem" />
                            <h2>Amazon Prime Gaming</h2>
                        </a>

                        <div className="games">
                            {data.filter(game => game.market === "amazon").map((game, i) =>
                                <a key={i} href={game.link} target="_blank" rel="noopener noreferrer" className="game">
                                    <img className="game-img" alt="game--img" src={game.img} />
                                    <h3 className="game-title-text">{game.title}</h3>
                                </a>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
