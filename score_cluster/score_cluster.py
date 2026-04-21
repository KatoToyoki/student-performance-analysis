import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATA_PATH = "data/StudentPerformanceFactors.csv"
OUTPUT_PATH = "score_cluster/score_cluster_output.csv"
FEATURES = ["Previous_Scores", "Exam_Score"]
N_CLUSTERS = 3
RANDOM_STATE = 42

df = pd.read_csv(DATA_PATH)

scaler = StandardScaler()
X = scaler.fit_transform(df[FEATURES])

kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=RANDOM_STATE, n_init=10)
df["cluster_id"] = kmeans.fit_predict(X)

# Map cluster_id to label by mean Exam_Score rank (Low < Mid < High)
cluster_means = df.groupby("cluster_id")["Exam_Score"].mean().sort_values()
label_map = {cid: label for cid, label in zip(cluster_means.index, ["Low", "Mid", "High"])}
df["Score_Cluster"] = df["cluster_id"].map(label_map)

output = df[FEATURES + ["Score_Cluster"]]
output.index.name = "Student_ID"
output.to_csv(OUTPUT_PATH, index=True)

print(f"Saved {len(output)} rows to {OUTPUT_PATH}")
print(output["Score_Cluster"].value_counts().sort_index())
