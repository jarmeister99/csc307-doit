import React, {useState} from "react";
import "../index.css"
import axios from 'axios';

function Login() {
    const [credentials, setCredentials] = useState(
        {
            username: '',
            password_hash: '',
        }
    );

    function handleChange(event) {
        const { name, value } = event.target;
        if (name === "password")
        setCredentials(
            {username: credentials['username'], password_hash: value}
        );
        else
        setCredentials(
            {username: value, password_hash: credentials['password_hash']}   
        );
    }


    async function checkLogin(credentials){
        try {
           const response = await axios.post('http://localhost:5000/login', credentials);
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
        setCredentials({username: '', password_hash: ''});
    }


    return (
        <form>
            <div>
                <label htmlFor="username">username</label>
                <input
                    type="text"
                    name="username"
                    id="username"
                    value={credentials.username}
                    onChange={handleChange} />
            </div>
            <div>
                <label htmlFor="password">password</label>
                <input
                    type="text"
                    name="password"
                    id="password"
                    value={credentials.password_hash}
                    onChange={handleChange} />
            </div>
            <div>
                <input type="button" value="Submit" onClick={submitLogin} />
            </div>
        </form>
    );
}

export default Login;