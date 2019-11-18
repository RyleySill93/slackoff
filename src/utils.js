import gifshot from "gifshot";
import asdf from 'gif.js.optimized';
var gifFrames = require('gif-frames');
var Jimp = require('jimp');


function convertFramesToJimpFrames(framesData) {
    return framesData.map(frame => convertFrameToJimp(frame))
}

function convertFrameToJimp(frame) {
    return Jimp.read(frame.getImage()._obj).then(image => image);
}

function gifUrlToJimpFrames(url) {
    return gifFrames({url, frames: 'all'}).then(frameData => convertFramesToJimpFrames(frameData));
}

function composite(trackedElementPosition, frame, pasteImage, xAdj, yAdj) {
    const { width, height } = pasteImage.bitmap;
    const halfWidth = Math.floor(width / 2);
    const halfHeight = Math.floor(height / 2);

    const x = trackedElementPosition.x - halfWidth;
    const y = trackedElementPosition.y - halfHeight;

    return frame.composite(pasteImage, x + xAdj, y + yAdj);
}

function createGif(payload) {
    return new Promise((resolve, reject) => {
        gifshot.createGIF(payload,(obj) => {
            resolve(obj.image);
        }, (errorResponse) => {
            reject(errorResponse)
        });
    });
}

export async function makeGif(baseGifUrl, inputTrackedElements, imageData) {
    const baseGifJimpFramePromises = await gifUrlToJimpFrames(baseGifUrl);
    const baseGifJimpFrames = await Promise.all(baseGifJimpFramePromises);
    const frames = [];
    baseGifJimpFrames.forEach((baseGifJimpFrame, frameIdx) => {
        inputTrackedElements.forEach(trackedElement => {
            const trackedElementPosition = imageData.get_tracked_element_position(trackedElement.id, frameIdx);
            const adjustment = imageData.get_tracked_element_adjustment(trackedElement.id);
            let trackedElementImage = trackedElement.image_file.clone().resize(Jimp.AUTO, trackedElementPosition.height + (adjustment.height || 0))
            frames.push(composite(trackedElementPosition, baseGifJimpFrame, trackedElementImage, adjustment.x || 0, adjustment.y || 0))
        });
    });

    const base64Frames = [];

    frames.forEach(frame => frame.getBase64(Jimp.AUTO, (err, res) => {
        base64Frames.push(res);
    }));

    const gif = await createGif({
        'images': base64Frames,
        'gifWidth': frames[0].bitmap.width,
        'gifHeight': frames[0].bitmap.height,
        'frameDuration': 0.1,
    });

    return gif;
}
