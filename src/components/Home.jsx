import React from "react";

function Home() {
  return (
    <div className="home">
      <div class="container">
        <div class="row align-items-center my-5">
          <div class="col-lg-7">
            <img
              class="img-fluid rounded mb-4 mb-lg-0"
              src="http://placehold.it/900x400"
              alt=""
            />
          </div>
          <div class="col-lg-5">
            <h1 class="font-weight-light">Home</h1>
            <p>
              Welcome to Do it! The one stop shop for scheduling all of your to-do list needs.
              More to come on the home page once functionality is finalized.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;