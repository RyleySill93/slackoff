import React, {Component} from "react";
import { Link } from 'react-router-dom';
import {withStyles} from "@material-ui/core";
import Button from './Button';

const styles = {
    imageHolder: {
        margin: '8px 8px -2px 8px',
        '&:hover div': {
            display: 'flex',
        },
        cursor: 'zoom-in',
        backgroundColor: '#433f4a',
        borderRadius: 8,
    },
    buttonHolder: {
        height: '100%',
        width: 250,
        position: 'absolute',
        display: 'none',
        top: 0,
        justifyContent: 'flex-end',
        backgroundColor: 'rgba(239, 239, 239, 0.5)',
        borderRadius: 8,
    },
    image: {
        display: 'block',
        width: 250,
        borderRadius: 8,
    },
};

class Image extends Component {
    render() {
        const { classes, url, type, width, height } = this.props;


        return (
            <div className={classes.imageHolder} style={{ minHeight: height / (width / 250) }}>
                <Link to={ type }>
                    <img src={url} className={classes.image} />
                    <div className={classes.buttonHolder}>
                        {/*<Button text="generate" />*/}
                    </div>
                </Link>
            </div>
        );
    }
}


export default withStyles(styles)(Image);
