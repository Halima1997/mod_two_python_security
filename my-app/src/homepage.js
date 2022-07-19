import React from "react";
import {Link } from "react-router-dom";

    function home() {

        return (
        <div>
            <p>
            Homepage
            <br />
            Select a button below.
            </p>
            <Link to="/projectid_search"><button>
            Search by Project ID 
            </button>
            </Link>
            
            <Link to="/username_search"><button>
            Search by Username 
            </button>
            </Link>
        </div>
        
        );

    }

    export default home;