import pandas as pd
import json

from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

stats = ['age', 'height', 'weight', 'draft number', 'gp', 'reb', 'ast', 'netrtg', 'oreb', 'dreb', 'usg', 'ts', 'astp']

with open('/Users/shay/PycharmProjects/BasketballV2/src/data/training_data.json', 'r') as file:
    data = json.load(file)

df = pd.json_normalize(data, sep='_')

# Function to extract and convert player stats
def extract_player_stats(players, stats):
    aggregated_stats = {f'team_avg_{stat}': 0 for stat in stats}
    num_players = len(players)

    if num_players == 0:
        return aggregated_stats

    for player in players:
        for stat in stats:
            if stat == 'height':
                # Convert height to inches
                feet, inches = player.get(stat, '0-0').split('-')
                player[stat] = int(feet) * 12 + int(inches)
            # default stat is zero :)
            aggregated_stats[f'team_avg_{stat}'] += float(player.get(stat, 0))

    # Calculate average by dividing by number of players
    for stat in stats:
        aggregated_stats[f'team_avg_{stat}'] /= num_players

    return aggregated_stats


aggregated_stats = df['players'].apply(lambda x: extract_player_stats(x, stats=stats))
aggregated_stats_df = pd.json_normalize(aggregated_stats)

# Concatenate the aggregated stats with the original DataFrame
df = pd.concat([df, aggregated_stats_df], axis=1)

df.drop(columns=['players'], inplace=True)
df.drop(columns=['year'], inplace=True)
df.drop(columns=['rolling_average'], inplace=True)

df['scores'] = pd.to_numeric(df['scores'], errors='coerce')
df.dropna(subset=['scores'], inplace=True)
df.fillna(0, inplace=True)

X = df.drop(['scores'], axis=1)
y = df['scores']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Split the data into 0.8 training and 0.2 testing
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Splits
print(f"Training Features Shape: {X_train.shape}")
print(f"Testing Features Shape: {X_test.shape}")
print(f"Training Labels Shape: {y_train.shape}")
print(f"Testing Labels Shape: {y_test.shape}")

# Trial and error to minimize error
model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=100,
    learning_rate=0.12,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)

print(f"Initial Model Performance:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Trial and error to minimize error
param_dist = {
    'n_estimators': [100, 200, 300, 400, 500],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 5, 7, 9],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'gamma': [0, 0.1, 0.2, 0.3],
    'reg_alpha': [0, 0.01, 0.1, 1],
    'reg_lambda': [1, 1.5, 2, 3]
}

xgb_model = xgb.XGBRegressor(
    objective='reg:squarederror',
    random_state=42,
    n_jobs=-1
)

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=xgb_model,
    param_distributions=param_dist,
    n_iter=50,  # Number of parameter settings sampled
    scoring='neg_mean_squared_error',
    cv=3,
    verbose=1,
    random_state=42,
    n_jobs=-1
)

# Fit RandomizedSearchCV
random_search.fit(X_train, y_train)

# Best parameters
print(f"Best Parameters: {random_search.best_params_}")

# Best estimator
best_model = random_search.best_estimator_

# Make predictions with the best model
final_predictions = best_model.predict(X_test)

# Evaluate the model
final_mae = mean_absolute_error(y_test, final_predictions)
final_rmse = mean_squared_error(y_test, final_predictions, squared=False)

print(f"Final Model Performance:")
print(f"Mean Absolute Error (MAE): {final_mae}")
print(f"Root Mean Squared Error (RMSE): {final_rmse}")

# 11. Feature Importance Visualization
importances = best_model.feature_importances_
feature_names = X_train.columns

feature_importances = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(15, 6))
# plt.(x='Importance', y='Feature', data=feature_importances.head(10))
sns.barplot(x='Importance', y='Feature', data=feature_importances.head(15))
plt.title('Top 10 Feature Importances')
plt.tight_layout()
plt.show()