def revarr(arr):


    def hlper(ind, response):

        if ind<0:
            return response


        response.append(arr[ind])

        return hlper(ind-1, response)


    return hlper(len(arr)-1,[])


print(revarr([1,2,3,4,5]))