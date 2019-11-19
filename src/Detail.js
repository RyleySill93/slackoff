import React from 'react';
import axios from 'axios';
import {withStyles} from "@material-ui/core";
import Button from "./Button";
import {Link} from "react-router-dom";
import Gifs from "./Gifs";
import ForwardIcon from '@material-ui/icons/Forward';
import Chip from '@material-ui/core/Chip';

const styles = {
    detail: {
        display: 'flex',
        margin: '20px 0px 15px 0px',
    },
    rightSide: {
        padding: '0px 20px 20px 20px',
        display: 'flex',
        flexDirection: 'column',
    },
    right: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexGrow: 1,
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
    meow: {
        marginBottom: 20,
    },
    tagHolder: {
        display: 'flex',
        marginBottom: 15,
    },
    tag: {
        border: '3px solid #DB5B90',
        margin: '0px 3px',
        backgroundColor: '#efeef1',
        fontWeight: 400,
        borderRadius: 200,
        height: 40,
        cursor: 'pointer',
        fontFamily: 'Baloo',
        '&:hover': {
            color: '#DB5B90',
        },
    },
    uploader: {
        display: 'flex',
        alignItems: 'center',
    },
    targetFace: {
        height: 100,
    },
    arrow: {
        fontSize: 75,
    },
    title: {
        fontSize: 30,
    }
};

const origin = 'http://localhost:8000';


class Detail extends React.Component {
    state = {
        url: '',
        files: [],
        loading: false,
    };

    componentDidMount() {
        const { type } = this.props.match.params;

        axios.get(`${origin}/types?type=${type}`).then(
            res => this.setState({ url: res.data.url, tracked_element_ids: res.data.tracked_element_ids })
        )
    }

    render() {
        const { classes } = this.props;

        const uploadFile = (file) => {
            const files = [...this.state.files, file];
            this.setState({ files });
        };

        const openDialog = () => {
          document.getElementById('upload-photo').click();
        };

        const doStuff = () => {
            this.setState({ loading: true });
            const formData = new FormData();
            this.state.files.forEach((file, index) => {
                formData.append(`${this.state.tracked_element_ids[index]}`, file, file.name);
            });
            formData.append("type", this.props.match.params.type);

            axios.post(`${origin}/make_gif/`, formData).then(res => {
                this.setState({ url: res.data.url })
            }).finally(() => this.setState({ loading: false }));
        };

        return (
            <div>
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
                        <div className={ classes.title }>
                            Create a GIF
                        </div>
                        <div className={ classes.right }>
                            <div/>
                            <div className={ classes.uploader }>
                                <img
                                    className={ classes.targetFace }
                                    src="https://www.freepngimg.com/thumb/drake/20552-2-drake-face-transparent-thumb.png"
                                />
                                <ForwardIcon className={ classes.arrow } />
                                <Button onClick={ openDialog }>
                                    CHOOSE A FACE
                                </Button>
                                <input type="file" id="upload-photo" hidden onChange={event => uploadFile(event.target.files[0])} />
                            </div>
                            <Button onClick={ doStuff }>
                                SEND IT
                            </Button>
                        </div>
                    </div>
                </div>
                {/*<div className={ classes.rightSide }>*/}
                {/*    <div className={ classes.faceUploader }>*/}
                {/*        <input type="file" id="upload-photo" hidden onChange={event => uploadFile(event.target.files[0])} />*/}
                {/*        /!*{ this.state.fileUrl && <img className={ classes.uploadedImage } src={this.state.fileUrl} /> }*!/*/}
                {/*        <Button onClick={ openDialog }>*/}
                {/*            CHOOSE A FACE*/}
                {/*        </Button>*/}
                {/*        <Button onClick={ doStuff }>*/}
                {/*            SEND IT*/}
                {/*        </Button>*/}
                {/*    </div>*/}
                {/*</div>*/}
                <div className={classes.tagHolder}>
                    <Chip
                        className={classes.tag}
                        label="#strut"
                    />
                    <Chip
                        className={classes.tag}
                        label="#confident"
                    />
                    <Chip
                        className={classes.tag}
                        label="#walk"
                    />
                </div>
                <Gifs />
            </div>
        )
    }
}

export default withStyles(styles)(Detail);