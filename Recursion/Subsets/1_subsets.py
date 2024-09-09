from datetime import datetime

def subset(str):
    response = []

    def helper(p, up):

        if not up:
            response.append(p)
            return


        helper(p+up[0], up[1::])
        helper(p,up[1::])


    helper("",str)
    return response

start_time = datetime.now()
print(subset("abcd"))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

