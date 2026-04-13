# Student Performance Analysis

## Project Introduction

This project analyzes student performance factors using clustering techniques.
We explore whether **attitude** and **inconvenience conditions** affect a student's exam score.

---

## Project Structure

```
.
├── README.md
├── requirements.txt
├── data/
│   └── StudentPerformanceFactors.csv
├── score_cluster/
│   ├── score_cluster.py
│   └── score_cluster_output.csv
├── attitude_cluster/
│   ├── attitude_cluster.py
│   └── attitude_cluster_output.csv
├── inconvenience_cluster/
│   ├── inconvenience_cluster.py
│   └── inconvenience_cluster_output.csv
└── cross_analysis/
    ├── cross_analysis.py
    └── cross_analysis_output.csv
```

---

## Environment Setup

```
pip install -r requirements.txt
```

---

## Execution Order

⚠️ Please follow the order below. `cross_analysis.py` requires the previous three outputs to run.

**Step 1 - Score Cluster**

```
python score_cluster/score_cluster.py
```

- Clusters students based on `Previous_Scores` and `Exam_Score`
- Generates `score_cluster/score_cluster_output.csv`
- Each student will be labeled as Low / Mid / High Score

**Step 2 - Attitude Cluster**

```
python attitude_cluster/attitude_cluster.py
```

- Clusters students based on `Hours_Studied`, `Attendance`, `Motivation_Level`, `Tutoring_Sessions`
- Generates `attitude_cluster/attitude_cluster_output.csv`
- Each student will be labeled as Expanding / Growing / Abundant Opportunities

**Step 3 - Inconvenience Cluster**

```
python inconvenience_cluster/inconvenience_cluster.py
```

- Clusters students based on `Access_to_Resources`, `Internet_Access`, `Teacher_Quality`, `Distance_from_Home`
- Generates `inconvenience_cluster/inconvenience_cluster_output.csv`
- Each student will be labeled as Inconvenience / Normal / Convenience

**Step 4 - Cross Analysis**

```
python cross_analysis/cross_analysis.py
```

- Combines the previous three outputs
- Compares the impact of attitude and inconvenience conditions on `Exam_Score`
- Generates `cross_analysis/cross_analysis_output.csv`

---

## Analysis Result

| File                               | Content                                          |
| ---------------------------------- | ------------------------------------------------ |
| `score_cluster_output.csv`         | Score cluster of students                        |
| `attitude_cluster_output.csv`      | Attitude cluster of students                     |
| `inconvenience_cluster_output.csv` | Inconvenience cluster of students                |
| `cross_analysis_output.csv`        | Final analysis that combined with three clusters |
