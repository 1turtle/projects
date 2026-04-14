import "./styles.css"
import { IoGameControllerOutline, IoSettingsOutline } from "react-icons/io5";
import { LuHistory } from "react-icons/lu";



export default function Navbar() {
    return (
        <>
            <nav id="top-navbar-cnt">
                <ul id="top-navbar">
                    <div id="top-navbar-title">
                        <IoGameControllerOutline size="2rem" />
                        <h1 id="top-navbar-title-text">FreeGamesTracker</h1>
                    </div>

                    {/*
                    <ul id="top-navbar-list">
                        <h5 id="top-navbar-item-text-1" className="top-navbar-item-text">Browse</h5>
                        <h5 id="top-navbar-item-text-2" className="top-navbar-item-text">History</h5>
                        <h5 id="top-navbar-item-text-3" className="top-navbar-item-text">Settings</h5>
                    </ul>
                    */}
                </ul>
            </nav>

            {/* Either use <nav> or <div> + <h2> so the element matches the
            height above. Styles are overwritten when using <nav> + <h1>. You
            can always define custom styles in index.css. */}
            <div id="navbar-title">
                <IoGameControllerOutline size="2rem" />
                <h2 id="navbar-title-text">FreeGamesTracker</h2>
            </div>

            {/* Check if your header indeeds stick using the text below...
            <p style={{fontSize:"3rem"}}>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                do eiusmod tempor incididunt ut labet dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id
                est laborum.

                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                do eiusmod tempor incididunt ut labet dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id
                est laborum.

                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                do eiusmod tempor incididunt ut labet dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id
                est laborum.

                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                do eiusmod tempor incididunt ut labet dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id
                est laborum.

                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                do eiusmod tempor incididunt ut labet dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu
                fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                proident, sunt in culpa qui officia deserunt mollit anim id
                est laborum.
            </p>
            */}

            {/*
            <nav id="btm-navbar-cnt">
                <ul id="btm-navbar">
                    <div id="btm-navbar-item-cnt-1" className="btm-navbar-item-cnt">
                        <IoGameControllerOutline size="2rem" />
                        <p id="btm-navbar-item-text-1" className="btm-navbar-item-text">Browse</p>
                    </div>

                    <div id="btm-navbar-item-cnt-2" className="btm-navbar-item-cnt">
                        <LuHistory size="2rem" />
                        <p id="btm-navbar-item-text-2" className="btm-navbar-item-text">History</p>
                    </div>

                    <div id="btm-navbar-item-cnt-3" className="btm-navbar-item-cnt">
                        <IoSettingsOutline size="2rem" />
                        <p id="btm-navbar-item-text-3" className="btm-navbar-item-text">Settings</p>
                    </div>
                </ul>
            </nav>
            */}
        </>
    )
}
