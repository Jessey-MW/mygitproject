import argparse,json

# parser = argparse.ArgumentParser()
# parser.description='帮助信息'
# parser.add_argument("-a", help="这是A",type=str,default="缺陷")
# parser.add_argument("-b", help="这是B",type=str,default="需求")
# args = parser.parse_args()
# if args.a:
#     print("这是A",args.a)
# if args.b:
#     print("这是B",args.b)

def read_json(path):
    file = open(path, "rb")
    fileJson = json.loads(file)
    print(fileJson)
