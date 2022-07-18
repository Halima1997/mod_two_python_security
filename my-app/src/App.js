import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import projectid_data from './projectid_search'
import username_data from './username_search'
import home from './homepage'


export default function App() {
    return (
            <Router>
                <div>
                    <Switch>
                        <Route path="/home" component={ home } />   
                        <Route path="/projectid_search" component={ projectid_data } />
                        <Route path="/username_search" component={ username_data } />
                    </Switch>

                </div>
            </Router>
    )
}


