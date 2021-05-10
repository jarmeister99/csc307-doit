import React, {useState} from "react";
import "../index.css"

function Login() {
    const [credentials, setCredentials] = useState(
        {
            username: '',
            password: '',
        }
    );

    function handleChange(event) {
        const { name, value } = event.target;
        console.log(name);
        console.log(value);
        if (name === "password")
        setCredentials(
            {name: credentials['username'], password: value}
        );
        else     
        setCredentials(
            {name: value, password: credentials['password']}   
        );
    }

    function checkLogin(credentials) {
        // make a post call to check agains the api and check the login information
        console.log(credentials);
    }

    function submitLogin() {
        checkLogin(credentials);
        setCredentials({username: '', password: ''});
    }

    return (
        <form>
            <div className="col-sm-10 form-group-lg">
                <div className="column">
                    <label htmlFor="username">username</label>
                    <input
                        type="text"
                        name="username"
                        id="username"
                        value={credentials.username}
                        onChange={handleChange} />
                </div>
                <div className="column">
                    <label htmlFor="password">password</label>
                    <input
                        type="text"
                        name="password"
                        id="password"
                        value={credentials.password}
                        onChange={handleChange} />
                </div>
                <div className="column">
                    <input type="button" value="Submit" onClick={submitLogin} />
                </div>
            </div>
        </form>
    );
}

export default Login;