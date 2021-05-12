import React, {useState} from "react";
import "../index.css"
import "./Login.css"
import axios from 'axios';

function Register() {
    const [credentials, setCredentials] = useState(
        {
            username: '',
            password_hash: '',
            email: ''
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
           const response = await axios.post('http://localhost:5000/register', credentials);
           console.log("here");
           return response;
        }
        catch (error) {
           console.log(error);
           console.log("also here");
           return false;
        }
     }


    function submitLogin() {
        console.log(credentials);
        checkLogin(credentials).then( result => {
            console.log(result.status);
            });
        setCredentials({username: '', password_hash: '', email: ''});
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
        </form>
    );
}

export default Register;