import {
    ImageData,
    TrackedElement,
    FrameData,
    TrackedElementPosition,
} from './imageData';


const guy = new TrackedElement(1);

const tracked_elements = [guy];

const frames_data = [
    new FrameData(0, [new TrackedElementPosition(guy.id, 295, 143, null, null, 196)]),
    new FrameData(1, [new TrackedElementPosition(guy.id, 292, 142, null, null, 196)]),
    new FrameData(2, [new TrackedElementPosition(guy.id, 292, 142, null, null, 196)]),
    new FrameData(3, [new TrackedElementPosition(guy.id, 293, 141, null, null, 196)]),
    new FrameData(4, [new TrackedElementPosition(guy.id, 292, 142, null, null, 196)]),
    new FrameData(5, [new TrackedElementPosition(guy.id, 294, 143, null, null, 196)]),
    new FrameData(6, [new TrackedElementPosition(guy.id, 296, 141, null, null, 196)]),
    new FrameData(7, [new TrackedElementPosition(guy.id, 294, 139, null, null, 196)]),
    new FrameData(8, [new TrackedElementPosition(guy.id, 296, 141, null, null, 196)]),
    new FrameData(9, [new TrackedElementPosition(guy.id, 297, 139, null, null, 196)]),
    new FrameData(10, [new TrackedElementPosition(guy.id, 298, 140, null, null, 196)]),
    new FrameData(11, [new TrackedElementPosition(guy.id, 298, 141, null, null, 196)]),
    new FrameData(12, [new TrackedElementPosition(guy.id, 298, 142, null, null, 196)]),
    new FrameData(13, [new TrackedElementPosition(guy.id, 296, 142, null, null, 196)]),
    new FrameData(14, [new TrackedElementPosition(guy.id, 293, 140, null, null, 196)]),
];

const adjustments = [
    new TrackedElementPosition(guy.id, null, null, null, null, 30)
];

const clapping = new ImageData(
    'clapping',
    'pics/clapping.gif',
    frames_data,
    tracked_elements,
    adjustments,
    'pics/clapping_mask.gif',
);

export default clapping;