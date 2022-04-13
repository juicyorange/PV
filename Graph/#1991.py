
'''
******* 문제 푼 후 느낀 것 *********
트리 순회에 관련된 문제로, 알고리즘 수업시간이나, 자료구조 수업시간에 수없이 봐왔었다.
하지만 오래되다 보니 기억이 드문드분 해져 잘 생각이 나지 않았다.
주기적으로 확인해서 까먹지 않도록 하자.

# 다시하기
'''

'''
2022/04/13
boj.kr/1991

트리 순회

문제 : ## 그림이 있는 문제이니 사이트에 가서 확인해보기

이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한
결과를 출력하는 프로그램을 작성하시오.

입력 :
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

결과 :
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = [[-1 for _ in range(3)] for _ in range(n)]


for i in range(n):
    root, left, right = map(str, input().split())
    arr[ord(root)-65][0] = ord(root)-65
    if(left != "."):
        arr[ord(root)-65][1] = ord(left)-65
    if(right != "."):
        arr[ord(root)-65][2] = ord(right)-65


def preorder(node):
    print(chr(node+65), end="")
    if (arr[node][1] != -1):
        preorder(arr[node][1])
    if (arr[node][2] != -1):
        preorder(arr[node][2])


def inorder(node):
    if (arr[node][1] != -1):
        inorder(arr[node][1])
    print(chr(node+65), end="")
    if (arr[node][2] != -1):
        inorder(arr[node][2])


def postorder(node):
    if (arr[node][1] != -1):
        postorder(arr[node][1])
    if (arr[node][2] != -1):
        postorder(arr[node][2])
    print(chr(node+65), end="")


preorder(0)
print("")
inorder(0)
print("")
postorder(0)
