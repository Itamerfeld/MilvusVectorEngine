import React from 'react'
import {NavLink} from 'react-router-dom'
import View from '@material-ui/icons/ViewWeek';
import Upload from '@material-ui/icons/Description';
import Search from '@material-ui/icons/FolderOpen';

export default function Nav() {

    return (
        <div className='nav-main'>
            <div className='nav-header'>
                <p>MVC</p>
            </div>
            <div>
                <NavLink className="nav-item" activeClassName='nav-item-active' exact to='/'><View/><p>Overview</p></NavLink>
                <NavLink className="nav-item" activeClassName='nav-item-active' to='/upload'><Upload/><p>Upload</p></NavLink>
                <NavLink className="nav-item" activeClassName='nav-item-active' to='/search'><Search/><p>Search</p></NavLink>
            </div>
        </div>
    )
}