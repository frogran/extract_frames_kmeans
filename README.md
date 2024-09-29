### README: Extracting Diverse Frames from Video Using K-Means Clustering

This script extracts a set of diverse frames from a video by clustering similar frames using K-Means and selecting representative frames from each cluster. It's useful when you want a concise summary of a video's content without manually reviewing every frame.

#### Features:
- Extracts frames evenly spaced from the video.
- Clusters frames based on visual similarity using K-Means.
- Saves a representative frame from each cluster.

#### Usage:
1. **Prerequisites**: Ensure you have the necessary libraries installed:
   ```bash
   pip install numpy opencv-python scikit-learn
   ```

2. **Command Line Usage**:
   The script can be run from the command line. It requires the video file path and an output directory where the frames will be saved.

   ```bash
   python extract_frames.py <video_path> <output_dir> --n_frames <number_of_frames> --num_extracted_frames <total_frames_to_sample>
   ```

   - `video_path`: Path to the input video.
   - `output_dir`: Directory where the extracted frames will be saved.
   - `--n_frames`: (Optional) Number of diverse frames to extract (default: 10).
   - `--num_extracted_frames`: (Optional) Number of frames to extract from the video for clustering (default: 100).

3. **Explanation of Parameters**:
   - `--n_frames`: This controls **how many diverse frames** you want as the final output. These frames are selected from different clusters. For example, if you set `--n_frames 10`, the script will output 10 diverse frames.
   
   - `--num_extracted_frames`: This controls **how many frames are initially extracted** from the video for clustering. The more frames you extract, the better the clustering process will be at finding diversity. For example, setting `--num_extracted_frames 100` means the script will extract 100 frames evenly spaced from the video for the clustering process. Note that the value for `--num_extracted_frames` should be larger than `--n_frames` to allow the clustering algorithm to find distinct frames.

4. **Example Calculations of Total Number of Frames**:

   - **Single Video Example**:
     Suppose you have a video that is 5 minutes long (300 seconds) and the frame rate is 30 frames per second (FPS). This video would contain:
     ```plaintext
     Total frames in the video = 300 seconds * 30 FPS = 9000 frames
     ```

     If you set `--num_extracted_frames 100`, the script will extract 100 frames from the 9000 available frames. Then, if you set `--n_frames 10`, it will select 10 diverse frames from the extracted 100 using K-Means clustering.

   - **Multiple Videos Example**:
     If you have 3 videos, each 2 minutes long, with a frame rate of 25 FPS, then the total number of frames per video is:
     ```plaintext
     Total frames per video = 120 seconds * 25 FPS = 3000 frames
     ```

     For 3 videos, the total frame count is:
     ```plaintext
     Total frames for all videos = 3 * 3000 = 9000 frames
     ```

     If you set `--num_extracted_frames 100` and `--n_frames 5` for each video, the script will:
     - Extract 100 frames from each video.
     - Cluster those frames and select 5 diverse frames from each video.

     The result will be 15 diverse frames (5 frames from each of the 3 videos).

5. **Example**:
   ```bash
   python extract_frames.py sample_video.mp4 output_frames/ --n_frames 8 --num_extracted_frames 120
   ```

   This command will extract 120 frames from `sample_video.mp4`, cluster them, and save 8 representative frames in the `output_frames/` directory.

#### How It Works:
- **Frame Extraction**: A set number of frames are extracted from the video, evenly spaced across its duration.
- **Feature Computation**: Each frame is resized and flattened to create a feature vector.
- **K-Means Clustering**: Frames are grouped into clusters based on their visual features.
- **Representative Frame Selection**: One frame from each cluster is chosen as the most representative.
- **Saving Frames**: The selected frames are saved as JPEG images in the specified directory.

#### License:
Feel free to modify and use the script for your personal or project needs.
