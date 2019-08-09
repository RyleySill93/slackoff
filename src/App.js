import React from 'react';
import './App.css';
import axios from 'axios';
import Dropzone from 'react-dropzone'


class App extends React.Component {
    state = {
        url: '',
        file: null,
        style: 'intensify',
        fileUrl: '',
    };

    render() {
        const uploadFile = (file) => {
            this.setState({ file, fileUrl: URL.createObjectURL(file) });
        };

        const doStuff = () => {
            const formData = new FormData();
            formData.append("file", this.state.file, this.state.file.name);
            axios.post(`${window.location.origin}/${this.state.style}/`, formData).then(res => {
                this.setState({ url: res.data.url })
            });
        };

        function openDialog() {
          document.getElementById('upload-photo').click();
        }

        return (
            <div className="App">
                <header>
                    <h1 className="title">slackoff.</h1>
                </header>
                <main className="App-main">
                    <div className="column">
                        <div className="step">1. UPLOAD</div>
                        <div className="button-holder">
                            <input type="file" id="upload-photo" hidden onChange={event => uploadFile(event.target.files[0])} />
                            {
                                this.state.file ? (
                                    <React.Fragment>
                                        <div/>
                                        <img style={{ width: 100 }} src={this.state.fileUrl} />
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
                        <div className="button-holder">
                            <div/>
                            <select className="button" value={this.state.style} onChange={event => this.setState({ style: event.target.value })}>
                                <option value="bobblify">BOBBLE</option>
                                <option value="intensify">INTENSIFY</option>
                            </select>
                            <div/>
                        </div>
                    </div>
                    <div className="column">
                        <div className="step">3. GENERATE EMOJI</div>
                        <div className="button-holder">
                            {
                                this.state.url ? (
                                    <React.Fragment>
                                        <div/>
                                        <img style={{ width: 100 }} src={this.state.url} />
                                        <div className="another-one">
                                            <img className="dj-khaled" style={{ width: 100 }} src={require('./khaled.png')} />
                                            <button className="button" onClick={doStuff}>ANOTHER ONE</button>
                                        </div>
                                    </React.Fragment>
                                ) : (
                                    <React.Fragment>
                                        <div/>
                                        <button className="button" onClick={doStuff}>CLICK ME</button>
                                        <div/>
                                    </React.Fragment>
                                )
                            }
                        </div>
                    </div>
                </main>
            </div>
        );
    }
}

export default App;
