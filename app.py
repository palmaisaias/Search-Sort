from flask import Flask, request, jsonify
from searcher_sorter import sort_videos, binary_search

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

sorted_videos = sort_videos(video_titles) #pops the video titles into the bubble sorter and retursn a beautiful, sorted list

@app.route('/search_video', methods=['GET'])
def search_video():
    title = request.args.get('title') #this pulls the title parameter from the url 
    if not title:
        return jsonify({'error': 'Please enter a title'}), 400
    
    index = binary_search(sorted_videos, title)
    if index is not None:
        print(f'{title} has been found')
        return jsonify({'message': "Here's what you were looking for!", 'title': sorted_videos[index]}), 200
    else:
        return jsonify({'error': 'Video not found in the list'}), 404

if __name__ == '__main__':
    app.run(debug=True)

