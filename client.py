import requests

url = "http://localhost:8000/predict"

sample_data = {
    "mean_radius": 14.2,
    "mean_texture": 20.1,
    "mean_perimeter": 92.3,
    "mean_area": 629.9,
    "mean_smoothness": 0.09,
    "mean_compactness": 0.10,
    "mean_concavity": 0.08,
    "mean_concave_points": 0.05,
    "mean_symmetry": 0.18,
    "mean_fractal_dimension": 0.06,
    "radius_error": 0.4,
    "texture_error": 1.2,
    "perimeter_error": 2.8,
    "area_error": 40.0,
    "smoothness_error": 0.007,
    "compactness_error": 0.02,
    "concavity_error": 0.03,
    "concave_points_error": 0.01,
    "symmetry_error": 0.02,
    "fractal_dimension_error": 0.003,
    "worst_radius": 16.0,
    "worst_texture": 25.0,
    "worst_perimeter": 105.0,
    "worst_area": 800.0,
    "worst_smoothness": 0.13,
    "worst_compactness": 0.25,
    "worst_concavity": 0.30,
    "worst_concave_points": 0.12,
    "worst_symmetry": 0.28,
    "worst_fractal_dimension": 0.08
}

response = requests.post(url, json=sample_data)
print("Status Code:", response.status_code)
print("Raw Response:", response.text)
