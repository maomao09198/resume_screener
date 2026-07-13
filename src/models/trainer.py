# src/models/trainer.py
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score
from src.features.extractor import FeatureExtractor

class ResumeTrainer:
    def __init__(self):
        self.extractor = FeatureExtractor()
        self.model = None
        
    def prepare_data(self, df):
        features = []
        for idx, row in df.iterrows():
            # Simulate resume text from skills
            resume_text = f"Experienced with {row['skills']}. {row['years_experience']} years."
            feat = self.extractor.create_features(resume_text)
            
            # Combine numerical + embedding
            X = np.concatenate([
                [feat['num_skills'], feat['skill_diversity']],
                feat['bert_embedding']
            ])
            features.append(X)
        
        X = np.array(features)
        y = df['fit'].values
        return X, y
    
    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        self.model = xgb.XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            use_label_encoder=False,
            eval_metric='logloss'
        )
        self.model.fit(X_train, y_train)
        
        y_pred = self.model.predict(X_test)
        print(f"F1 Score: {f1_score(y_test, y_pred):.3f}")
        print(f"AUC-ROC: {roc_auc_score(y_test, y_pred):.3f}")
        
        return self.model

# Run training
if __name__ == "__main__":
    df = pd.read_csv('data/labels.csv')
    trainer = ResumeTrainer()
    X, y = trainer.prepare_data(df)
    model = trainer.train(X, y)
    
    # Save model
    import joblib
    joblib.dump(model, 'models/resume_model.pkl')