import React from "react";
import {Link } from "react-router-dom";

    function home() {

        return (
        <div >
            
            <p className="text">
                
            Select a button:
          
            </p>
            <Link to="/projectid_search"><button className="formbutton">
            Search by Project ID 
            </button>
            </Link>
            
            <Link to="/username_search"><button className="formbutton"> 
            Search by Username 
            </button>
            </Link>
        </div>
        
        );

    }

    export default home;