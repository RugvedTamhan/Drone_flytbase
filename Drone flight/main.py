from Load_Data import load_path
from Check_Conflict import check_conflict
from Visualizer import plot_paths

primary, others = load_path()
result = check_conflict(primary, others)

print(result)
plot_paths(primary, others, result)
