import {
    ImageData,
    TrackedElement,
    FrameData,
    TrackedElementPosition,
} from './imageData';

const vince = new TrackedElement(1);
const tracked_elements = [vince];

const frames_data = [
    new FrameData(0, [new TrackedElementPosition(vince.id,125, 85, null, null, 18)]),
    new FrameData(1, [new TrackedElementPosition(vince.id,126, 82, null, null, 21)]),
    new FrameData(2, [new TrackedElementPosition(vince.id,129, 80, null, null, 23)]),
    new FrameData(3, [new TrackedElementPosition(vince.id,129, 78, null, null, 24)]),
    new FrameData(4, [new TrackedElementPosition(vince.id,130, 74, null, null, 25)]),
    new FrameData(5, [new TrackedElementPosition(vince.id,129, 68, null, null, 26)]),
    new FrameData(6, [new TrackedElementPosition(vince.id,127, 63, null, null, 27)]),
    new FrameData(7, [new TrackedElementPosition(vince.id,126, 60, null, null, 28)]),
    new FrameData(8, [new TrackedElementPosition(vince.id,125, 58, null, null, 29)]),
    new FrameData(9, [new TrackedElementPosition(vince.id,124, 58, null, null, 32)]),
    new FrameData(10, [new TrackedElementPosition(vince.id,118, 55, null, null, 34)]),
    new FrameData(11, [new TrackedElementPosition(vince.id,112, 55, null, null, 37)]),
    new FrameData(12, [new TrackedElementPosition(vince.id,111, 52, null, null, 40)]),
    new FrameData(13, [new TrackedElementPosition(vince.id,111, 47, null, null, 43)]),
    new FrameData(14, [new TrackedElementPosition(vince.id,116, 43, null, null, 43)]),
    new FrameData(15, [new TrackedElementPosition(vince.id,119, 43, null, null, 44)]),
    new FrameData(16, [new TrackedElementPosition(vince.id,122, 46, null, null, 44)]),
    new FrameData(17, [new TrackedElementPosition(vince.id,126, 51, null, null, 47)]),
    new FrameData(18, [new TrackedElementPosition(vince.id,135, 54, null, null, 51)]),
    new FrameData(19, [new TrackedElementPosition(vince.id,149, 52, null, null, 53)]),
    new FrameData(20, [new TrackedElementPosition(vince.id,155, 51, null, null, 56)]),
    new FrameData(21, [new TrackedElementPosition(vince.id,155, 45, null, null, 57)]),
    new FrameData(22, [new TrackedElementPosition(vince.id,152, 39, null, null, 57)]),
    new FrameData(23, [new TrackedElementPosition(vince.id,151, 35, null, null, 56)]),
    new FrameData(24, [new TrackedElementPosition(vince.id,151, 37, null, null, 54)]),
    new FrameData(25, [new TrackedElementPosition(vince.id,149, 43, null, null, 57)]),
    new FrameData(26, [new TrackedElementPosition(vince.id,142, 48, null, null, 57)]),
    new FrameData(27, [new TrackedElementPosition(vince.id,128, 47, null, null, 58)]),
    new FrameData(28, [new TrackedElementPosition(vince.id,116, 48, null, null, 60)]),
    new FrameData(29, [new TrackedElementPosition(vince.id,112, 45, null, null, 60)]),
    new FrameData(30, [new TrackedElementPosition(vince.id,116, 39, null, null, 58)]),
    new FrameData(31, [new TrackedElementPosition(vince.id,121, 37, null, null, 55)]),
    new FrameData(32, [new TrackedElementPosition(vince.id,122, 39, null, null, 55)]),
    new FrameData(33, [new TrackedElementPosition(vince.id,118, 44, null, null, 57)]),
];

const adjustments = [
    new TrackedElementPosition(vince.id, null, null, null, null, 30)
];

const strut = new ImageData(
    'strut',
    'pics/strut.gif',
    frames_data,
    tracked_elements,
    adjustments,
    null,
);

export default strut;