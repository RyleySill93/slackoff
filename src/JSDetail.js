import React from 'react';
import axios from 'axios';
import {withStyles} from "@material-ui/core";
import Button from "./Button";
import {Link} from "react-router-dom";
import { makeGif } from './utils';
import {TrackedElement} from "./imageData";
import clapping from './clapping';
import strut from './strut';
var Jimp = require('jimp');



const styles = {
    detail: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 'calc(100vh - 123px)',
    },
    rightSide: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        width: 400,
    },
    image: {
        borderRadius: 32,
        height: 400,
        alignSelf: 'center',
    },
    faceUploader: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    uploadedImage: {
        alignSelf: 'center',
        height: 200,
        marginBottom: 16,
    },
    buttonCaption: {
        fontSize: 12,
        color: '#433f4a',
        textDecoration: 'underline',
        cursor: 'pointer',
        marginTop: 8,
    },
};

const origin = 'http://localhost:8000';


class JSDetail extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: '',
            file: '',
            loading: false,
        };
        this.uploadFile = this.uploadFile.bind(this);
    }

    componentDidMount() {
        const { type } = this.props.match.params;

        axios.get(`${origin}/types?type=${type}`).then(
            res => this.setState({ url: res.data.url })
        )
    }

    async uploadFile(file) {
        //
        const dude = await Jimp.read(URL.createObjectURL(file)).then(res => res);
        const that = this;

        const trackedElements = [
            new TrackedElement(
                1,
                dude,
            )
        ]

        const meow = await makeGif(this.state.url, trackedElements, strut);

        this.setState({url: meow})

        // const that = this;
        // gifFrames({ url: this.state.url, frames: 'all' }).then(function (frameData) {
        //     Jimp.read( URL.createObjectURL(file)).then(uploadedFile => {
        //         Jimp.read(frameData[0].getImage()._obj).then(image => {
        //             const meow = image.composite(uploadedFile, 0, 0);
        //             meow.getBase64(Jimp.AUTO, (err, res) => {
        //                 debugger
        //                 that.setState({meow: res})
        //             })
        //         })
        //     })
        // });
    }


    render() {
        const { classes } = this.props;

        const openDialog = () => {
          document.getElementById('upload-photo').click();
        };

        return (
            <div className={ classes.detail }>
                <div style={{ width: this.state.imgWidth }}>
                    {
                        this.state.loading ? (
                            <div className="loader" />
                        ) : (
                            <img
                                className={ classes.image }
                                src={this.state.url}
                                onLoad={dude => {
                                    const ratio = dude.target.naturalHeight / dude.target.naturalWidth;
                                    this.setState({ imgWidth: 400 / ratio })
                                }}
                            />
                        )
                    }
                </div>
                <div className={ classes.rightSide }>
                    <div className={ classes.faceUploader }>
                        <input type="file" id="upload-photo" hidden onChange={event => this.uploadFile(event.target.files[0])} />
                        {/*{ this.state.fileUrl && <img className={ classes.uploadedImage } src={this.state.fileUrl} /> }*/}
                        <Button onClick={ openDialog }>
                            UPLOAD A FACE
                        </Button>
                        <Link
                            className={ classes.buttonCaption }
                            to="/how-to-cut-out-a-face"
                        >
                            How do I get a face cutout from a picture?
                        </Link>
                    </div>
                    <img src={ this.state.meow } />>
                </div>
            </div>
        )
    }
}

export default withStyles(styles)(JSDetail);