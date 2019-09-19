import React from 'react';
import { withStyles } from "@material-ui/core";

const styles = {

};

function HowToFace(props) {
    return (
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
    )
}

export default withStyles(styles)(HowToFace)
