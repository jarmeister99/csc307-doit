import React, {useState} from "react";
import "../index.css"
import "./css/Login.css"
import axios from 'axios';
import { hashCode } from './helpers/hash.js';

function Login() {
    const [credentials, setCredentials] = useState(
        {
            username: '',
            password_hash: '',
        }
    );

    const [loggedIn, setLoggedIn] = useState(
        {
            attempted: false,
            loggedIn: false
        }
    );

    function handleChange(event) {
        const { name, value } = event.target;
        if (name === "password")
        setCredentials(
            {username: credentials['username'], password_hash: value}
        );
        else if (name === "username")
        setCredentials(
            {username: value, password_hash: credentials['password_hash']}   
        );
    }


    async function checkLogin(credentials){
        try {
            setLoggedIn(
                {attempted: true, loggedIn: false}
            );

            credentials.password_hash = hashCode(credentials.password_hash);
            const response = await axios.post('http://localhost:5000/login', credentials, {withCredentials: true});

            setLoggedIn(
                {attempted: true, loggedIn: true}
            );

            return response;
        }
        catch (error) {
            console.log(error);
            return false;
        }
     }


    function submitLogin() {
        checkLogin(credentials).then( result => {
            console.log(result.status);
            });    
        setCredentials({username: '', password_hash: ''});
    }

    function renderLoggedIn() {
        if(loggedIn.attempted === false) {
            return <div></div>;
        }
        else if(loggedIn.attempted === true && loggedIn.loggedIn === true) {
            return <header style={{color:'green'}}>Logged In!</header>;
        }
        else{
            return <p style={{color:'red'}}>Unsuccessful</p>;
        }
    }

    return (
        <div className="col-md-3">
            <form>
                <div className="username">
                    <label htmlFor="username">username‎‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎</label>
                    <input
                        type="text"
                        name="username"
                        id="username"
                        class="tbox"
                        value={credentials.username}
                        onChange={handleChange} />
                </div>
                <div className="password">
                    <label htmlFor="password">password‏‏‎ ‎‏‏‎‎‏‏‎ ‎‏‏‎ ‎</label>
                    <input
                        type="password"
                        name="password"
                        id="password"
                        class="tbox"
                        value={credentials.password_hash}
                        onChange={handleChange} />
                </div>
                <div className="loginbutton">
                    <input type="button" class="button" value="Login" onClick={submitLogin} />
                </div>
                <div className="loginrender">
                    {renderLoggedIn()}
                </div>
            </form>
        </div>
    );
}

export default Login;