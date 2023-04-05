from deepface import DeepFace
import realtime
import arduino

def stream(
    db_path="C:\\Users\\jacks\\OneDrive\\Documents\\Hacklahoma\\FaceID\\database",
    model_name="Facenet",
    detector_backend="opencv",
    distance_metric="cosine",
    enable_face_analysis=True,
    source=0,
    time_threshold=10,
    frame_threshold=5,
):

    """
    This function applies real time face recognition and facial attribute analysis
    Parameters:
            db_path (string): facial database path. You should store some .jpg files in this folder.
            model_name (string): VGG-Face, Facenet, Facenet512, OpenFace, DeepFace, DeepID, Dlib,
            ArcFace, SFace
            detector_backend (string): opencv, retinaface, mtcnn, ssd, dlib or mediapipe
            distance_metric (string): cosine, euclidean, euclidean_l2
            enable_facial_analysis (boolean): Set this to False to just run face recognition
            source: Set this to 0 for access web cam. Otherwise, pass exact video path.
            time_threshold (int): how many second analyzed image will be displayed
            frame_threshold (int): how many frames required to focus on face
    """

    if time_threshold < 1:
        raise ValueError(
            "time_threshold must be greater than the value 1 but you passed " + str(time_threshold)
        )

    if frame_threshold < 1:
        raise ValueError(
            "frame_threshold must be greater than the value 1 but you passed "
            + str(frame_threshold)
        )

    realtime.analysis(
        db_path,
        model_name,
        detector_backend,
        distance_metric,
        enable_face_analysis,
        source=source,
        time_threshold=time_threshold,
        frame_threshold=frame_threshold,
    )