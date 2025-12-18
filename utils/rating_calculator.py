from flask import Flask, request, jsonify
from main import app, require_api_key


def calculate_rating(story_points, total_tasks, difficult_tasks, avg_iterations, performance_score):
    # SP Score
    sp_score = (story_points / 30) * 2

    # Difficulty Score
    difficulty_score = difficult_tasks / total_tasks if total_tasks > 0 else 0

    # Iteration Score
    if avg_iterations <= 1:
        iteration_score = 2.0
    elif avg_iterations <= 2:
        iteration_score = 1.5
    elif avg_iterations <= 3:
        iteration_score = 1.0
    elif avg_iterations <= 4:
        iteration_score = 0.5
    else:
        iteration_score = 0.0

    # Final Rating
    final_rating = sp_score + difficulty_score + iteration_score + performance_score
    return {
        "final_rating": round(final_rating, 2),
        "breakdown": {
            "sp_score": round(sp_score, 2),
            "difficulty_score": round(difficulty_score, 2),
            "iteration_score": iteration_score,
            "performance_score": performance_score
        }
    }

@app.route('/calculate-rating', methods=['POST'])
@require_api_key
def calculate():
    data = request.get_json()  or {}
    secret_key = data.get('secret_key')

    if secret_key != 'Tommy2025!':
        return jsonify({"error": "Invalid secret key"}), 403
    else:
        story_points = data.get('story_points', 0)
        total_tasks = data.get('total_tasks', 0)
        difficult_tasks = data.get('difficult_tasks', 0)
        avg_iterations = data.get('avg_iterations', 1)
        performance_score = data.get('performance_score', 1)  # 0.2 / 0.6 / 1

        result = calculate_rating(story_points, total_tasks, difficult_tasks, avg_iterations, performance_score)
        return jsonify(result)
