
def recDc(change_list, change, result_dic):
    min_coin = change
    if change in change_list:
        return 1
    elif result_dic[change] > 0:
        return result_dic[change]
    else:
        for i in [c for c in change_list if c < change]:
            num_coins = 1 + recDc(change_list, change-i, result_dic)

            if num_coins < min_coin:
                min_coin = num_coins
                result_dic[change] = min_coin
    return min_coin

def dpDc(change_list, change, result_dic):
    for cents in range(1,change +1 ):
        count = cents
        for j in [c for c in change_list if c <= cents]:
            if result_dic[cents - j] + 1 < count:
                count = result_dic[cents - j] + 1
        result_dic[cents] = count
    return result_dic[change]

print (recDc([1,5,10,25], 63, {i : 0 for i in range(65)}))
print (dpDc([1,5,10,25], 63, {i : 0 for i in range(65)}))
