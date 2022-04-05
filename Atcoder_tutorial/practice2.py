import copy

#データの入力
N,Q=input().split()
N,Q=int(N),int(Q) 
count=0

#データの初期値を設定
input_data=""
for i in range(N):
    input_data += chr(ord("A")+i)
input_data=list(input_data)

# 一回の施行で全体で最大の値を決める
for i in range(N):
    for j in range(N-1-i):

#質問回数が規定数を超えた場合の処理
        if(Q<count):
            print("質問回数が規定数を超えました。")
            print(input_data)
            break
        
        print("?",input_data[j],input_data[j+1])
        ans=input()

        if ans==">":
            input_data[j],input_data[j+1]=input_data[j+1],input_data[j]
        count+=1

# 最大の値が決定するごとに表示する
    else:
        A=copy.deepcopy(i)
        display_data=[]

        for j in range(N):
            display_data.append("?")            

        while A>=0:
            display_data[N-A-1]=input_data[N-A-1]
            A-=1

        sub_out=""
        for j in display_data:
            sub_out+=j
        print(sub_out)

        continue
    break

#正常にソートが完了した場合の処理
if(Q>=count):
    print("ソートが完了しました. 質問回数は",count,"回でした")


    out_data=""
    for i in input_data:
        out_data+=i


    print("!",out_data)
        
