import React from 'react';
import './App.css';
import {withStyles} from "@material-ui/core";

import axios from 'axios';
import Masonry from 'react-masonry-component';
import Image from './Gif';


var Jimp = require('jimp');

const styles = {
    width: {
        width: 1100,
        margin: '0 auto',
    }
};

class Gifs extends React.Component {
    state = {
        imageUrls: [],
    };

    componentDidMount(){
        axios.get('http://localhost:8000/gifs/').then(res => {
            this.setState({imageUrls: res.data})
        }).catch(err => {
            debugger
        })
    }

    render() {
        const { classes } = this.props;

        return (
            <div className={classes.width}>
                <Masonry columnWidth={100}>
                    {
                        this.state.imageUrls.map(image => (
                            <Image
                                url={image.url}
                                type={image.type}
                                width={image.width}
                                height={image.height}
                            />
                        ))
                    }
                </Masonry>
            </div>
        )
    }
}

export default withStyles(styles)(Gifs);
