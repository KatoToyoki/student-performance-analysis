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

**Step 2 - Attitude Cluster** *(requires Step 1 output)*

```
python attitude_cluster/attitude_cluster.py
```

- Clusters students based on `Hours_Studied`, `Attendance`, `Motivation_Level`, `Tutoring_Sessions`
- Each student will be labeled as **Expanding Opportunities / Growing Opportunities / Abundant Opportunities**
- Joins with `score_cluster_output.csv` via `Student_ID` to compare attitude cluster against Score Cluster
- Analyzes and concludes whether attitude factors affect a student's exam score
- Generates `attitude_cluster/attitude_cluster_output.csv`

**Step 3 - Inconvenience Cluster** *(requires Step 1 output)*

```
python inconvenience_cluster/inconvenience_cluster.py
```

- Clusters students based on `Access_to_Resources`, `Internet_Access`, `Teacher_Quality`, `Distance_from_Home`
- Each student will be labeled as **Inconvenience / Normal / Convenience**
- Joins with `score_cluster_output.csv` via `Student_ID` to compare inconvenience cluster against Score Cluster
- Analyzes and concludes whether inconvenience conditions affect a student's exam score
- Generates `inconvenience_cluster/inconvenience_cluster_output.csv`

**Step 4 - Cross Analysis** *(requires Step 1, 2, 3 outputs)*

```
python cross_analysis/cross_analysis.py
```

- Combines Step 2 and Step 3 outputs with Score Cluster
- Compares attitude vs inconvenience impact on exam score across all cluster combinations:
  - 🟢 Abundant Opportunities × 🔴 Inconvenience → good attitude but poor conditions
  - 🔴 Expanding Opportunities × 🟢 Convenience → poor attitude but good conditions
  - 🟢 Abundant Opportunities × 🟢 Convenience → good attitude and good conditions
  - 🔴 Expanding Opportunities × 🔴 Inconvenience → poor attitude and poor conditions
- Key questions answered:
  - Does good attitude overcome poor conditions, or vice versa?
  - Which factor — attitude or external conditions — has a greater impact on exam score?
- Generates `cross_analysis/cross_analysis_output.csv`

---

## Analysis Result

| File                               | Content                                          |
| ---------------------------------- | ------------------------------------------------ |
| `score_cluster_output.csv`         | Score cluster of students                        |
| `attitude_cluster_output.csv`      | Attitude cluster of students                     |
| `inconvenience_cluster_output.csv` | Inconvenience cluster of students                |
| `cross_analysis_output.csv`        | Final analysis that combined with three clusters |
