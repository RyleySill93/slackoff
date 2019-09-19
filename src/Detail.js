import React from 'react';
import axios from 'axios';
import {withStyles} from "@material-ui/core";
import Button from "./Button";
import {Link} from "react-router-dom";


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


class Detail extends React.Component {
    state = {
        url: '',
        file: '',
        loading: false,
    };

    componentDidMount() {
        const { type } = this.props.match.params;

        axios.get(`${origin}/types?type=${type}`).then(
            res => this.setState({ url: res.data.url })
        )
    }

    render() {
        const { classes } = this.props;

        const uploadFile = (file) => {
            this.setState({ file, fileUrl: URL.createObjectURL(file) });
            doStuff(file)
        };

        const openDialog = () => {
          document.getElementById('upload-photo').click();
        };

        const doStuff = (file) => {
            this.setState({ loading: true });
            const formData = new FormData();
            formData.append("file", file, file.name);
            axios.post(`${origin}/${this.props.match.params.type}/`, formData).then(res => {
                this.setState({ url: res.data.url })
            }).finally(() => this.setState({ loading: false }));
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
                        <input type="file" id="upload-photo" hidden onChange={event => uploadFile(event.target.files[0])} />
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
                </div>
            </div>
        )
    }
}

export default withStyles(styles)(Detail);