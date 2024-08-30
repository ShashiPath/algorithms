import random

def get_cost(craters, boulders, interests):
    # Higher craters, lower cost
    crater_cost = 9 - (craters // 10)
    # Higher boulders, lower cost
    boulder_cost = 9 - (boulders // 10)
    # Higher scientific interests, higher cost
    interest_cost = interests // 10
    
    # Ensure cost is within 0-9 range
    crater_cost = max(0, min(9, crater_cost))
    boulder_cost = max(0, min(9, boulder_cost))
    interest_cost = max(0, min(9, interest_cost))
    
    return crater_cost, boulder_cost, interest_cost

def average_cost(crater_cost, boulder_cost, interest_cost):
    return (crater_cost + boulder_cost + interest_cost) / 3

def generate_costs_for_areas(num_areas=30):
    costs = []
    
    for _ in range(num_areas):
        craters = random.randint(0, 100)
        boulders = random.randint(0, 100)
        interests = random.randint(0, 100)
        
        crater_cost, boulder_cost, interest_cost = get_cost(craters, boulders, interests)
        avg_cost = average_cost(crater_cost, boulder_cost, interest_cost)
        
        costs.append(round(avg_cost))
        
    return costs

# Generate costs for 30 nearby areas
costs_for_areas = generate_costs_for_areas()
print(f"The merit for 30 nearby areas are: {costs_for_areas}")
