import numpy as np
from stl import mesh
from scipy.spatial import distance

def load_mesh(filepath, sample_size=None):
    # STLファイルを読み込み、メッシュの頂点を取得
    stl_mesh = mesh.Mesh.from_file(filepath)
    points = np.vstack((stl_mesh.v0, stl_mesh.v1, stl_mesh.v2)).astype(np.float32)
    
    # サンプリング
    if sample_size and len(points) > sample_size:
        indices = np.random.choice(len(points), sample_size, replace=False)
        points = points[indices]
        
    return points

def hausdorff_distance_chunked(points1, points2, chunk_size=1000):
    max_min_distances = []

    # points1のチャンクごとにpoints2との最小距離を計算
    for i in range(0, len(points1), chunk_size):
        print(f'Processing chunk {i} of {len(points1)}')
        chunk1 = points1[i:i + chunk_size]
        d1 = distance.cdist(chunk1, points2, 'euclidean')
        max_min_distances.append(np.max(np.min(d1, axis=1)))

    # points2のチャンクごとにpoints1との最小距離を計算
    for i in range(0, len(points2), chunk_size):
        print(f'Processing chunk {i} of {len(points2)}')
        chunk2 = points2[i:i + chunk_size]
        d2 = distance.cdist(chunk2, points1, 'euclidean')
        max_min_distances.append(np.max(np.min(d2, axis=1)))

    # Hausdorff距離を返す
    return max(max_min_distances)

if __name__ == "__main__":
    # STLファイルからメッシュを読み込み（必要ならサンプリングを指定）
    points1 = load_mesh('l_raw.stl', sample_size=None)
    points2 = load_mesh('l_rescan1.stl', sample_size=None)

    # チャンク処理によるHausdorff距離の計算
    dist = hausdorff_distance_chunked(points1, points2)
    print(f'Hausdorff Distance: {dist}')
