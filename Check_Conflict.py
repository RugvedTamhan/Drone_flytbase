def interpolate_paths(wp1, wp2, t):
    t1, t2 = wp1["t"], wp2["t"]
    ratio = (t - t1)/(t2 - t1)
    x = wp1["x"] + ratio * (wp2["x"] - wp1["x"])
    y = wp1["y"] + ratio * (wp2["y"] - wp1["y"])
    z = wp1["z"] + ratio * (wp2["z"] - wp1["z"])
    return {"x": float(x), "y": float(y), "z": float(z)}

def get_position(waypoints, t):
    for i in range(len(waypoints) - 1):
            if waypoints[i]["t"] <= t <= waypoints[i+1]["t"]:
                return interpolate_paths(waypoints[i], waypoints[i+1], t)
    return None

def distance_drone(p1, p2):
    return((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2 + (p1["z"] - p2["z"])**2)**0.5

def classify_conflict(pos1, pos2, t1, t2, distance, safe_distance=2.5):
    xy_distance = ((pos1["x"] - pos2["x"])**2 + (pos1["y"] - pos2["y"])**2) ** 0.5
    z_distance = abs(pos1["z"] - pos2["z"])
    same_time = t1 == t2
    close_xy = xy_distance < safe_distance
    close_z = z_distance < 1.5

    if same_time and close_xy and close_z:
        return "4D"
    elif same_time and close_xy and not close_z:
        return "Altitude-only"
    elif same_time and not close_xy:
        return "Time-only"
    elif not same_time and close_xy and close_z:
        return "Spatial-only"
    else:
        return "Unknown"

def check_conflict(primary, others, safe_distance=2.5):
    start = primary["start_time"]
    end = primary["end_time"]
    wp_primary = primary["waypoints"]

    for t in range(start, end + 1):
        pos_primary = get_position(wp_primary, t)
        if not pos_primary:
            continue

        for other in others:
            if other["start_time"] <= t <= other["end_time"]:
                pos_other = get_position(other["waypoints"], t)
                if not pos_other:
                    continue

                dist = distance_drone(pos_primary, pos_other)
                if dist < safe_distance:
                    conflict_type = classify_conflict(pos_primary, pos_other, t, t, dist, safe_distance)
                    return {
                        "status": "conflict",
                        "time": t,
                        "distance": round(dist, 2),
                        "location": pos_primary,
                        "with": other["id"],
                        "type": conflict_type
                    }

    return {"status": "clear"}


