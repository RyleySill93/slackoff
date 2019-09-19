import React from 'react';
import {BrowserRouter as Router, Link} from "react-router-dom";
import {withStyles} from "@material-ui/core";

import Routes from './Routes';


const styles = {
    app: {
        textAlign: 'center',
        minHeight: '100vh',
        fontSize: 'calc(10px + 2vmin)',
        fontFamily: 'Baloo',
        color: '#433f4a',
        backgroundColor: '#ffd139',
        height: '100vh',
        justifyContent: 'space-between',
        display: 'flex',
        flexDirection: 'column',
    },
    header: {
        display: 'flex',
        alignItems: 'flex-start',
    },
    title: {
        fontFamily: 'Pacifico',
        fontWeight: 'bold',
        color: '#433f4a',
        fontSize: '70px',
        margin: '0px 0px 0px 30px',
        textAlign: 'left',
        textDecoration: 'none',
    },
    center: {
        width: 1100,
        margin: '0 auto',
    },
};

function App(props) {
    const { classes } = props;
    return (
        <Router>
            <div className={ classes.app }>
                <header className={ classes.header }>
                    <Link className={ classes.title } to="/">
                        slackoff.
                    </Link>
                </header>
                <div className={ classes.center }>
                    <Routes />
                </div>
                <div />
            </div>
        </Router>
    )
}

export default withStyles(styles)(App);
