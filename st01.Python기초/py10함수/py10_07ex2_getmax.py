# ����� �Լ� �����
# �� ���� ������ �־����� �μ� �߿��� �� ū ���� ã�Ƽ� �̰��� ��ȯ�ϴ� �Լ��� ������. 


# �Լ�����
# x : �Ű�����
# y : �Ű�����

def getmax(x, y):
    if x>y:
        return x # x ��ȯ
    else:
        return y # y ��ȯ
    
# return�� �� ���� ����ϴ°� ����
def getmax(x, y):
    result = None # None : ���� ����.
    
    if x>y:
        result = x # x ��ȯ
    else:
        result = y # y ��ȯ
    
    return result

n1 = input("ù��° ���� �Է� : ")
n1 = int(n1)

n2 = input("�ι�° ���� �Է� : ")
n2 = int(n2)

# �Ȱ��� �ڵ�� �Լ��� ����

def myinput() :
    n1 = input("ù��° ���� �Է� : ")
    n1 = int(n1)
    return n1

n1 = myinput()

# �Է¹޴� ������ �޽����� �ٸ��Ƿ�, mesgó��
def myinput(mesg) :
    try:  # ����ó��
        n1 = input(mesg)
        n1 = int(n1)        
    except ValueError as ex:
        print(ex)

    return n1


# �Է� ó��
n1 = myinput("ù��° ���� �Է�: ")
n2 = myinput("�ι�° ���� �Է�: ")

# �ִ밪 ���

val = getmax(n1, n2)
print(val)


# �Է�ó��, �ִ밪 ����� main �Լ��� �־ ���
# �� main �Լ��� ����� ����ϴ°�?
# ���α׷��Ϳ��� �����ϴ� ����� ���������� ������� �ʴ´�.

def main():
    # �Է� ó��
    n1 = myinput("ù��° ���� �Է�: ")
    n2 = myinput("�ι�° ���� �Է�: ")

    # �ִ밪 ���

    val = getmax(n1, n2)
    print(val)


main()