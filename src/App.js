import React from 'react';
import './App.css';
import axios from 'axios';
import Dropzone from 'react-dropzone'
import { BrowserRouter as Router, Route, Link, withRouter } from "react-router-dom";


class App extends React.Component {
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
            axios.post(`${'http://localhost:8000'}/${this.state.style}/`, formData).then(res => {
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
    }

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
                    <Link className="caption" to="/how-to-cut-out-a-face">how do I get a face cutout from a picture?</Link>
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

        const howtoface = (
            <main className="help-section">
                <img className="gif" src="http://i.imgur.com/DHRYpiZ.gif" />
                <div className="section-title">
                    How to cut out a face from a picture
                </div>
                <ol>
                    <li>
                        Open up your picture in Preview. If you don't have a Mac, start <a href="https://www.apple.com/shop/buy-mac/macbook-pro">here.</a>
                    </li>
                    <li>
                        Click on the toolbox or pen button the upper right hand corner, then select the lasso tool.
                    </li>
                    <img className="gif" src="https://media.giphy.com/media/hqljpSlE9NWsCqO94Q/giphy.gif" />
                    <li>
                        Carefully cut the face out of the picture. When you're done, click crop and convert.
                    </li>
                    <img className="gif" src="https://media.giphy.com/media/dxTpaE9A6TXGdRXb9u/giphy.gif" />
                </ol>
            </main>
        );


        const howtoemoji = (
            <main className="help-section">
                <img className="gif" src="https://media.giphy.com/media/iJIkiyiuGQA81nqOpF/giphy.gif" />
                <div className="section-title">
                    How to upload an emoji to slack
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
                <Route path="/how-to-cut-out-a-face" component={ () => howtoface} />
                <Route path="/how-to-upload-an-emoji" component={ () => howtoemoji} />
              </div>
            </Router>
        )
    }
}

export default App;
