#Health Management System
# 3 clients - Krishna, Nischal and Parth
## store exercies and diet
## write a function, inp = client name
# Define client routines and diets in a dictionary
clients_data = {
    'Krishna': {
        'exercise': ['Cardio', 'Shoulder', 'Legs', 'Chest', 'Again Cardio'],
        'exercise_time': ['05:30:00', '08:30:00', '10:30:00', '12:30:00', '17:30:00'],
        'diet': ['Sattu and Fruits', 'Ghee-Roti-Sabzi', 'Dry fruits', 'Chole-Bhature'],
        'diet_time': ['07:30:00', '13:30:00', '18:30:00', '20:30:00']
    },
    'Nischal': {
        'exercise': ['Yoga', 'Back and Biceps', 'Abs', 'Running', 'Swimming'],
        'exercise_time': ['06:00:00', '09:00:00', '11:00:00', '15:00:00', '18:00:00'],
        'diet': ['Oats and Almond Milk', 'Vegetable Pulao', 'Mixed Nuts', 'Paneer Tikka'],
        'diet_time': ['08:00:00', '13:00:00', '16:00:00', '19:00:00']
    },
    'Parth': {
        'exercise': ['Cycling', 'Triceps', 'Chest', 'HIIT', 'Stretching'],
        'exercise_time': ['05:45:00', '09:15:00', '11:45:00', '14:30:00', '18:45:00'],
        'diet': ['Smoothie and Seeds', 'Rajma Rice', 'Fruit Salad', 'Mushroom Curry'],
        'diet_time': ['07:00:00', '12:30:00', '16:30:00', '20:00:00']
    }
}

# Take input from the user
clients = input("Enter the name of the client: ")
if clients not in clients_data: print("No user found"), exit()
routine = int(input("Press 0 for exercises and 1 for diet: "))
# Fetch the respective routine based on input
match routine:
    case 0 :
        for exercise, time in zip(clients_data[clients]['exercise'], clients_data[clients]['exercise_time']):
            print(f"{time}: {exercise}")
    case 1 : 
        for diet, time in zip(clients_data[clients]['diet'], clients_data[clients]['diet_time']):
            print(f"{time}: {diet}")
    case _ :
        print("Invalid Input")
