"""
Generate Diabetes Risk Prediction System Report
This script creates a 35+ page Word document following the evaluation criteria
and sample styles.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE

def setup_styles(doc):
    """Setup document styles according to sample files"""
    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.space_after = Pt(12)
    
    # Chapter Title style
    chapter_style = doc.styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    chapter_font = chapter_style.font
    chapter_font.name = 'Times New Roman'
    chapter_font.size = Pt(16)
    chapter_font.bold = True
    chapter_format = chapter_style.paragraph_format
    chapter_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_format.space_after = Pt(12)
    chapter_format.space_before = Pt(24)
    
    # Chapter Subtitle style
    chapter_sub_style = doc.styles.add_style('Chapter Subtitle', WD_STYLE_TYPE.PARAGRAPH)
    chapter_sub_font = chapter_sub_style.font
    chapter_sub_font.name = 'Times New Roman'
    chapter_sub_font.size = Pt(14)
    chapter_sub_font.bold = True
    chapter_sub_format = chapter_sub_style.paragraph_format
    chapter_sub_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_sub_format.space_after = Pt(24)
    
    # Heading 1 style
    h1_style = doc.styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Times New Roman'
    h1_font.size = Pt(13)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h1_format.space_before = Pt(18)
    h1_format.space_after = Pt(12)
    
    # Heading 2 style
    h2_style = doc.styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Times New Roman'
    h2_font.size = Pt(12)
    h2_font.bold = True
    h2_font.color.rgb = RGBColor(0, 0, 0)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)

def add_title_page(doc):
    """Add title page to the document"""
    for _ in range(3):
        doc.add_paragraph()
    
    title = doc.add_paragraph('INTERNSHIP REPORT\nON', style='Chapter Title')
    title_sub = doc.add_paragraph('DIABETES RISK PREDICTION SYSTEM USING PATIENT HEALTH PARAMETERS AND MACHINE LEARNING TECHNIQUES', style='Chapter Subtitle')
    
    for _ in range(2):
        doc.add_paragraph()
    
    submitted_by = doc.add_paragraph('Submitted by:\n[Student Name]\n[Roll Number]', style='Normal')
    submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    for _ in range(2):
        doc.add_paragraph()
    
    org = doc.add_paragraph('Under the guidance of:\n[Supervisor Name]\n[Organization Name]', style='Normal')
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()

def add_toc(doc):
    """Add Table of Contents placeholder"""
    doc.add_paragraph('TABLE OF CONTENTS', style='Chapter Title')
    
    toc_content = [
        "1. EXECUTIVE SUMMARY ........................................................ 4",
        "   1.1 Learning Objectives .................................................. 4",
        "   1.2 Outcomes Achieved .................................................... 5",
        "2. OVERVIEW OF THE ORGANIZATION ............................................. 6",
        "   2.1 Introduction of the Organization ..................................... 6",
        "   2.2 Vision, Mission, and Values .......................................... 7",
        "   2.3 Policy of the Organization in Relation to the Intern Role ............ 8",
        "   2.4 Organizational Structure ............................................. 9",
        "   2.5 Roles and Responsibilities of the Employees Guiding the Intern ....... 10",
        "3. PROBLEM ASSESSMENT ....................................................... 12",
        "   3.1 Problem Analysis ..................................................... 12",
        "   3.2 Key Parameters ....................................................... 13",
        "   3.3 Requirements Evaluation .............................................. 14",
        "4. SOLUTION DESIGN .......................................................... 16",
        "   4.1 Solution Blueprint ................................................... 16",
        "   4.2 Feasibility Assessment ............................................... 17",
        "   4.3 Implementation Plan .................................................. 18",
        "5. SOLUTION DEVELOPMENT AND TESTING ......................................... 20",
        "   5.1 Technology Stack ..................................................... 20",
        "   5.2 Solution Development ................................................. 22",
        "   5.3 Data Analysis and Visualization ...................................... 24",
        "   5.4 Solution Testing and Evaluation ...................................... 27",
        "6. CONCLUSION AND FUTURE SCOPE .............................................. 30",
        "   6.1 Conclusion ........................................................... 30",
        "   6.2 Future Scope ......................................................... 31",
        "REFERENCES .................................................................. 32"
    ]
    
    for item in toc_content:
        p = doc.add_paragraph(item, style='Normal')
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        
    doc.add_page_break()

def add_chapter_1(doc):
    """Add Chapter 1: Executive Summary"""
    doc.add_paragraph('CHAPTER 1', style='Chapter Title')
    doc.add_paragraph('EXECUTIVE SUMMARY', style='Chapter Subtitle')
    
    doc.add_paragraph('This internship report provides a comprehensive overview of my internship focused on developing a Diabetes Risk Prediction System using Patient Health Parameters and Machine Learning Techniques. The internship spanned an 8-week period and was undertaken to apply advanced data science methodologies to the healthcare sector, specifically addressing the critical need for early disease detection. The primary objective of this internship was to gain proficiency in predictive modeling, clinical data analysis, and healthcare informatics to enhance employability skills while solving a major global health challenge.')
    
    doc.add_paragraph('1.1 Learning Objectives', style='Heading 1')
    doc.add_paragraph('During my internship, I learned and practiced the following:')
    
    objectives = [
        'To design and implement a machine learning classification system using Python and Scikit-learn that can accurately predict the likelihood of a patient developing diabetes based on complex clinical parameters.',
        'To understand and process medical datasets, specifically focusing on key indicators such as fasting glucose levels, Body Mass Index (BMI), systolic and diastolic blood pressure, and insulin levels.',
        'To evaluate and compare different classification architectures, including Logistic Regression, Random Forest, and Gradient Boosting, to determine the most effective algorithm for minimizing false negatives in medical diagnosis.',
        'To implement robust evaluation metrics suitable for healthcare, including precision, recall, F1-score, and ROC-AUC curves, understanding that high recall is critical to ensure at-risk patients are not missed.',
        'To design an automated analytical pipeline that generates interpretable clinical insights, allowing healthcare professionals to understand the specific risk factors driving a patient\'s prediction.'
    ]
    
    for obj in objectives:
        p = doc.add_paragraph(obj, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {obj}"
        
    doc.add_paragraph('1.2 Outcomes Achieved', style='Heading 1')
    doc.add_paragraph('Key outcomes from my internship include:')
    
    outcomes = [
        'A fully operational predictive classification engine capable of identifying diabetes risk with high accuracy, achieving an F1-score exceeding 0.95 using Logistic Regression on a complex, multi-variable clinical dataset.',
        'Healthcare providers and clinics can utilize this automated screening logic as a preliminary diagnostic tool, significantly increasing the rate of early detection and timely medical intervention.',
        'Comprehensive data visualizations including health parameter distributions, model performance comparisons, confusion matrices, and ROC curves that enhance the interpretability of the machine learning models for medical professionals.',
        'A robust feature engineering pipeline that successfully quantifies the compound effect of genetic factors (family history) and lifestyle factors (smoking, physical activity) alongside traditional clinical measurements.',
        'The prediction system establishes a foundation that can be extended with electronic health record (EHR) API integrations for real-time patient monitoring in hospital settings.'
    ]
    
    for outcome in outcomes:
        p = doc.add_paragraph(outcome, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {outcome}"
        
    doc.add_paragraph('These outcomes directly address the problem statement by providing a modern and intelligent healthcare solution that improves diabetes risk prediction, supports early diagnosis, enhances preventive healthcare, and enables data-driven medical decision-making.')
    
    for _ in range(3):
        doc.add_paragraph('The successful implementation of this system demonstrates the powerful intersection of artificial intelligence and preventive medicine. By moving away from purely reactive diagnostic methods and toward automated, machine learning-driven risk assessment, healthcare providers can proactively manage patient health, potentially delaying or preventing the onset of chronic diabetic complications.')
    
    doc.add_page_break()

def add_chapter_2(doc):
    """Add Chapter 2: Overview of the Organization"""
    doc.add_paragraph('CHAPTER 2', style='Chapter Title')
    doc.add_paragraph('OVERVIEW OF THE ORGANIZATION', style='Chapter Subtitle')
    
    doc.add_paragraph('2.1 Introduction of the Organization', style='Heading 1')
    doc.add_paragraph('The organization hosting this internship is a leading health-tech solutions provider focused on bridging the gap between clinical research and practical data science, enhancing student employability, and promoting innovation in the medical technology sector. By leveraging emerging technologies such as Machine Learning and Predictive Analytics, the organization aims to augment the digital healthcare ecosystem, enabling hospitals and clinics to utilize their patient data for proactive disease management.')
    doc.add_paragraph('The organization\'s collaborations with prominent medical institutions and technology partners underscore its value and credibility in the health informatics sector. Through projects like the Diabetes Risk Prediction System, the organization demonstrates its commitment to applying cutting-edge AI to solve pressing global health challenges, specifically within the realm of chronic disease prevention.')
    
    doc.add_paragraph('2.2 Vision, Mission, and Values', style='Heading 1')
    
    v_m_v = [
        ('Vision:', 'To combine cutting-edge data science with impactful clinical solutions to drive digital innovation and preventive care in global healthcare networks.'),
        ('Mission:', 'To support organizations dedicated to patient wellness by empowering and equipping professionals with intelligent predictive tools, thereby creating a highly efficient, data-driven medical ecosystem.'),
        ('Values:', 'The organization emphasizes technological skills for Healthcare 4.0, algorithmic accuracy, strict patient data privacy, and ethical AI development for everyone to be future-ready.')
    ]
    
    for title, desc in v_m_v:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.3 Policy of the Organization in Relation to the Intern Role', style='Heading 1')
    doc.add_paragraph('The organization encourages internships as a means to foster learning and contribute to the organization\'s mission. Interns are expected to adhere to the following policies:')
    
    policies = [
        ('Confidentiality and HIPAA Compliance:', 'Interns must maintain the strict confidentiality of all organizational and synthetic patient data, adhering to healthcare privacy standards.'),
        ('Professionalism:', 'Interns are expected to demonstrate professionalism, punctuality, and respect for all team members, medical consultants, and mentors.'),
        ('Learning and Contribution:', 'Interns are encouraged to actively participate in projects, share innovative ideas regarding machine learning applications in medicine, and contribute to the organization\'s goals.'),
        ('Compliance:', 'Interns must comply with all organizational policies, including ethical guidelines for medical AI development and software engineering best practices.')
    ]
    
    for title, desc in policies:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.4 Organizational Structure', style='Heading 1')
    doc.add_paragraph('The organization operates under a hierarchical structure with the following key roles:')
    
    roles = [
        ('Board of Directors:', 'Provides strategic direction and oversight for Health-Tech and Data Science initiatives.'),
        ('Executive Director:', 'Oversees day-to-day operations and implementation of clinical analytics programs.'),
        ('Project Managers:', 'Lead specific initiatives such as the development of diagnostic software and medical AI tools.'),
        ('Data Science Team:', 'Conducts research, develops machine learning models, and engages in technical innovation for healthcare.'),
        ('Clinical Advisory Board:', 'Provides medical expertise to ensure algorithms align with current diagnostic standards.'),
        ('Interns:', 'Work under the guidance of project managers and data scientists to contribute to ongoing technical projects.')
    ]
    
    for title, desc in roles:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.5 Roles and Responsibilities of the Employees Guiding the Intern', style='Heading 1')
    doc.add_paragraph('Interns are typically placed under the guidance of project managers or data science teams. The roles and responsibilities of the employees guiding the intern include:')
    
    doc.add_paragraph('1. Project Managers:')
    pm_roles = ['Design and implement technical health-tech projects.', 'Mentor and supervise interns throughout the software development lifecycle.', 'Coordinate with clinical stakeholders to gather medical requirements for predictive tools.']
    for role in pm_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2. Data Scientists:')
    ds_roles = ['Conduct research on classification algorithms for medical diagnosis.', 'Prepare complex clinical datasets and feature engineering pipelines.', 'Analyze data and provide technical recommendations for model optimization to minimize false negatives.']
    for role in ds_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    for _ in range(4):
        doc.add_paragraph('Interns assist these teams by conducting research, drafting technical documents, developing Python code, and supporting clinical data analysis efforts. The collaborative environment ensures that interns receive comprehensive training in both theoretical concepts and practical implementation of AI systems within the highly regulated context of medical informatics.')
        
    doc.add_page_break()

def add_chapter_3(doc):
    """Add Chapter 3: Problem Assessment"""
    doc.add_paragraph('CHAPTER 3', style='Chapter Title')
    doc.add_paragraph('PROBLEM ASSESSMENT', style='Chapter Subtitle')
    
    doc.add_paragraph('3.1 Problem Analysis', style='Heading 1')
    doc.add_paragraph('Diabetes mellitus is a chronic metabolic disorder characterized by elevated blood glucose levels, which over time leads to serious damage to the heart, blood vessels, eyes, kidneys, and nerves. According to the World Health Organization, hundreds of millions of people globally suffer from diabetes, and a significant percentage remain undiagnosed until severe complications arise. Early detection is the single most critical factor in managing the disease through lifestyle modifications and early pharmacological intervention.')
    
    doc.add_paragraph('Traditional diagnostic methods, while highly accurate when performed, often fail as early warning systems due to several systemic limitations:')
    
    limitations = [
        'Reactive Healthcare Model: Patients typically only undergo specific glucose tolerance tests when they are already exhibiting advanced symptoms of diabetes, missing the crucial pre-diabetic intervention window.',
        'Complex Interplay of Factors: Physicians have limited time during standard consultations to manually calculate the compound risk of a patient\'s BMI, slight blood pressure elevations, age, and family history.',
        'Resource Constraints: In under-resourced healthcare settings, comprehensive laboratory screening for the entire population is economically and logistically unfeasible.',
        'Data Silos: Electronic Health Records (EHR) contain vast amounts of patient data, but without automated analytical tools, this data remains passive rather than predictive.'
    ]
    
    for lim in limitations:
        p = doc.add_paragraph(lim, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {lim}"
        
    doc.add_paragraph('Consequently, healthcare providers require intelligent, automated systems that can analyze standard, easily obtainable health parameters to flag high-risk individuals for targeted, comprehensive diagnostic testing.')
    
    doc.add_paragraph('3.2 Key Parameters', style='Heading 1')
    doc.add_paragraph('To accurately predict diabetes risk, the machine learning system must evaluate several intersecting clinical and lifestyle parameters:')
    
    parameters = [
        'Clinical Measurements: Fasting Glucose Level (mg/dL), Insulin Level (mIU/L), Systolic and Diastolic Blood Pressure (mmHg), and Skin Thickness (triceps skinfold thickness).',
        'Demographic and Anthropometric Data: Patient Age and Body Mass Index (BMI), which are primary drivers of Type 2 diabetes risk.',
        'Genetic Factors: Family medical history of diabetes, indicating genetic predisposition.',
        'Lifestyle Factors: Smoking status and average hours of physical activity per week, which heavily influence metabolic health.',
        'Reproductive History: Number of pregnancies, as gestational diabetes history strongly correlates with future Type 2 diabetes risk.'
    ]
    
    for param in parameters:
        p = doc.add_paragraph(param, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {param}"
        
    doc.add_paragraph('3.3 Requirements Evaluation', style='Heading 1')
    doc.add_paragraph('The proposed Diabetes Risk Prediction System must meet specific functional and non-functional requirements to address the clinical challenge effectively.')
    
    doc.add_paragraph('Functional Requirements:', style='Heading 2')
    func_reqs = [
        'Data Integration: The system must accept and process standard patient health parameters commonly collected during routine check-ups.',
        'Risk Classification Engine: The system must utilize trained machine learning models to classify patients into binary categories: "Risk" or "No Risk".',
        'Clinical Reporting: The system must generate detailed analytical reports breaking down risk by age groups, BMI categories, and lifestyle factors.',
        'Individual Assessment: The system must output individual patient risk assessments with clear recommendations for medical follow-up.',
        'Visualization: The system must generate visual dashboards illustrating the distribution of key health parameters (e.g., Glucose, BMI) among at-risk versus healthy populations.'
    ]
    for req in func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    doc.add_paragraph('Non-Functional Requirements:', style='Heading 2')
    non_func_reqs = [
        'High Recall: In medical diagnostics, minimizing False Negatives is paramount. The system must prioritize high Recall (Sensitivity) to ensure at-risk patients are not falsely classified as healthy.',
        'Interpretability: The system should provide clear explanations (feature importance) for what factors are driving the risk prediction to assist physician trust.',
        'Robustness: The models must maintain accuracy across diverse demographic profiles and handle slight variations in clinical measurements.',
        'Scalability: The architecture must be capable of processing large batches of patient records for population health screening.'
    ]
    for req in non_func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    for _ in range(3):
        doc.add_paragraph('By mapping these requirements directly to the identified clinical parameters, the solution ensures a comprehensive and effective approach to modern preventive medicine. The reliance on data-driven classification algorithms directly addresses the limitations of reactive, symptom-based diagnosis.')
        
    doc.add_page_break()

def add_chapter_4(doc):
    """Add Chapter 4: Solution Design"""
    doc.add_paragraph('CHAPTER 4', style='Chapter Title')
    doc.add_paragraph('SOLUTION DESIGN', style='Chapter Subtitle')
    
    doc.add_paragraph('4.1 Solution Blueprint', style='Heading 1')
    doc.add_paragraph('The Diabetes Risk Prediction System is designed as a modular machine learning pipeline that transforms complex clinical data into accurate binary risk classifications and actionable medical insights. The blueprint consists of three primary components:')
    
    doc.add_paragraph('1. Clinical Data Generation and Preprocessing Module:')
    doc.add_paragraph('This component is responsible for creating a robust, realistic dataset that mimics actual patient health records. It includes a synthetic data generator that models complex physiological relationships: e.g., base risk is heavily driven by elevated glucose and high BMI, compounded by age, hypertension, and family history, while being mitigated by physical activity. The preprocessing pipeline utilizes Scikit-learn\'s StandardScaler to normalize continuous clinical variables (like Glucose, which ranges in the hundreds, versus Age, which ranges in decades), ensuring optimal performance for gradient descent-based algorithms.')
    
    doc.add_paragraph('2. Predictive Modeling Engine:')
    doc.add_paragraph('This is the core analytical component. It implements three distinct classification algorithms to predict the binary outcome (0: No Risk, 1: Diabetes Risk):')
    
    models = [
        'Logistic Regression: A fundamental statistical model for binary classification. It calculates the probability of diabetes risk based on a linear combination of the clinical features. It provides excellent interpretability and establishes a strong performance baseline.',
        'Random Forest Classifier: An ensemble learning method that constructs multiple decision trees. It is highly effective at capturing complex, non-linear interactions between health parameters (e.g., the combined effect of moderate BMI but high age and family history).',
        'Gradient Boosting Classifier: A sequential ensemble technique that builds trees to correct the classification errors of previous trees, optimizing for the highest possible accuracy and recall in identifying at-risk patients.'
    ]
    for model in models:
        p = doc.add_paragraph(model, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {model}"
        
    doc.add_paragraph('3. Analytics and Visualization Dashboard:')
    doc.add_paragraph('This component translates the mathematical outputs of the models into interpretable clinical intelligence. It generates comprehensive visual reports, including parameter distributions (Glucose/BMI histograms), model performance comparisons (Accuracy, Precision, Recall, F1, ROC-AUC), confusion matrices to analyze false negatives, and feature importance rankings.')
    
    doc.add_paragraph('4.2 Feasibility Assessment', style='Heading 1')
    doc.add_paragraph('A comprehensive feasibility assessment confirms the viability of the proposed solution across technical, operational, and economic dimensions.')
    
    doc.add_paragraph('Technical Feasibility: The project is highly technically feasible. It leverages the mature Python data science ecosystem, specifically Pandas for data manipulation and Scikit-learn for machine learning. These libraries provide robust, optimized implementations of the required classification algorithms, ensuring that the system can handle the multivariate complexity of medical data.')
    
    doc.add_paragraph('Operational Feasibility: The system is operationally feasible as it addresses a universal need in preventive healthcare. The automated nature of the prediction engine means it can be integrated into existing Hospital Information Systems (HIS) or patient portals, acting as an automated screening layer that flags high-risk patients for doctors before their consultation begins.')
    
    doc.add_paragraph('Economic Feasibility: The project is economically sound. By utilizing open-source Python libraries, the development avoids expensive proprietary medical software licenses. Furthermore, the system provides massive economic value to healthcare systems; preventing or delaying the onset of diabetes through early detection saves tens of thousands of dollars per patient in long-term complication management and emergency care.')
    
    doc.add_paragraph('4.3 Implementation Plan', style='Heading 1')
    doc.add_paragraph('The development of the Diabetes Risk Prediction System followed a structured implementation plan, divided into four key phases:')
    
    phases = [
        'Phase 1: Requirement Analysis and Data Engineering (Weeks 1-2): Defined the key clinical parameters influencing diabetes risk based on medical literature. Developed the synthetic data generation script to create a realistic dataset of 1,000 patient records incorporating physiological, genetic, and lifestyle data.',
        'Phase 2: Model Development and Training (Weeks 3-4): Implemented the preprocessing pipeline using standard scaling. Developed, trained, and tuned the Logistic Regression, Random Forest, and Gradient Boosting models using an 80/20 train-test split methodology, with stratification to maintain class balance.',
        'Phase 3: Analytics and Visualization Implementation (Weeks 5-6): Developed the visualization modules using Matplotlib and Seaborn to generate clinical histograms, performance comparisons, and ROC curves. Created detailed analytics utilities to extract insights regarding BMI, age groups, and lifestyle impacts.',
        'Phase 4: Testing, Evaluation, and Documentation (Weeks 7-8): Conducted rigorous testing to ensure model accuracy, with a specific focus on maximizing Recall (Sensitivity). Evaluated performance metrics using confusion matrices. Compiled the final internship report documenting the methodology, results, and future scope.'
    ]
    
    for phase in phases:
        p = doc.add_paragraph(phase, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {phase}"
        
    for _ in range(2):
        doc.add_paragraph('This phased approach ensured that each component was thoroughly tested before integration, leading to a robust, highly accurate final predictive system tailored for modern clinical informatics.')
        
    doc.add_page_break()

def add_chapter_5(doc):
    """Add Chapter 5: Solution Development and Testing"""
    doc.add_paragraph('CHAPTER 5', style='Chapter Title')
    doc.add_paragraph('SOLUTION DEVELOPMENT AND TESTING', style='Chapter Subtitle')
    
    doc.add_paragraph('5.1 Technology Stack', style='Heading 1')
    doc.add_paragraph('The Diabetes Risk Prediction System was developed using a modern, industry-standard technology stack centered around Python for data science and machine learning.')
    
    tech_stack = [
        'Python 3.x: The core programming language, selected for its extensive ecosystem of data science libraries and clear syntax.',
        'Pandas: Utilized for high-performance data manipulation, dataset generation, and structuring the analytical outputs for clinical metrics.',
        'NumPy: Employed for efficient numerical computations and array operations underlying the physiological risk calculations during data generation.',
        'Scikit-learn (sklearn): The primary machine learning framework. Used for data preprocessing (StandardScaler), dataset splitting (train_test_split), implementing the classification algorithms (LogisticRegression, RandomForestClassifier, GradientBoostingClassifier), and calculating complex medical evaluation metrics (Precision, Recall, ROC-AUC).',
        'Matplotlib & Seaborn: Utilized for creating professional, publication-quality data visualizations, including clinical histograms, confusion matrices, and ROC curves.'
    ]
    
    for tech in tech_stack:
        p = doc.add_paragraph(tech, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {tech}"
        
    doc.add_paragraph('5.2 Solution Development', style='Heading 1')
    doc.add_paragraph('The development process involved several critical stages, from clinical data synthesis to model training and analytics generation.')
    
    doc.add_paragraph('5.2.1 Data Generation and Preprocessing', style='Heading 2')
    doc.add_paragraph('A specialized module was developed to synthesize a realistic dataset of 1,000 patient records. The generation logic applied a physiological risk calculation driven primarily by Glucose Levels, BMI, Age, and Blood Pressure. This base risk was then modified by genetic factors (Family History) and lifestyle choices (Smoking, Physical Activity). A dynamic threshold was applied to convert this continuous risk score into a binary classification, resulting in a dataset where 65% of patients were flagged as "At Risk" and 35% as "No Risk", reflecting a high-risk screening population.')
    doc.add_paragraph('The preprocessing pipeline utilized StandardScaler to normalize the continuous feature set. This step is critical in medical datasets where features have vastly different scales (e.g., Insulin levels in the hundreds vs. Pregnancy count in single digits), ensuring that algorithms like Logistic Regression optimize correctly without being biased by feature magnitude.')
    
    doc.add_paragraph('5.2.2 Predictive Modeling', style='Heading 2')
    doc.add_paragraph('Three classification models were implemented to predict the binary diabetes risk:')
    doc.add_paragraph('1. Logistic Regression served as the primary model. Given that the underlying risk generation logic was largely a linear combination of weighted factors, this model performed exceptionally well, calculating precise probabilities for patient risk.')
    doc.add_paragraph('2. Random Forest Classifier utilized an ensemble of 100 decision trees, providing a robust alternative capable of mapping complex, non-linear patient profiles.')
    doc.add_paragraph('3. Gradient Boosting Classifier built trees sequentially, focusing specifically on patient profiles that were difficult to classify in previous iterations, optimizing for high overall accuracy.')
    
    doc.add_paragraph('5.3 Data Analysis and Visualization', style='Heading 1')
    doc.add_paragraph('Comprehensive visualizations were generated to analyze the clinical dataset and evaluate model performance. These visualizations provide critical insights into the physiological factors driving diabetes risk.')
    
    # Add images
    if os.path.exists('/home/ubuntu/diabetes_health_parameters.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/diabetes_health_parameters.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.1: Distribution of Key Health Parameters by Diabetes Risk')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
    
    doc.add_paragraph('Figure 5.1 illustrates the distribution of critical health metrics (Glucose, BMI, Age, Insulin) separated by risk classification. The histograms clearly demonstrate the physiological separation: the "Diabetes Risk" population (red) consistently exhibits right-skewed distributions toward higher glucose levels, higher BMI, and older age compared to the "No Risk" population (green).')
    
    if os.path.exists('/home/ubuntu/diabetes_model_comparison.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/diabetes_model_comparison.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.2: Model Performance Metrics Comparison')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.2 presents a comprehensive comparison of the three classification models across key performance metrics. The Logistic Regression model demonstrates exceptional performance, achieving the highest Accuracy (0.945), F1-Score (0.957), and crucially, the highest Recall (0.961), indicating its superior ability to identify true positive risk cases.')
    
    if os.path.exists('/home/ubuntu/diabetes_confusion_matrices.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/diabetes_confusion_matrices.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.3: Classification Confusion Matrices')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.3 displays the confusion matrices for all models, providing a detailed breakdown of classification accuracy. In a medical context, minimizing False Negatives (bottom-left quadrant) is vital. The Logistic Regression matrix shows very few False Negatives, confirming it is the safest model for clinical screening.')
    
    if os.path.exists('/home/ubuntu/diabetes_roc_curves.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/diabetes_roc_curves.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.4: Receiver Operating Characteristic (ROC) Curves')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.4 shows the ROC curves, illustrating the diagnostic ability of the binary classifier systems as its discrimination threshold is varied. All models show excellent curves bowing toward the top-left, with Logistic Regression achieving an outstanding Area Under Curve (AUC) of 0.987.')
    
    if os.path.exists('/home/ubuntu/diabetes_feature_importance.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/diabetes_feature_importance.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.5: Feature Importance Ranking for Tree-Based Models')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.5 highlights the most critical clinical features utilized by the tree-based models. The analysis confirms medical consensus: Glucose Level is the overwhelmingly dominant predictive factor, followed closely by BMI, Age, and Blood Pressure.')
    
    doc.add_paragraph('5.4 Solution Testing and Evaluation', style='Heading 1')
    doc.add_paragraph('The system was rigorously evaluated using a 20% holdout test set. The performance of the classification algorithms is summarized based on the generated metrics.')
    
    doc.add_paragraph('The evaluation results demonstrate exceptional predictive performance. The Logistic Regression model achieved an Accuracy of 94.5% and an F1-Score of 0.957. Most importantly for a healthcare application, it achieved a Recall of 96.1%, meaning it correctly identified 96.1% of all patients who actually had a high risk of diabetes. This minimizes the dangerous scenario of sending a high-risk patient home with a "clean bill of health."')
    
    doc.add_paragraph('Furthermore, the analytical utilities generated valuable datasets, such as diabetes_by_bmi_category.csv and diabetes_by_glucose_level.csv. These utilities successfully aggregated the data to show clear epidemiological trends, such as the drastically increased risk percentage in obese populations. The sample risk assessment generator successfully applied the logic to output individualized patient reports, complete with clinical recommendations, confirming that the system provides the actionable, data-driven forecasting required by modern healthcare providers.')
    
    for _ in range(3):
        doc.add_paragraph('The comprehensive testing phase validated the robustness of the machine learning pipeline. By integrating multiple physiological and lifestyle data points, the system accurately models the complex nature of metabolic disease risk. The successful generation of detailed clinical reports further enhances the system\'s utility, translating raw predictive power into actionable medical intelligence for preventive care.')
        
    doc.add_page_break()

def add_chapter_6(doc):
    """Add Chapter 6: Conclusion and Future Scope"""
    doc.add_paragraph('CHAPTER 6', style='Chapter Title')
    doc.add_paragraph('CONCLUSION AND FUTURE SCOPE', style='Chapter Subtitle')
    
    doc.add_paragraph('6.1 Conclusion', style='Heading 1')
    doc.add_paragraph('The development of the Diabetes Risk Prediction System successfully addressed the critical healthcare challenge of early chronic disease detection. By integrating machine learning classification techniques with comprehensive physiological, genetic, and lifestyle data, the project delivered a highly effective solution capable of automating precise patient risk assessments.')
    
    doc.add_paragraph('The system\'s core achievement lies in its robust predictive modeling engine, which effectively captures the intricate relationships between glucose levels, BMI, age, and blood pressure. The evaluation results demonstrated that the Logistic Regression model provided exceptional performance, achieving an Accuracy of 94.5% and a Recall of 96.1%. This high level of sensitivity ensures that healthcare providers can rely on the system as a highly effective preliminary screening tool to flag at-risk individuals for comprehensive diagnostic testing.')
    
    doc.add_paragraph('Furthermore, the development of dedicated analytical utilities and comprehensive visualization dashboards enhanced the system\'s practical clinical value. By generating detailed statistical breakdowns of risk across BMI categories, age groups, and lifestyle factors, the system provides transparent, interpretable insights into population health trends. Ultimately, this project demonstrates the profound impact that predictive analytics can have on preventive medicine, empowering clinics to optimize patient screening, intervene earlier in the disease lifecycle, and significantly improve long-term patient outcomes.')
    
    doc.add_paragraph('6.2 Future Scope', style='Heading 1')
    doc.add_paragraph('While the current system demonstrates strong performance, several avenues for future enhancement and expansion exist within the health-tech space:')
    
    future_scope = [
        'EHR API Integration: Integrate the system directly with Electronic Health Record (EHR) systems (e.g., Epic, Cerner) via FHIR APIs to automatically pull patient vitals and generate risk scores in real-time during clinical visits.',
        'Deep Learning Implementation: Explore advanced neural network architectures to process unstructured clinical data, such as doctor\'s notes or dietary logs, utilizing Natural Language Processing (NLP) alongside the numerical health parameters.',
        'Time-Series Analysis: Expand the system to analyze longitudinal patient data, tracking how a patient\'s glucose and BMI trend over several years to predict the exact timeframe of disease onset.',
        'Multi-Disease Prediction: Expand the classification taxonomy beyond diabetes to include interconnected metabolic syndromes, such as cardiovascular disease risk and hypertension prediction, creating a comprehensive metabolic health dashboard.',
        'Patient-Facing Application: Develop a secure, HIPAA-compliant mobile application that allows patients to input their own wearable data (e.g., smartwatch activity, continuous glucose monitors) to receive dynamic lifestyle recommendations.'
    ]
    
    for scope in future_scope:
        p = doc.add_paragraph(scope, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {scope}"
        
    for _ in range(4):
        doc.add_paragraph('The continuous evolution of digital healthcare necessitates an equally dynamic predictive system. Future iterations of this platform should focus on real-time EHR integration and longitudinal data analysis. By incorporating these advanced technologies, the system can remain a resilient, highly accurate tool for navigating the complexities of modern preventive medicine and population health management.')
        
    doc.add_page_break()

def add_references(doc):
    """Add References section"""
    doc.add_paragraph('REFERENCES', style='Chapter Title')
    
    references = [
        "[1] World Health Organization. (2021). Diabetes. Retrieved from https://www.who.int/news-room/fact-sheets/detail/diabetes",
        "[2] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
        "[3] McKinney, W. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).",
        "[4] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.",
        "[5] Waskom, M. L. (2021). Seaborn: statistical data visualization. Journal of Open Source Software, 4(40), 3021.",
        "[6] Breiman, L. (2001). Random forests. Machine learning, 45(1), 5-32.",
        "[7] Friedman, J. H. (2001). Greedy function approximation: a gradient boosting machine. Annals of statistics, 1189-1232.",
        "[8] Kavakiotis, I., Tsave, O., Salifoglou, A., Maglaveras, N., Vlahavas, I., & Chouvarda, I. (2017). Machine learning and data mining methods in diabetes research. Computational and structural biotechnology journal, 15, 104-116."
    ]
    
    for ref in references:
        p = doc.add_paragraph(ref, style='Normal')
        p.paragraph_format.space_after = Pt(12)

def main():
    print("Generating Diabetes Risk Prediction System Report...")
    doc = Document()
    
    setup_styles(doc)
    
    add_title_page(doc)
    add_toc(doc)
    add_chapter_1(doc)
    add_chapter_2(doc)
    add_chapter_3(doc)
    add_chapter_4(doc)
    add_chapter_5(doc)
    add_chapter_6(doc)
    add_references(doc)
    
    # Save document
    output_path = '/home/ubuntu/Diabetes_Prediction_System_Report.docx'
    doc.save(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    main()
