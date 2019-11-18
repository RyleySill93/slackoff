import React from 'react';
import './App.css';
import {withStyles} from "@material-ui/core";

import axios from 'axios';
import Dropzone from 'react-dropzone'
import { BrowserRouter as Router, Route, Link, withRouter, Switch } from "react-router-dom";
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Masonry from 'react-masonry-component';
import Image from './Gif';
import Detail from './Detail';


var Jimp = require('jimp');



class Meow extends React.Component {
    state = {
        url: '',
        file: null,
        style: 'intensify',
        fileUrl: '',
        loading: false,
    };

    getContent = () => {
        const doStuff = () => {
            if (!this.state.file) return;
            this.setState({ loading: true });
            const formData = new FormData();
            formData.append("file", this.state.file, this.state.file.name);
            axios.post(`http://localhost:8000/${this.state.style}/`, formData).then(res => {
                this.setState({ url: res.data.url })
            })
                .finally(() => this.setState({ loading: false }));
        };

        if (this.state.loading) {
            return (
                <React.Fragment>
                    <div/>
                    <div className="loader">Loading...</div>
                    <div/>
                </React.Fragment>
            )
        } else if (this.state.url) {
            return (
                <React.Fragment>
                    <div/>
                    <img style={{ height: 200 }} src={this.state.url} />
                    <div className="another-one">
                        <img className="dj-khaled" style={{ width: 100 }} src={require('./khaled.png')} />
                        <button className="button" onClick={doStuff}>ANOTHER ONE</button>
                    </div>
                </React.Fragment>
            )
        }

        return (
            <React.Fragment>
                <div/>
                <button className="button" onClick={doStuff}>CLICK ME</button>
                <div/>
            </React.Fragment>
        )
    };

    render() {
        const uploadFile = (file) => {
            this.setState({ file, fileUrl: URL.createObjectURL(file) });
        };

        function openDialog() {
          document.getElementById('upload-photo').click();
        }

        const app = (
            <main className="App-main">
                <div className="column">
                    <div className="step">1. UPLOAD FACE</div>

                    <div className="button-holder">
                        <input type="file" id="upload-photo" hidden onChange={event => uploadFile(event.target.files[0])} />
                        {
                            this.state.file ? (
                                <React.Fragment>
                                    <div/>
                                    <img style={{ height: 200 }} src={this.state.fileUrl} />
                                    <button className="button" onClick={openDialog}>SEND PICS? ;)</button>
                                </React.Fragment>
                            ) : (
                                <React.Fragment>
                                    <div/>
                                    <button className="button" onClick={openDialog}>SEND PICS? ;)</button>
                                    <div/>
                                </React.Fragment>
                            )
                        }
                    </div>
                </div>
                <div className="column column-middle">
                    <div className="step">2. SELECT STYLE</div>
                    <small>&nbsp;</small>
                    <div className="button-holder">
                        <div/>
                        <select className="button" value={this.state.style} onChange={event => this.setState({ style: event.target.value })}>
                            <option value="bobblify">:BOBBLE:</option>
                            <option value="intensify">:INTENSIFY:</option>
                            <option value="detective">:DETECTIVE:</option>
                            <option value="appears">:APPEARS:</option>
                            <option value="disappears">:DISAPPEARS:</option>
                            <option value="carlton_dance">:CARLTON:</option>
                            <option value="rap_battle">:RAP_BATTLE:</option>
                            <option value="strut">:STRUT:</option>
                            <option value="trapped">:LET_ME_IN:</option>
                            <option value="wrecking-ball">:WRECKING_BALL:</option>
                            <option value="heres-johnny">:HERES_JOHNNY:</option>
                            <option value="javert">:JAVERT:</option>
                            <option value="time">:TIME:</option>
                            <option value="left-hanging">:LEFT_HANGING:</option>
                            <option value="thinking">:THINKING:</option>
                            <option value="trump">:TRUMP:</option>
                            <option value="hide">:HIDE:</option>
                            <option value="begging">:BEGGING:</option>
                            <option value="chimp">:CHIMP:</option>
                            <option value="fire">:FIRE:</option>
                            <option value="computer_kid">:COMPUTER_KID:</option>
                            <option value="toast">:TOAST:</option>
                            <option value="clapping">:CLAPPING:</option>
                            <option value="mind_blown">:MIND_BLOWN:</option>
                        </select>
                        <div/>
                    </div>
                </div>
                <div className="column">
                    <div className="step">3. GENERATE EMOJI</div>
                    <Link className="caption" to="/how-to-upload-an-emoji">how do I upload an emoji to slack?</Link>
                    <div className="button-holder">
                        { this.getContent() }
                    </div>
                </div>
            </main>
        );

        return (
            <Router>
              <div className="App">
                <header className="header">
                    <Link className="title" to="/">
                        slackoff.
                    </Link>
                </header>
                <Route exact path="/" component={() => app} />
              </div>
            </Router>
        )
    }
}


