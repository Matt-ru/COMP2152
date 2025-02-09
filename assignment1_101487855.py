""" 
Author: Matthew Zygiel
Student Number: 101487855
Comp2152 - Assignment 1
"""

gym_member = "Alex Alliton" # string
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # boolean

workout_stats = {
	"Alex": (30, 45, 20),
	"Jamie": (25, 50, 15),
	"Taylor": (40, 30, 25)
}

for friend, minutes in workout_stats.copy().times():
	total_minutes = sum(minutes)
	workout_stats[f"{friend}_Total"] = total_minutes
	
print(workout_stats)

workout_list = [minutes for friend, minutes in workout_stats.items() if not friend.endswith("_Total")]

print(workout_list)

yoga_running = [row[:2] for row in workout_list]
print("Yoga & Running Minutes:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Wightlifting Minutes (Last Two Friends):", weightlifting_last_two)
for friend, total in workout_stats.items():
	if friend.endswith("_Total") and total >= 120:
		name = friend.replace("_Total", "") 
		print(f"Great job staying active, {name}!")
		
friend_name = input("Enter a friend's name.")

if friend_name in workout_stats:

	yoga, running, weightlifting = workout_stats[friend_name]
	print(f"{friend_name}'s workout minutes:")
	print(f"	Yoga: {yoga} minutes")
	print(f"	Running: {running} minutes")
	print(f"	Weightlifting: {weightlifting")
	
	total_key = f"{friend_name}_Total"
	if total_key in workout_stats:
		print(f"	Total: {workout_stats[total_key]} minutes")
else: 
	print(f"Friend {friend_name} not found in the records.")

total_minutes_only = {friend: total for friend, total in workout_stats.items() if friend.endswith("_Total")}

max_friend = max(total_minutes_only, key = total_minutes_only.get)
min_friend = max(total_minutes_only, key = total_minutes_only.get)

print(f"Friend with the highest total workout minutes: {max_friend.replace('_Total', '')} ({total_minutes_only[max_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {min_friend.replace('_Total', '')} ({total_minutes_only[min_friend]} minutes)")
	
	