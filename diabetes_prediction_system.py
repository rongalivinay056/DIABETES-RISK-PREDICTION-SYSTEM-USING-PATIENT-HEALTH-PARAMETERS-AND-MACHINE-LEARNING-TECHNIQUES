"""
Diabetes Risk Prediction System
Predicts diabetes risk using patient health parameters with machine learning
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve, auc
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

def generate_diabetes_dataset(n_samples=1000, random_state=42):
    """Generate synthetic diabetes dataset with patient health parameters"""
    np.random.seed(random_state)
    
    data = {
        'Patient_ID': [f'PAT{i:06d}' for i in range(n_samples)],
        'Age': np.random.randint(20, 80, n_samples),
        'Glucose_Level': np.random.normal(120, 35, n_samples),
        'Blood_Pressure_Systolic': np.random.normal(130, 20, n_samples),
        'Blood_Pressure_Diastolic': np.random.normal(80, 12, n_samples),
        'BMI': np.random.normal(28, 6, n_samples),
        'Insulin_Level': np.random.normal(80, 40, n_samples),
        'Skin_Thickness': np.random.normal(25, 10, n_samples),
        'Pregnancy_Count': np.random.randint(0, 10, n_samples),
        'Family_History': np.random.choice([0, 1], n_samples, p=[0.6, 0.4]),
        'Smoking_Status': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
        'Physical_Activity_hours': np.random.uniform(0, 10, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Generate diabetes risk based on health parameters
    # Risk calculation
    risk_score = (
        (df['Glucose_Level'] - 100) / 50 +
        (df['BMI'] - 25) / 5 +
        (df['Age'] - 40) / 20 +
        (df['Blood_Pressure_Systolic'] - 120) / 30 +
        (df['Insulin_Level'] - 70) / 50
    )
    
    # Add family history impact
    risk_score += df['Family_History'] * 1.5
    
    # Add smoking impact
    risk_score += df['Smoking_Status'] * 1.0
    
    # Reduce risk for physical activity
    risk_score -= (df['Physical_Activity_hours'] / 10) * 0.8
    
    # Add noise
    risk_score += np.random.normal(0, 0.5, n_samples)
    
    # Convert to binary classification (0: No Diabetes, 1: Diabetes Risk)
    threshold = np.percentile(risk_score, 35)
    df['Diabetes_Risk'] = (risk_score > threshold).astype(int)
    
    # Ensure realistic value ranges
    df['Glucose_Level'] = np.clip(df['Glucose_Level'], 50, 250)
    df['Blood_Pressure_Systolic'] = np.clip(df['Blood_Pressure_Systolic'], 80, 200)
    df['Blood_Pressure_Diastolic'] = np.clip(df['Blood_Pressure_Diastolic'], 40, 120)
    df['BMI'] = np.clip(df['BMI'], 15, 50)
    df['Insulin_Level'] = np.clip(df['Insulin_Level'], 10, 300)
    df['Skin_Thickness'] = np.clip(df['Skin_Thickness'], 0, 100)
    
    return df

def preprocess_data(df):
    """Preprocess the dataset for modeling"""
    df_processed = df.copy()
    
    # Select features for modeling
    feature_cols = [
        'Age', 'Glucose_Level', 'Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic',
        'BMI', 'Insulin_Level', 'Skin_Thickness', 'Pregnancy_Count',
        'Family_History', 'Smoking_Status', 'Physical_Activity_hours'
    ]
    
    return df_processed, feature_cols

def train_models(X_train, X_test, y_train, y_test):
    """Train multiple classification models"""
    models = {}
    results = {}
    
    # Model 1: Logistic Regression
    print("Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    y_proba_lr = lr_model.predict_proba(X_test)[:, 1]
    
    models['Logistic Regression'] = lr_model
    results['Logistic Regression'] = {
        'predictions': y_pred_lr,
        'probabilities': y_proba_lr,
        'accuracy': accuracy_score(y_test, y_pred_lr),
        'precision': precision_score(y_test, y_pred_lr),
        'recall': recall_score(y_test, y_pred_lr),
        'f1': f1_score(y_test, y_pred_lr),
        'roc_auc': roc_auc_score(y_test, y_proba_lr)
    }
    
    # Model 2: Random Forest Classifier
    print("Training Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    y_proba_rf = rf_model.predict_proba(X_test)[:, 1]
    
    models['Random Forest'] = rf_model
    results['Random Forest'] = {
        'predictions': y_pred_rf,
        'probabilities': y_proba_rf,
        'accuracy': accuracy_score(y_test, y_pred_rf),
        'precision': precision_score(y_test, y_pred_rf),
        'recall': recall_score(y_test, y_pred_rf),
        'f1': f1_score(y_test, y_pred_rf),
        'roc_auc': roc_auc_score(y_test, y_proba_rf)
    }
    
    # Model 3: Gradient Boosting Classifier
    print("Training Gradient Boosting Classifier...")
    gb_model = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
    gb_model.fit(X_train, y_train)
    y_pred_gb = gb_model.predict(X_test)
    y_proba_gb = gb_model.predict_proba(X_test)[:, 1]
    
    models['Gradient Boosting'] = gb_model
    results['Gradient Boosting'] = {
        'predictions': y_pred_gb,
        'probabilities': y_proba_gb,
        'accuracy': accuracy_score(y_test, y_pred_gb),
        'precision': precision_score(y_test, y_pred_gb),
        'recall': recall_score(y_test, y_pred_gb),
        'f1': f1_score(y_test, y_pred_gb),
        'roc_auc': roc_auc_score(y_test, y_proba_gb)
    }
    
    return models, results

def plot_diabetes_distribution(df):
    """Plot distribution of diabetes risk"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Count plot
    diabetes_counts = df['Diabetes_Risk'].value_counts()
    colors = ['#2ecc71', '#e74c3c']
    labels = ['No Diabetes Risk', 'Diabetes Risk']
    axes[0].bar([labels[0], labels[1]], [diabetes_counts[0], diabetes_counts[1]], 
               color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_ylabel('Number of Patients', fontsize=11, fontweight='bold')
    axes[0].set_title('Distribution of Diabetes Risk in Dataset', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    for i, v in enumerate([diabetes_counts[0], diabetes_counts[1]]):
        axes[0].text(i, v + 10, str(v), ha='center', fontweight='bold')
    
    # Pie chart
    axes[1].pie([diabetes_counts[0], diabetes_counts[1]], labels=labels, autopct='%1.1f%%',
               colors=colors, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
    axes[1].set_title('Percentage Distribution of Diabetes Risk', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/diabetes_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: diabetes_distribution.png")
    plt.close()

def plot_model_comparison(results, y_test):
    """Compare model performance metrics"""
    models = list(results.keys())
    metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    
    fig, axes = plt.subplots(1, 5, figsize=(18, 5))
    
    colors = ['#3498db', '#e74c3c', '#f39c12']
    
    for idx, metric in enumerate(metrics):
        values = [results[m][metric] for m in models]
        axes[idx].bar(models, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
        axes[idx].set_ylabel(metric.upper(), fontsize=11, fontweight='bold')
        axes[idx].set_title(f'{metric.upper()}', fontsize=12, fontweight='bold')
        axes[idx].set_ylim([0, 1])
        axes[idx].grid(axis='y', alpha=0.3)
        for i, v in enumerate(values):
            axes[idx].text(i, v + 0.02, f'{v:.4f}', ha='center', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/diabetes_model_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: diabetes_model_comparison.png")
    plt.close()

def plot_confusion_matrices(results, y_test):
    """Plot confusion matrices for all models"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    models = list(results.keys())
    
    for idx, model_name in enumerate(models):
        cm = confusion_matrix(y_test, results[model_name]['predictions'])
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], cbar=False,
                   xticklabels=['No Risk', 'Risk'], yticklabels=['No Risk', 'Risk'],
                   annot_kws={'fontsize': 12, 'fontweight': 'bold'})
        axes[idx].set_xlabel('Predicted', fontsize=11, fontweight='bold')
        axes[idx].set_ylabel('Actual', fontsize=11, fontweight='bold')
        axes[idx].set_title(f'{model_name}\nAccuracy: {results[model_name]["accuracy"]:.4f}', 
                          fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/diabetes_confusion_matrices.png', dpi=300, bbox_inches='tight')
    print("Saved: diabetes_confusion_matrices.png")
    plt.close()

def plot_roc_curves(results, y_test):
    """Plot ROC curves for all models"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#3498db', '#e74c3c', '#f39c12']
    
    for idx, (model_name, result) in enumerate(results.items()):
        fpr, tpr, _ = roc_curve(y_test, result['probabilities'])
        roc_auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, color=colors[idx], lw=2.5, 
               label=f'{model_name} (AUC = {roc_auc:.4f})', marker='o', markersize=4)
    
    ax.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Classifier')
    ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
    ax.set_title('ROC Curves - Diabetes Risk Prediction Models', fontsize=13, fontweight='bold')
    ax.legend(loc='lower right', fontsize=11)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/diabetes_roc_curves.png', dpi=300, bbox_inches='tight')
    print("Saved: diabetes_roc_curves.png")
    plt.close()

def plot_feature_importance(models, feature_names):
    """Plot feature importance for tree-based models"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Random Forest
    rf_importance = models['Random Forest'].feature_importances_
    rf_indices = np.argsort(rf_importance)[-10:]
    axes[0].barh(range(len(rf_indices)), rf_importance[rf_indices], 
                color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_yticks(range(len(rf_indices)))
    axes[0].set_yticklabels([feature_names[i] for i in rf_indices], fontsize=10)
    axes[0].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[0].set_title('Random Forest - Feature Importance', fontsize=12, fontweight='bold')
    axes[0].grid(axis='x', alpha=0.3)
    
    # Gradient Boosting
    gb_importance = models['Gradient Boosting'].feature_importances_
    gb_indices = np.argsort(gb_importance)[-10:]
    axes[1].barh(range(len(gb_indices)), gb_importance[gb_indices], 
                color='#f39c12', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1].set_yticks(range(len(gb_indices)))
    axes[1].set_yticklabels([feature_names[i] for i in gb_indices], fontsize=10)
    axes[1].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[1].set_title('Gradient Boosting - Feature Importance', fontsize=12, fontweight='bold')
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/diabetes_feature_importance.png', dpi=300, bbox_inches='tight')
    print("Saved: diabetes_feature_importance.png")
    plt.close()

def plot_health_parameters_analysis(df):
    """Plot analysis of key health parameters"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Glucose level by diabetes risk
    df_no_risk = df[df['Diabetes_Risk'] == 0]['Glucose_Level']
    df_risk = df[df['Diabetes_Risk'] == 1]['Glucose_Level']
    axes[0, 0].hist([df_no_risk, df_risk], bins=20, label=['No Risk', 'Diabetes Risk'],
                   color=['#2ecc71', '#e74c3c'], alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[0, 0].set_xlabel('Glucose Level (mg/dL)', fontsize=11, fontweight='bold')
    axes[0, 0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0, 0].set_title('Glucose Level Distribution by Diabetes Risk', fontsize=12, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(alpha=0.3)
    
    # BMI by diabetes risk
    df_no_risk_bmi = df[df['Diabetes_Risk'] == 0]['BMI']
    df_risk_bmi = df[df['Diabetes_Risk'] == 1]['BMI']
    axes[0, 1].hist([df_no_risk_bmi, df_risk_bmi], bins=20, label=['No Risk', 'Diabetes Risk'],
                   color=['#2ecc71', '#e74c3c'], alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[0, 1].set_xlabel('BMI (kg/m²)', fontsize=11, fontweight='bold')
    axes[0, 1].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0, 1].set_title('BMI Distribution by Diabetes Risk', fontsize=12, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(alpha=0.3)
    
    # Age by diabetes risk
    df_no_risk_age = df[df['Diabetes_Risk'] == 0]['Age']
    df_risk_age = df[df['Diabetes_Risk'] == 1]['Age']
    axes[1, 0].hist([df_no_risk_age, df_risk_age], bins=20, label=['No Risk', 'Diabetes Risk'],
                   color=['#2ecc71', '#e74c3c'], alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[1, 0].set_xlabel('Age (years)', fontsize=11, fontweight='bold')
    axes[1, 0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[1, 0].set_title('Age Distribution by Diabetes Risk', fontsize=12, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(alpha=0.3)
    
    # Insulin level by diabetes risk
    df_no_risk_insulin = df[df['Diabetes_Risk'] == 0]['Insulin_Level']
    df_risk_insulin = df[df['Diabetes_Risk'] == 1]['Insulin_Level']
    axes[1, 1].hist([df_no_risk_insulin, df_risk_insulin], bins=20, label=['No Risk', 'Diabetes Risk'],
                   color=['#2ecc71', '#e74c3c'], alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[1, 1].set_xlabel('Insulin Level (mIU/L)', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Insulin Level Distribution by Diabetes Risk', fontsize=12, fontweight='bold')
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/diabetes_health_parameters.png', dpi=300, bbox_inches='tight')
    print("Saved: diabetes_health_parameters.png")
    plt.close()

def main():
    print("="*80)
    print("DIABETES RISK PREDICTION SYSTEM - MACHINE LEARNING ANALYSIS")
    print("="*80)
    
    # Generate dataset
    print("\n[1] Generating synthetic diabetes dataset...")
    df = generate_diabetes_dataset(n_samples=1000)
    df.to_csv('/home/ubuntu/diabetes_data.csv', index=False)
    print(f"Dataset generated: {df.shape[0]} records")
    print(f"Diabetes Risk Cases: {(df['Diabetes_Risk'] == 1).sum()} ({(df['Diabetes_Risk'] == 1).sum()/len(df)*100:.1f}%)")
    print(f"No Risk Cases: {(df['Diabetes_Risk'] == 0).sum()} ({(df['Diabetes_Risk'] == 0).sum()/len(df)*100:.1f}%)")
    
    # Preprocess data
    print("\n[2] Preprocessing data...")
    df_processed, feature_cols = preprocess_data(df)
    
    # Prepare features and target
    X = df_processed[feature_cols]
    y = df_processed['Diabetes_Risk']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set: {X_train_scaled.shape[0]} samples, {X_train_scaled.shape[1]} features")
    print(f"Test set: {X_test_scaled.shape[0]} samples")
    
    # Train models
    print("\n[3] Training classification models...")
    models, results = train_models(X_train_scaled, X_test_scaled, y_train, y_test)
    
    # Print results
    print("\n[4] Model Performance Results:")
    print("-" * 80)
    for model_name, result in results.items():
        print(f"\n{model_name}:")
        print(f"  Accuracy:  {result['accuracy']:.6f}")
        print(f"  Precision: {result['precision']:.6f}")
        print(f"  Recall:    {result['recall']:.6f}")
        print(f"  F1-Score:  {result['f1']:.6f}")
        print(f"  ROC-AUC:   {result['roc_auc']:.6f}")
    
    # Generate visualizations
    print("\n[5] Generating visualizations...")
    plot_diabetes_distribution(df)
    plot_model_comparison(results, y_test)
    plot_confusion_matrices(results, y_test)
    plot_roc_curves(results, y_test)
    plot_feature_importance(models, feature_cols)
    plot_health_parameters_analysis(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All visualizations saved")
    print("="*80)

if __name__ == "__main__":
    main()
