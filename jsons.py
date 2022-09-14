import json 
with open ('cart_data.json', 'r') as file:
    json_object = json.load(file)

# refined_json_object = json_object['carts']
# print(json_object['carts'])

# input_user_id = 30

# for item in json_object['carts']:
#     # print(item['userId'])
#     if item['userId'] == input_user_id:
#         print(item['total'])

# input_user_id = 2


# for item in json_object['carts']:
#     if item['id'] == input_user_id:
#         prd = []
#         prd = item['products']
#         for dict in item['products']:
#             if (dict["discountPercentage"]):
#                 print(int(dict["discountPercentage"]))
#                 print(len(item["products"]))
        # print(prd)


for item in json_object['carts']:
    print(item['id'], len(item['products']),item['total'])

dict_obj = dict()
 
dict_obj['1'] = 'for'
dict_obj['2'] = 'geeks'
 
print(dict_obj)
    #  prd = []
    #  prd = item['products']
    #  for dict in prd:
    #     print(len(prd), dict['id'])

# print(len(json_object['carts']['product']))
        