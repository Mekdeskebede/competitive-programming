class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipe_dict = defaultdict(list)
        n = len(recipes)
        
        for i in range(n):
            for ingredient in ingredients[i]:
                recipe_dict[ingredient].append(recipes[i])
                
        incoming = defaultdict(int)
        for i in range(n):
            incoming[recipes[i]] = len(ingredients[i])
            
        queue = deque()
        for supply in supplies:
            queue.append(supply)
            
        order = []
        recipes_copy = set(recipes)
        while queue:
            node = queue.popleft()
            
            for neighbor in recipe_dict[node]:
                if incoming[neighbor]:
                    incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    order.append(neighbor)
                    queue.append(neighbor)
                    
        return order
        
                
        
        