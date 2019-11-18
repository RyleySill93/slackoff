from gifs.gifs_data import types
from ..models import TrackedElement, TrackedElementPosition, FrameData, TrackedElementAdjustment, ImageData


def load_gifs():
    for gif_type in types:
        image_data = ImageData.objects.create(
            type=gif_type.image_data.type,
            background_image_path=gif_type.image_data.background_image_path,
            foreground_image_path=gif_type.image_data.foreground_image_path,
        )

        tes = []
        for tracked_element in gif_type.tracked_elements:
            te = TrackedElement(
                image_data=image_data,
                index=tracked_element.id - 1,
            )
            tes.append(te)

        tes = TrackedElement.objects.bulk_create(tes)

        for frame_data in gif_type.frames_data:
            fd = FrameData.objects.create(
                index=frame_data.index,
                image_data=image_data,
                has_foreground=frame_data.index in gif_type.image_data.foreground_indicies,
            )

            teps = []
            for tracked_element_position in frame_data.tracked_element_positions:
                tep = TrackedElementPosition(
                    frame_data=fd,
                    tracked_element=[te for te in tes if tracked_element_position.tracked_element_id == te.index + 1][0],
                    x=tracked_element_position.x,
                    y=tracked_element_position.y,
                    z=tracked_element_position.z,
                    width=tracked_element_position.width,
                    height=tracked_element_position.height,
                    rotation=tracked_element_position.rotation,
                    brightness=tracked_element_position.brightness,
                )
                teps.append(tep)
            TrackedElementPosition.objects.bulk_create(teps)

        for adjustment in gif_type.adjustments:
            TrackedElementAdjustment.objects.create(
                tracked_element_id=[te for te in tes if adjustment.tracked_element_id == te.index + 1][0].id,
                x=adjustment.x,
                y=adjustment.y,
                z=adjustment.z,
                width=adjustment.width,
                height=adjustment.height,
                rotation=adjustment.rotation,
                brightness=adjustment.brightness,
            )

