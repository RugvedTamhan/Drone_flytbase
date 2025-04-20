import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_paths(primary, others, conflict_info=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    wp = primary["waypoints"]
    x = [pt["x"] for pt in wp]
    y = [pt["y"] for pt in wp]
    z = [pt["z"] for pt in wp]
    ax.plot(x, y, z, label="Primary Drone", color='blue', marker='o')

    for drone in others:
        wp = drone["waypoints"]
        x = [pt["x"] for pt in wp]
        y = [pt["y"] for pt in wp]
        z = [pt["z"] for pt in wp]
        ax.plot(x, y, z, label=f"{drone['id']}", color='gray', linestyle='--')

    # Plot conflict point if any
    if conflict_info and conflict_info["status"] == "conflict":
        c = conflict_info["location"]
        ax.scatter(c["x"], c["y"], c["z"], color='red', s=100, label="Conflict Point")

    ax.set_title("3D Drone Flight Paths")
    ax.set_xlabel("X (meters)")
    ax.set_ylabel("Y (meters)")
    ax.set_zlabel("Z (altitude)")
    plt.show()
