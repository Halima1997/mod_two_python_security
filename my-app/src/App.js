import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import data from './components/data'



export default function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/data" component={ data } />
                </Switch>

            </div>
        </Router>
    )
}
