import collections


class Solution:

    def get_notes(self,start_node,adj_list, target_level):

        q = collections.deque()

        q.append((start_node,0))

        response = []
        while len(q):

            node_id,level = q.popleft()
            if level == target_level:
                response.append(node_id)


            neigbors = adj_list.get(node_id)

            for neighbor in neigbors:
                q.append((neighbor,level+1))


        return response


start_node = 0
root_node = 10
adj_list = {
    10:[5,6,1],
    5:[2,3],
    6:[],
    1:[0],
    2:[],
    3:[],
    0:[],
}

print(Solution().get_notes(root_node,adj_list,2))