const styles = {
    width: {
        width: 1100,
        margin: '0 auto',
    }
}

class App extends React.Component {
    state = {
        url: '',
        file: true,
        style: 'intensify',
        fileUrl: '',
        loading: false,
        imageUrls: [],
    };

    getContent = () => {
        const doStuff = () => {
            if (!this.state.file) return;
            this.setState({ loading: true });
            const formData = new FormData();
            formData.append("file", this.state.file, this.state.file.name);
            axios.post(`${window.location.origin}/${this.state.style}/`, formData).then(res => {
                this.setState({ url: res.data.url })
            }).finally(() => this.setState({ loading: false }));
        };

        if (this.state.loading) {
            return (
                <React.Fragment>
                    <div/>
                    <div className="loader">Loading...</div>
                    <div/>
                </React.Fragment>
            )
        } else if (this.state.url) {
            return (
                <React.Fragment>
                    <div/>
                    <img style={{ height: 200 }} src={this.state.url} />
                    <div className="another-one">
                        <img className="dj-khaled" style={{ width: 100 }} src={require('./khaled.png')} />
                        <button className="button" onClick={doStuff}>ANOTHER ONE</button>
                    </div>
                </React.Fragment>
            )
        }

        return (
            <React.Fragment>
                <div/>
                <button className="button" onClick={doStuff}>CLICK ME</button>
                <div/>
            </React.Fragment>
        )
    }

    componentDidMount(){
        fetch('https://i.imgur.com/LuF7JAs.png?1').then(response => {
          response.blob().then(blobResponse => {
            const urlCreator = window.URL || window.webkitURL;
            const fileUrl = urlCreator.createObjectURL(blobResponse);
            this.setState({fileUrl})
          })
        })

        axios.get('http://localhost:8000/gifs/').then(res => {
            this.setState({imageUrls: res.data})
        }).catch(err => {
            debugger
        })
    }

    render() {
        const { classes } = this.props;
        const uploadFile = (file) => {
            this.setState({ file, fileUrl: URL.createObjectURL(file) });
        };

        function openDialog() {
          document.getElementById('upload-photo').click();
        }

        const rotate = () => {
            Jimp.read(this.state.fileUrl)
            .then(image => {
                debugger
                image.rotate(30).getBase64(Jimp.AUTO, (err, res) => {
                    this.setState({fileUrl: res})
                console.log(res)
              })
                debugger
            })
            .catch(err => {
                debugger
            })
        }

        return (
            <Router>
              <div className="App">
                <header className="header">
                    <Link className="title" to="/">
                        slackoff.
                    </Link>
                </header>
                  <div>
                  </div>
                  {/*<Switch>*/}
                  {/*    <Route*/}
                  {/*        path="/:type"*/}
                  {/*        render={routeProps => (*/}
                  {/*            <Detail type={routeProps.match.params.type} />*/}
                  {/*        )}*/}
                  {/*    />*/}
                  {/*    <Route*/}
                  {/*        path="/"*/}
                  {/*        render={() => (*/}
                  {/*            <div className={classes.width}>*/}
                  {/*                <Masonry>*/}
                  {/*                    {*/}
                  {/*                      this.state.imageUrls.slice(0,3).map(image => <Image url={image.url} type={image.type} />)*/}
                  {/*                  }*/}
                  {/*                </Masonry>*/}
                  {/*            </div>*/}
                  {/*        )}*/}
                  {/*    />*/}
                  {/*</Switch>*/}
              </div>
            </Router>
        )
    }
}

export default withStyles(styles)(Meow);
