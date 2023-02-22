def connect(self, root):        
        queue=deque()
        queue.append(root)
        queue.append(None)
        while len(queue)>1:
            curr = queue.popleft()
            if curr == None:
                queue.append(None)
            else:
                curr.nextRight = queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
    
        
