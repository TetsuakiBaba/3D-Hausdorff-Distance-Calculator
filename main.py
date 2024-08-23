import numpy as np
from stl import mesh
from scipy.spatial import distance

def load_mesh(filepath):
    # STLファイルを読み込み、メッシュの頂点を取得
    stl_mesh = mesh.Mesh.from_file(filepath)
    points = np.vstack((stl_mesh.v0, stl_mesh.v1, stl_mesh.v2))
    return points

def hausdorff_distance(points1, points2):
    # 各点セット間の最短距離を計算
    d1 = distance.cdist(points1, points2, 'euclidean')
    d2 = distance.cdist(points2, points1, 'euclidean')
    hausdorff_dist = max(np.max(np.min(d1, axis=1)), np.max(np.min(d2, axis=1)))
    return hausdorff_dist

if __name__ == "__main__":
    # STLファイルからメッシュを読み込み
    points1 = load_mesh('cube.stl')
    points2 = load_mesh('cube.stl')

    # Hausdorff距離を計算
    dist = hausdorff_distance(points1, points2)
    print(f'Hausdorff Distance : {dist}')
    
