# extract_frames_kmeans

Extracting Diverse Frames from Video Using K-Means Clustering

This script extracts a set of diverse frames from a video by clustering similar frames using K-Means and selecting representative frames from each cluster. It's useful when you want a concise summary of a video's content without manually reviewing every frame.
Features:

    Extracts frames evenly spaced from the video.
    Clusters frames based on visual similarity using K-Means.
    Saves a representative frame from each cluster.

Usage:

    Prerequisites: Ensure you have the necessary libraries installed:

    bash

pip install numpy opencv-python scikit-learn

Command Line Usage: The script can be run from the command line. It requires the video file path and an output directory where the frames will be saved.

bash

python extract_frames.py <video_path> <output_dir> --n_frames <number_of_frames> --num_extracted_frames <total_frames_to_sample>

    video_path: Path to the input video.
    output_dir: Directory where the extracted frames will be saved.
    --n_frames: (Optional) Number of diverse frames to extract (default: 10).
    --num_extracted_frames: (Optional) Number of frames to extract from the video for clustering (default: 100).

Example:

bash

    python extract_frames.py sample_video.mp4 output_frames/ --n_frames 8 --num_extracted_frames 120

    This command will extract 120 frames from sample_video.mp4, cluster them, and save 8 representative frames in the output_frames/ directory.

How It Works:

    Frame Extraction: A set number of frames are extracted from the video, evenly spaced across its duration.
    Feature Computation: Each frame is resized and flattened to create a feature vector.
    K-Means Clustering: Frames are grouped into clusters based on their visual features.
    Representative Frame Selection: One frame from each cluster is chosen as the most representative.
    Saving Frames: The selected frames are saved as JPEG images in the specified directory.

License:

Feel free to modify and use the script for your personal or project needs.
