import React from 'react';
import './App.css';
import axios from 'axios';
import Dropzone from 'react-dropzone'


class App extends React.Component {
    state = {
        data: '',
        file: null,
        style: 'intensify'
    };

    render() {
        const uploadFile = (file) => {
            this.setState({ file })
        };

        const doStuff = () => {
            const formData = new FormData();
            formData.append("file", this.state.file, this.state.file.name);
            axios.post(`http://localhost:8000/${this.state.style}/`, formData).then(res => {
                this.setState({ data: res.data })
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
                            <button className="button" onClick={openDialog}>SEND PICS? ;)</button>
                        </div>
                    </div>
                    <div className="column column-middle">
                        <div className="step">2. SELECT STYLE</div>
                        <div className="button-holder">
                            <select className="button" value={this.state.style} onChange={event => this.setState({ style: event.target.value })}>
                                <option value="bobblify">BOBBLE</option>
                                <option value="intensify">INTENSIFY</option>
                            </select>
                        </div>
                    </div>
                    <div className="column">
                        <div className="step">3. GENERATE EMOJI</div>
                        <div className="button-holder">
                            {
                                this.state.data ? (
                                    <img style={{ width: 100 }} src={`data:image/gif;base64,${this.state.data}`} />
                                ) : <button className="button" onClick={doStuff}>CLICK ME</button>
                            }
                        </div>
                    </div>
                </main>
            </div>
        );
    }
}

export default App;
