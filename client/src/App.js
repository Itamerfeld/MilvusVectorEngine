import React from 'react';
import Nav from './components/Nav'
import Upload from './components/Upload'
import Search from './components/Search'

import { BrowserRouter as Router, Route , Redirect } from "react-router-dom";
import Overview from './components/Overview';

export default function App() {

  return (
      <div className='main'>
        <Router>
          <Nav/> 
          <div className='data-main'>
            <Route path="/" exact component={()=><Overview/>} />
            <Route path="/upload" component={()=><Upload/>} />
            <Route path="/search" component={()=><Search/>} />     
            <Redirect to='/'/>    
          </div>  
        </Router>
      </div>   
  );
}
