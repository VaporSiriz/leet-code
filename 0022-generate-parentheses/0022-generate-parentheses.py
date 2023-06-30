class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(parenthesis: str):
            if buckets['l']==0 and buckets['r']==0:
                stack.append(parenthesis)
                return
            if buckets['l'] > buckets['r']:
                return
            if buckets['l']>0:
                buckets['l']-=1
                recursive(parenthesis+'(')
                buckets['l']+=1
            if buckets['r']>0:
                buckets['r']-=1
                recursive(parenthesis+')')
                buckets['r']+=1
        stack = []
        buckets = {
            'l': n,
            'r': n,
        }
        recursive('')
        return stack
        
        