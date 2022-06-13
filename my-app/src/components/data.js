import React, { useState } from "react";


export default function App() {
  const [usernames, setUsernames] = useState([]);
  const [query, setQuery] = useState("");


  const handleSubmit = (e) => {
    e.preventDefault();
  
    if (!query) return;

    async function fetchData() {
      const response = await fetch(
        `users_projectid/${query}`
      );
      const data = await response.json();
      setUsernames(data.usernames);
    }
    fetchData();
    
    
  } ;

  return (
    <div className="App"
      style={{
      margin: 20,
      }}
     >
      <form onSubmit={handleSubmit}>
        <br/>
        <label>
          Input Project ID:{" "}
          <input
            type="text"
            placeholder="enter project_id"
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
            }}
          />
        </label>
        <input type="submit" value="Submit"/>
      </form>
      
      <ul>
        {
          usernames.map((users) => {
            
            return (
              <div key = { users } >
                <ul>{users}</ul>
              </div>
                
            )
          })  
        }
      </ul>
      
    </div>
  );
}
