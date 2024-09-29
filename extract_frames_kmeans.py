import argparse
import cv2
import numpy as np
from sklearn.cluster import KMeans
import os

def extract_frames_from_video(video_path, num_frames=100):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []
    
    for i in range(num_frames):
        frame_id = int(total_frames / num_frames * i)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
        else:
            break
    cap.release()
    return frames

def compute_frame_features(frames):
    features = []
    for frame in frames:
        small_frame = cv2.resize(frame, (64, 64))
        feature_vector = small_frame.flatten()
        features.append(feature_vector)
    return np.array(features)

def kmeans_cluster_frames(features, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features)
    return kmeans.labels_

def select_representative_frames(frames, labels):
    unique_labels = np.unique(labels)
    representative_frames = []
    
    for label in unique_labels:
        cluster_indices = np.where(labels == label)[0]
        representative_index = cluster_indices[0]
        representative_frames.append(frames[representative_index])
    
    return representative_frames

def save_frames(frames, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, frame in enumerate(frames):
        frame_path = os.path.join(output_dir, f'frame_{i}.jpg')
        cv2.imwrite(frame_path, frame)

def export_diverse_frames(video_path, output_dir, n_frames=10, num_extracted_frames=100):
    frames = extract_frames_from_video(video_path, num_extracted_frames)
    features = compute_frame_features(frames)
    labels = kmeans_cluster_frames(features, n_frames)
    representative_frames = select_representative_frames(frames, labels)
    save_frames(representative_frames, output_dir)

def main():
    parser = argparse.ArgumentParser(description='Export a diverse set of frames from a video using k-means clustering.')
    parser.add_argument('video_path', type=str, help='Path to the input video file')
    parser.add_argument('output_dir', type=str, help='Directory to save the output frames')
    parser.add_argument('--n_frames', type=int, default=10, help='Number of diverse frames to extract')
    parser.add_argument('--num_extracted_frames', type=int, default=100, help='Number of frames to extract from the video for clustering')
    
    args = parser.parse_args()
    
    export_diverse_frames(args.video_path, args.output_dir, args.n_frames, args.num_extracted_frames)

if __name__ == '__main__':
    main()
