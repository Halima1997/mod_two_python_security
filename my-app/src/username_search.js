import React, { useState } from "react";


export default function App() {
  const [result, setResult] = useState([]);
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    
  
    if (!query) return;

    async function fetchData() {
      const response = await fetch(
        `users_username/${query}`
      );
      
      const username_data = await response.json();
      console.log(username_data)
      if (!response.ok) {
        window.alert(response.status)
        return
      }

      setResult(username_data.result);
      
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
          Input Username:{" "}
          <input 
            className="forminput"
            type="text"
            placeholder="username"
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
            }}
            
          />
          
        </label>
        <input className="formbutton" type="submit" value="Submit"/>
      </form>
      
      <ul>
        {
          result.map((user) => {
            
            return (
              <div key = { user } >
                <ul>{user}</ul>
              </div>
                
            )
          })}
        </ul>

      
    </div>
  );
}
