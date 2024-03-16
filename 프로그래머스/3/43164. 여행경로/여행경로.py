
def solution(tickets):
    answer=[]
    tickets.sort()
    
    def dfs(tickets, start, visited):
        if not tickets:
            return visited
        for i,ticket in enumerate(tickets):
            if ticket[0]==start:
                visited.append(ticket[1])
                result=dfs(tickets[0:i]+tickets[i+1:], ticket[1], visited)
                if result: 
                    return result
                visited.pop()
        return []
    
    answer=["ICN"]+dfs(tickets, "ICN", [])
    return answer