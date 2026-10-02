"""
Diabetes Analytics Utilities
Generates detailed analytical datasets and insights for diabetes prediction system
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def generate_diabetes_dataset(n_samples=1000, random_state=42):
    """Generate synthetic diabetes dataset"""
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
    
    # Generate diabetes risk
    risk_score = (
        (df['Glucose_Level'] - 100) / 50 +
        (df['BMI'] - 25) / 5 +
        (df['Age'] - 40) / 20 +
        (df['Blood_Pressure_Systolic'] - 120) / 30 +
        (df['Insulin_Level'] - 70) / 50
    )
    
    risk_score += df['Family_History'] * 1.5
    risk_score += df['Smoking_Status'] * 1.0
    risk_score -= (df['Physical_Activity_hours'] / 10) * 0.8
    risk_score += np.random.normal(0, 0.5, n_samples)
    
    threshold = np.percentile(risk_score, 35)
    df['Diabetes_Risk'] = (risk_score > threshold).astype(int)
    
    # Clip values
    df['Glucose_Level'] = np.clip(df['Glucose_Level'], 50, 250)
    df['Blood_Pressure_Systolic'] = np.clip(df['Blood_Pressure_Systolic'], 80, 200)
    df['Blood_Pressure_Diastolic'] = np.clip(df['Blood_Pressure_Diastolic'], 40, 120)
    df['BMI'] = np.clip(df['BMI'], 15, 50)
    df['Insulin_Level'] = np.clip(df['Insulin_Level'], 10, 300)
    df['Skin_Thickness'] = np.clip(df['Skin_Thickness'], 0, 100)
    
    return df

def analyze_by_age_group(df):
    """Analyze diabetes risk by age group"""
    print("[1] Analyzing diabetes risk by age group...")
    
    df_age = df.copy()
    df_age['Age_Group'] = pd.cut(df_age['Age'], bins=[0, 30, 40, 50, 60, 100],
                                 labels=['20-30', '31-40', '41-50', '51-60', '60+'])
    
    stats = []
    for age_group in ['20-30', '31-40', '41-50', '51-60', '60+']:
        subset = df_age[df_age['Age_Group'] == age_group]
        risk_count = (subset['Diabetes_Risk'] == 1).sum()
        
        stats.append({
            'Age_Group': age_group,
            'Total_Patients': len(subset),
            'Diabetes_Risk_Count': risk_count,
            'Risk_Percentage': risk_count / len(subset) * 100 if len(subset) > 0 else 0,
            'Avg_Glucose': subset['Glucose_Level'].mean(),
            'Avg_BMI': subset['BMI'].mean()
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/diabetes_by_age_group.csv', index=False)
    print("✓ Saved: diabetes_by_age_group.csv")
    return stats_df

def analyze_by_bmi_category(df):
    """Analyze diabetes risk by BMI category"""
    print("[2] Analyzing diabetes risk by BMI category...")
    
    df_bmi = df.copy()
    df_bmi['BMI_Category'] = pd.cut(df_bmi['BMI'],
                                    bins=[0, 18.5, 25, 30, 100],
                                    labels=['Underweight', 'Normal', 'Overweight', 'Obese'])
    
    stats = []
    for bmi_cat in ['Underweight', 'Normal', 'Overweight', 'Obese']:
        subset = df_bmi[df_bmi['BMI_Category'] == bmi_cat]
        risk_count = (subset['Diabetes_Risk'] == 1).sum()
        
        stats.append({
            'BMI_Category': bmi_cat,
            'Total_Patients': len(subset),
            'Diabetes_Risk_Count': risk_count,
            'Risk_Percentage': risk_count / len(subset) * 100 if len(subset) > 0 else 0,
            'Avg_Glucose': subset['Glucose_Level'].mean(),
            'Avg_Insulin': subset['Insulin_Level'].mean()
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/diabetes_by_bmi_category.csv', index=False)
    print("✓ Saved: diabetes_by_bmi_category.csv")
    return stats_df

def analyze_by_glucose_level(df):
    """Analyze diabetes risk by glucose level"""
    print("[3] Analyzing diabetes risk by glucose level...")
    
    df_glucose = df.copy()
    df_glucose['Glucose_Category'] = pd.cut(df_glucose['Glucose_Level'],
                                            bins=[0, 100, 125, 200, 300],
                                            labels=['Normal', 'Prediabetic', 'Diabetic', 'Severe'])
    
    stats = []
    for glucose_cat in ['Normal', 'Prediabetic', 'Diabetic', 'Severe']:
        subset = df_glucose[df_glucose['Glucose_Category'] == glucose_cat]
        risk_count = (subset['Diabetes_Risk'] == 1).sum()
        
        stats.append({
            'Glucose_Category': glucose_cat,
            'Total_Patients': len(subset),
            'Diabetes_Risk_Count': risk_count,
            'Risk_Percentage': risk_count / len(subset) * 100 if len(subset) > 0 else 0,
            'Avg_Age': subset['Age'].mean(),
            'Avg_BMI': subset['BMI'].mean()
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/diabetes_by_glucose_level.csv', index=False)
    print("✓ Saved: diabetes_by_glucose_level.csv")
    return stats_df

def analyze_by_family_history(df):
    """Analyze diabetes risk by family history"""
    print("[4] Analyzing diabetes risk by family history...")
    
    stats = []
    for family_hist in [0, 1]:
        subset = df[df['Family_History'] == family_hist]
        risk_count = (subset['Diabetes_Risk'] == 1).sum()
        
        family_label = 'Yes' if family_hist == 1 else 'No'
        stats.append({
            'Family_History': family_label,
            'Total_Patients': len(subset),
            'Diabetes_Risk_Count': risk_count,
            'Risk_Percentage': risk_count / len(subset) * 100,
            'Avg_Age': subset['Age'].mean(),
            'Avg_Glucose': subset['Glucose_Level'].mean(),
            'Avg_BMI': subset['BMI'].mean()
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/diabetes_by_family_history.csv', index=False)
    print("✓ Saved: diabetes_by_family_history.csv")
    return stats_df

def analyze_by_smoking_status(df):
    """Analyze diabetes risk by smoking status"""
    print("[5] Analyzing diabetes risk by smoking status...")
    
    stats = []
    for smoking in [0, 1]:
        subset = df[df['Smoking_Status'] == smoking]
        risk_count = (subset['Diabetes_Risk'] == 1).sum()
        
        smoking_label = 'Smoker' if smoking == 1 else 'Non-Smoker'
        stats.append({
            'Smoking_Status': smoking_label,
            'Total_Patients': len(subset),
            'Diabetes_Risk_Count': risk_count,
            'Risk_Percentage': risk_count / len(subset) * 100,
            'Avg_Age': subset['Age'].mean(),
            'Avg_Glucose': subset['Glucose_Level'].mean(),
            'Avg_BMI': subset['BMI'].mean()
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/diabetes_by_smoking_status.csv', index=False)
    print("✓ Saved: diabetes_by_smoking_status.csv")
    return stats_df

def generate_clinical_insights(df):
    """Generate clinical insights"""
    print("[6] Generating clinical insights...")
    
    insights = []
    
    insights.append("DIABETES RISK PREDICTION SYSTEM - CLINICAL INSIGHTS")
    insights.append("="*70)
    
    insights.append(f"\nTotal Patients Analyzed: {len(df)}")
    insights.append(f"Patients with Diabetes Risk: {(df['Diabetes_Risk'] == 1).sum()} ({(df['Diabetes_Risk'] == 1).sum()/len(df)*100:.1f}%)")
    insights.append(f"Patients without Diabetes Risk: {(df['Diabetes_Risk'] == 0).sum()} ({(df['Diabetes_Risk'] == 0).sum()/len(df)*100:.1f}%)")
    
    insights.append("\n\nKey Health Metrics:")
    insights.append("-" * 70)
    insights.append(f"  Average Glucose Level: {df['Glucose_Level'].mean():.2f} mg/dL")
    insights.append(f"  Average BMI: {df['BMI'].mean():.2f} kg/m²")
    insights.append(f"  Average Age: {df['Age'].mean():.1f} years")
    insights.append(f"  Average Systolic BP: {df['Blood_Pressure_Systolic'].mean():.2f} mmHg")
    insights.append(f"  Average Insulin Level: {df['Insulin_Level'].mean():.2f} mIU/L")
    
    insights.append("\n\nRisk Factors Analysis:")
    insights.append("-" * 70)
    
    family_hist_risk = (df[df['Family_History'] == 1]['Diabetes_Risk'] == 1).sum() / len(df[df['Family_History'] == 1]) * 100
    insights.append(f"  Patients with Family History: {family_hist_risk:.1f}% have diabetes risk")
    
    smoker_risk = (df[df['Smoking_Status'] == 1]['Diabetes_Risk'] == 1).sum() / len(df[df['Smoking_Status'] == 1]) * 100
    insights.append(f"  Smokers: {smoker_risk:.1f}% have diabetes risk")
    
    high_glucose = df[df['Glucose_Level'] > 125]
    insights.append(f"  High Glucose (>125 mg/dL): {(high_glucose['Diabetes_Risk'] == 1).sum() / len(high_glucose) * 100:.1f}% have diabetes risk")
    
    obese = df[df['BMI'] > 30]
    insights.append(f"  Obese Patients (BMI>30): {(obese['Diabetes_Risk'] == 1).sum() / len(obese) * 100:.1f}% have diabetes risk")
    
    # Write insights to file
    with open('/home/ubuntu/diabetes_clinical_insights.txt', 'w') as f:
        f.write('\n'.join(insights))
    
    print("✓ Saved: diabetes_clinical_insights.txt")
    return insights

def generate_sample_risk_assessments(df):
    """Generate sample risk assessments"""
    print("[7] Generating sample risk assessments...")
    
    assessments = []
    
    # Select diverse patient profiles
    sample_patients = [
        df.iloc[0],
        df[df['Diabetes_Risk'] == 1].iloc[0],
        df[df['Age'] > 60].iloc[0],
        df[df['BMI'] > 35].iloc[0],
        df[df['Glucose_Level'] > 150].iloc[0],
    ]
    
    for i, patient in enumerate(sample_patients):
        risk_level = 'High Risk' if patient['Diabetes_Risk'] == 1 else 'Low Risk'
        
        assessments.append({
            'Assessment_ID': i + 1,
            'Patient_ID': patient['Patient_ID'],
            'Age': int(patient['Age']),
            'Glucose_Level': f"{patient['Glucose_Level']:.1f}",
            'BMI': f"{patient['BMI']:.1f}",
            'Family_History': 'Yes' if patient['Family_History'] == 1 else 'No',
            'Smoking_Status': 'Yes' if patient['Smoking_Status'] == 1 else 'No',
            'Risk_Classification': risk_level,
            'Recommendation': 'Immediate Medical Consultation' if patient['Diabetes_Risk'] == 1 else 'Regular Check-up'
        })
    
    assess_df = pd.DataFrame(assessments)
    assess_df.to_csv('/home/ubuntu/diabetes_sample_risk_assessments.csv', index=False)
    print("✓ Saved: diabetes_sample_risk_assessments.csv")
    return assess_df

def main():
    print("="*80)
    print("DIABETES ANALYTICS UTILITIES - GENERATING DETAILED DATASETS")
    print("="*80)
    print()
    
    # Generate main dataset
    print("Generating diabetes dataset...")
    df = generate_diabetes_dataset(n_samples=1000)
    df.to_csv('/home/ubuntu/diabetes_full_dataset.csv', index=False)
    print(f"✓ Dataset created: {df.shape[0]} records\n")
    
    # Generate analytical datasets
    analyze_by_age_group(df)
    analyze_by_bmi_category(df)
    analyze_by_glucose_level(df)
    analyze_by_family_history(df)
    analyze_by_smoking_status(df)
    generate_clinical_insights(df)
    generate_sample_risk_assessments(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All datasets generated successfully")
    print("="*80)

if __name__ == "__main__":
    main()
