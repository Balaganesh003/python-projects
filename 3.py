class Solution:
    def reduceTheDamage(self, districts, start):
        from collections import deque
        
        lenD = len(districts)
        lenS = len(start)
        
        # Step 1: Determine the initial infected state
        infected = [False] * lenD
        for s in start:
            infected[s] = True

        # Step 2: Simulate infection spread
        def simulate_seal(sealed):
            visited = [False] * lenD
            queue = deque()
            infected_count = 0

            # Initialize queue with initially infected districts
            for s in start:
                if s != sealed:
                    queue.append(s)
                    visited[s] = True
            
            # Spread the infection
            while queue:
                curr = queue.popleft()
                infected_count += 1
                for neighbor in range(lenD):
                    if districts[curr][neighbor] == 1 and not visited[neighbor] and neighbor != sealed:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            return infected_count
        
        # Step 3: Evaluate impact of sealing each district
        min_infected = float('inf')
        best_district = -1
        
        for i in range(lenD):
            if i not in start:
                continue  # Only consider sealing infected districts
            result = simulate_seal(i)
            if result < min_infected or (result == min_infected and i < best_district):
                min_infected = result
                best_district = i
        
        return best_district
