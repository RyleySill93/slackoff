import React from 'react';
import {BrowserRouter as Router, Link} from "react-router-dom";
import {withStyles} from "@material-ui/core";
import Search from '@material-ui/icons/Search';
import AppBar from '@material-ui/core/AppBar';

import Routes from './Routes';
import Button from './Button';

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
        width: 1100,
        margin: '0 auto',
        marginTop: 155,
    },
    header: {
        display: 'flex',
        alignItems: 'center',
        flexDirection: 'column',
        backgroundColor: '#ffd139',
        boxShadow: 'none',
        height: 155,
    },
    title: {
        fontFamily: 'Pacifico',
        fontWeight: 'bold',
        color: '#433f4a',
        fontSize: '50px',
        display: 'block',
        textAlign: 'left',
        marginLeft: 4,
        marginBottom: 4,
        textDecoration: 'none',
    },
    center: {
        width: 1100,
        margin: '0 auto',
    },
    inputContainer: {
        width: 'calc(100% - 35px)',
        height: 50,
        backgroundColor: '#efeef1',
        display: 'flex',
        borderRadius: 8,
        border: '3px solid #433f4a',
    },
    search: {
        backgroundColor: '#EE7AAA',
        width: 50,
        color: '#efeef1',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: '5px 0px 0px 5px',
    },
    input: {
        backgroundColor: 'transparent',
        boxShadow: 'none',
        border: 'none',
        width: '100%',
        outline: 'none',
        fontFamily: 'Baloo',
        fontSize: 25,
        fontWeight: 100,
        marginLeft: 12,
        color: '#433f4a',
    },
    headerContent: {
        width: 1100,
    },
    titleBlock: {
        display: 'flex',
        justifyContent: 'space-between',
        width: 'calc(100% - 25px)',
        alignItems: 'center',
    }
};

function App(props) {
    const { classes } = props;
    return (
        <Router>
            <div className={ classes.app }>
                <AppBar className={ classes.header }>
                    <div className={ classes.headerContent }>
                        <div className={classes.titleBlock}>
                            <Link className={ classes.title } to="/">
                                gifhub
                            </Link>
                            <Button>
                                Log in
                            </Button>
                        </div>
                        <div className={ classes.inputContainer } position="sticky">
                            <div className={ classes.search }>
                                <Search />
                            </div>
                            <input className={classes.input} type="text" placeholder="Find a GIF"/>
                        </div>
                    </div>
                </AppBar>
                <div className={ classes.center }>
                    <Routes />
                </div>
                <div />
            </div>
        </Router>
    )
}

export default withStyles(styles)(App);
