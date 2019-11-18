import React from 'react';
import {withStyles} from "@material-ui/core";


const styles = {
    button: {
        borderRadius: 3,
        height: 50,
        margin: 5,
        width: 200,
        textAlign: 'center',
        backgroundColor: '#efeef1',
        color: '#433f4a',
        border: '5px solid #EE7AAA',
        boxShadow: '0 10px #DB5B90',
        cursor: 'pointer',
        fontSize: 24,
        fontFamily: 'Baloo',
        outline: 'none',
        transition: 'transform 0.1s, box-shadow 0.1s',
        zIndex: 1,
        '&:hover': {
            backgroundColor: '#efeef1',
            color: '#EE7AAA',
            boxShadow: '0 8px #DB5B90',
            transform: 'translateY(2px)',
        },
        '&:active': {
            backgroundColor: '#EE7AAA',
            color: '#fff',
            boxShadow:' 0 0px #DB5B90',
            transform: 'translateY(10px)',
        }
    }
};

function Button(props) {
    return (
        <button className={props.classes.button} {...props}>
            { props.children }
        </button>
    )
}

export default withStyles(styles)(Button);