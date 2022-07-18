import React, { useState } from "react";


export default function App() {
  const [result, setResult] = useState([]);
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    
  
    if (!query) return;

    async function fetchData() {
      const response = await fetch(
        `users_projectid/${query}`
      );
      
      const projectid_data = await response.json();
      console.log(projectid_data)
      if (!response.ok) {
        window.alert(response.status)
        return
      }

      setResult(projectid_data.result);
      
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
            className="forminput"
            type="text"
            placeholder="project id"
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
          result.map((id) => {
            
            return (
              <div key = { id } >
                <ul>{id}</ul>
              </div>
                
            )
          })}
        </ul>

      
    </div>
  );
}
