# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    is_desired_state = desired_state == 'well-done' or 'medium'
    is_criteria_satisfied_well_done = time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE
    is_criteria_satisfied_medium = time * temperature * pressure * COOKED_CONSTANT >= MEDIUM
    
    if desired_state == is_desired_state and is_criteria_satisfied_well_done: 
        return True
    if desired_state == is_desired_state and is_criteria_satisfied_medium:
        return True
    return False