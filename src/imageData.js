export class ImageData {
    constructor(
        type,
        background_image_path,
        frames_data,
        tracked_elements,
        adjustments,
        foreground_image_path=null,
        foreground_indicies=null,
    ) {
        this.type = type
        this.background_image_path = background_image_path
        this.frames_data = frames_data
        this.tracked_elements = tracked_elements
        this.adjustments = adjustments
        this.foreground_image_path = foreground_image_path
        this.foreground_indicies = foreground_indicies || new Array(frames_data.length)
    }

    get_frame(frame_index) {
        let result = null;
        this.frames_data.forEach(frame => {
            if (frame.index === frame_index) {
                result = frame;
            }
        });

        return result;
    }

    get_tracked_element_position(tracked_element_id, frame_index) {
        const frame = this.get_frame(frame_index);

        if (!frame) return null;

        let result = null;

        frame.tracked_element_positions.forEach(tracked_element_position => {
            if (tracked_element_position.tracked_element_id === tracked_element_id) {
                result = tracked_element_position
            }
        });

        if (!result) {
            throw `tracked element position not found: id: ${tracked_element_id} - frame index: ${frame_index}`
        }

        return result;
    }

    get_tracked_element_adjustment(tracked_element_id) {
        let result = null;
        this.adjustments.forEach(adjustment => {
            if (adjustment.tracked_element_id === tracked_element_id) {
                result = adjustment
            }
        });

        return result
    }
}

export class FrameData {
    constructor(index, tracked_element_positions) {
        this.index = index
        this.tracked_element_positions = tracked_element_positions
    }
}

export class TrackedElement {
    constructor(id, image_file=null, text=null) {
        this.id = id
        this.image_file = image_file
        this.text = text
    }
}

export class TrackedElementPosition {
    constructor(
        tracked_element_id,
        x=null,
        y=null,
        z=null,
        width=null,
        height=null,
        rotation=null,
        brightness=null,
    ) {
        this.tracked_element_id = tracked_element_id
        this.x = x
        this.y = y
        this.z = z
        this.width = width
        this.height = height
        this.rotation = rotation
        this.brightness = brightness
    }
}
