import React, {useState} from "react";
import "../index.css"
import "./css/Login.css"
import axios from 'axios';
import { hashCode } from './helpers/hash.js';

function Register() {
    const [credentials, setCredentials] = useState(
        {
            username: '',
            password_hash: '',
            email: ''
        }
    );

    const [registered, setRegistered] = useState(
        {
            attempted: false,
            correct: false
        }
    );

    function handleChange(event) {
        const { name, value } = event.target;
        if (name === "password")
        setCredentials(
            {username: credentials['username'], 
             password_hash: value, 
             email: credentials['email']}
        );
        else if (name === "username")
        setCredentials(
            {username: value, 
             password_hash: credentials['password_hash'],
             email: credentials['email']}   
        );
        else
        setCredentials(
            {username: credentials['username'], 
             password_hash: credentials['password_hash'],
             email: value}   
        );
    }


    async function checkLogin(credentials){
        try {
            setRegistered(
                {attempted: true, correct: false}
            );
            
            credentials.password_hash = hashCode(credentials.password_hash);
            const response = await axios.post('http://localhost:5000/register', credentials);

            setRegistered(
                {attempted: true, correct: true}
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
        setCredentials({username: '', password_hash: '', email: ''});
    }

    function renderRegister() {
        if(registered.attempted === false) {
            return <div></div>;
        }
        else if(registered.attempted === true && registered.correct === true) {
            return <header style={{color:'green'}}>Created!</header>;
        }
        else{
            return <p style={{color:'red'}}>Unsuccesful</p>;
        }
    }

    return (
        <form>
            <div className="username">
                <label htmlFor="username">username‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎</label>
                <input
                    type="text"
                    name="username"
                    id="username"
                    class="tbox"
                    value={credentials.username}
                    onChange={handleChange} />
            </div>
            <div className="password">
                <label htmlFor="password">password‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎</label>
                <input
                    type="password"
                    name="password"
                    id="password"
                    class="tbox"
                    value={credentials.password_hash}
                    onChange={handleChange} />
            </div>
            <div className="email">
                <label htmlFor="password">email‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎</label>
                <input
                    type="text"
                    name="email"
                    id="email"
                    class="tbox"
                    value={credentials.email}
                    onChange={handleChange} />
            </div>
            <div className="registerbutton">
                <input type="button" className="button" value="Submit" onClick={submitLogin} />
            </div>
            <div className="registerrender">
                    {renderRegister()}
            </div>
        </form>
    );
}

export default Register;