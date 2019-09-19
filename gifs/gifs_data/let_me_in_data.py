from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

conan = TrackedElement(id=1)
tracked_elements = [conan]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=268, y=109, height=186)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=269, y=111, height=186)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=271, y=124, height=186)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=270, y=136, height=189)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=266, y=130, height=190)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=270, y=129, height=200)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=266, y=131, height=209)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=273, y=132, height=215)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=283, y=129, height=223)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=290, y=121, height=225)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=298, y=117, height=230)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=303, y=111, height=235)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=304, y=109, height=240)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=304, y=103, height=245)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=303, y=94, height=250)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=303, y=96, height=255)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=conan.id, x=292, y=98, height=260)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=conan.id, height=30, x=15, y=10)
]

let_me_in = ImageData(
    type='let_me_in',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/conan.gif',
    foreground_image_path='pics/mask.gif',
    foreground_indicies=list(range(len(frames_data))),
    adjustments=adjustments,
)

