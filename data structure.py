# function "1" to check if num is prime
def isprime(x):
    #  we need to check for all odd numbers below square root of our number
    # +2 one for converting float to int and one for not taking the right limit
    j = int(x ** .5)
    i = 1
    # we assume that our num is prime until we prove it isn't
    y = True
    # 0 1 2 3 negative nums and any even num don't need any check
    if x == 2 or x == 3:
        return y
    elif x % 2 == 0 or x == 1 or x == 0 or x < 0:
        y = False
        return y
    else:
        while i > 0 and i < j:
            i = i + 2
            if x % i == 0 and x != i:
                y = False
                return y
        if y:
            return y
# checked all confusing nums + 12 random numbers



# function "2" to get all factors of a num
def factors(n):
    # simple code to get all factors of a num
    v = int( n ** .5)+1
    for pa in range (1,v):
        if n % pa == 0 :
            print(pa)
            if pa != int(n/pa):
                print(int(n/pa))


# function "3" to get the square root for perfect square numbers
def sqrt(x):
    # counter with 0 initial value
    ans = 0
    # 0 and negative nums need no check
    if x >= 0 :
        # check all nums square from zero to bigger than our num
        while x > ans * ans:
            ans = ans + 1
        if x == ans * ans :
            return ans 
        else:
            return 'not perfect square'
    else:
        return'a negative num is given'



# function "4" to print first  n  prime nums
def ppns(n):
    # 2 is the first prime num but it's even
    print(2, end=' ')
    # check or odd nums from 3 and up
    i = 3
    number_of_prime_nums = 1
    # collecting n prime numbers
    while number_of_prime_nums < n:
        if isprime(i):
            print(i, end=' ')
            i = i + 2
            number_of_prime_nums = number_of_prime_nums + 1
            # printing all 50 num in a line
            if number_of_prime_nums % 50 == 0 :
                print()
        else:
            i = i + 2


# function "5" to get square root of ana num by bisiction method
def square_root(x,n):
    if x < 0 :
        # accepts only positive nums
        return 'a negative num is given!'
    # x num to get its square root and n for  accuracy
    low = 0
    # if x < 1 guess from 0 to 1
    high = max(1, x)
    # guess the middle of range and count number of guesses
    num_of_guesses = 1
    guess = (high+low)/2
    # reguess until you get the desired accuracy
    while abs(guess*guess - x) >= n and num_of_guesses<100:
        if guess * guess > x:
            high = guess
            num_of_guesses = num_of_guesses + 1
        else:
            low = guess
            num_of_guesses =num_of_guesses  + 1
        guess = (high + low) / 2
    if num_of_guesses == 100 :
        return 'we have exceeded 100 guesses'
    else:
        return guess



# function "6" to get square root of any num by newten method

def Square_root(x,n):
    # x num to get its square root and n for  accuracy
    if x < 0 :
        # accepts onlu positive nums
        return 'negative num is given'
    x = float(x)
    # we can start with any guess
    guess = x/2
    num_of_guesses = 1
    diff = guess ** 2 - x
    # continue to check until we get our desired accuracy
    while abs(diff) >= n and num_of_guesses < 100 :
        guess = guess - diff/(2*guess)
        diff = guess ** 2 - x
        num_of_guesses = num_of_guesses + 1
    if num_of_guesses == 100:
        # 100 guesses is fuck
        return 'we have exceeded 100 guesses'
    else:
        return guess




# function "7" a simple ex to solve 2 eq in 2 variables

def guessANDcheck(heads,legs):
    # assume at first all is hens
    numOFhens = heads
    numOFhourses=0
    # reduce number of hens and increase num of horses until we get it
    for i in range(heads+1):
        numOFhens = heads - numOFhourses
        if 2 * numOFhens + 4 * numOFhourses == legs:
            return [('num of chicken',numOFhens),('num of horses',numOFhourses)]
        else:
            numOFhourses = numOFhourses + 1
    return 'nonsense'





# function "8"  to check if pallindrome or not
def isPalindrome(s):
    # takes a string and check all parallel index until the last one
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


# function "9" calculate triangle hypotenuse
import math
def caculate():
  inputOk = False
  while not inputOk:
    try:
      base = float(input('enter base'))
      hight = float(input('enter hight'))
      inputOk = True
    except:
       print('type error please enter float or integer ')
  hyp = math.sqrt((base**2+hight**2))
  return hyp
            

# function "10" binary search increase by log2 of lists size

def search(v, k):
    high = len(v)
    low = 0
    guess = int((high+low)/2)
    while high-low > 1:
        if v[guess] == k:
            return True
        elif v[guess] > k:
            if guess == len(v):
                return v[len(v)] == k
            high = guess
        else:
            if guess == 0:
                return v[0] == k
            low = guess
        guess = int((high+low)/2)
    for i in range(low, high+1):
        if v[i] == k:
            return True
        else:
            return False
def search1(l,v):

    # the same but with recursion
    if len(l)==0:
        return False
    elif len(l)==1:
        return l[0]==v
    else:
        half  = len(l)//2
        if l[half]== v :
            return True
        elif l[half]>v:
            return search1(l[:half],v)
        else:
            return search1(l[half+1:],v)        





# function "11" examples on recursion


def factorial(a):
    if a == 1 :
        return a
    else:
        return a * factorial(a-1)
def factorial2(a):
    prod = 1
    for i in range(1,a+1):
        prod *= i
    return prod
def mult(a,b):
    if b == 1 :
        return a
    else:
        return a + mult(a,b-1)
def towers(size,frome,to,spare):
    # towers rings challenge
    # when size = 1 move from from  to to
    # size > 1 move all rings but the last one from from to spare
    # move firs ring from from to to
    # move rest of rings from spare to to
    if size==1:
        print('move from '+str(frome) + ' to ' + str(to))
    else:
         towers(size-1,frome,spare,to)
         towers(1,frome,to,spare)
         towers(size-1,spare,to,frome)
def pallindrome(s):
    def tochars(s):
        # converts string to only letters without spaces or marks and all lowercase
        s = s.lower()
        ans = ''
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                ans += i
        return ans
    def ispal(s):
        if len(s) < 2:
            return True
        else:
            return s[0] == s[-1] and pallindrome(s[1:-1])
    return ispal(tochars(s))
def rabbits(n):
    # a pair of female and male are born every month
    # get older in month and reborn in month non is dead
    if n ==1 or n == 2 :
        return n
    if n == 0 :
        return  1
    else:return rabbits(n-1)+ rabbits(n-2)
    # inefficient and have a limit of 35 months
def rabbits2(n,d):

    # dictionary having known values and the future known is added
    if n in d:
        # if value is known return it
        return d[n]
    else:
        ans = rabbits2(n-1,d)+rabbits2(n-2,d)
        d[n]=ans
        return ans
    # very efficient and have a limit of 1000
    # if we tried to put dic in local scope in every
    # recursive step dic values will be ste to default
    # and we will be redo the previous code with the same
    # fucken efficiency
#dic = {0:1,1:1,2:2}
#print(rabbits2(1000,dic))
def rabbits3(n):
    # linear rabbits solution with 100000 limit
    if n == 0 :
        return n
    elif n == 1 :
        return n
    else:
        rabbits1 =0
        rabbits2=1
        for i in range(n-1):
            tmp = rabbits1
            rabbits1=rabbits2
            rabbits2=tmp+rabbits2
        return rabbits2    

def fib(n):
    global num_calls1
    num_calls1 += 1
    print('fib called with ' + str(n))
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib1(n):
    global num_calls2
    global memo
    num_calls2 += 1
    if n not in memo:
        memo[n] = fib1(n-1) + fib1(n-2)
    return memo[n]


##num_calls1 = 0
##num_calls2 = 0
##memo = {0: 1, 1: 1}
##print(fib(10), '    this is fib of(10)')
##print(num_calls1, '    this is number of calls')
##print(fib1(10), '   this is fib1 of 10 ')
##print(num_calls2, '    this is number of calls')
##




# function "12"  sorting & searchind



def binary_search(list1, value):
    high = len(list1)-1
    low = 0
    mid = int((high+low)/2)
    while high-low > 1:
        if list1[mid] == value:
            return True
        elif list1[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
        mid = int((high+low)/2)
    return list1[low] == value or list1[high] == value


def linear_search(list1, value):
    for i in range(len(list1)):
        if list1[i] == value:
            return True
    else:
        return False


def sel_sort(list1):
    suffix = 0
    while suffix != len(list1):
        for i in range(suffix, len(list1)):
            if list1[i] < list1[suffix]:
                list1[suffix], list1[i] = list1[i], list1[suffix]
        suffix += 1
    return list1


def bubble_sort(list1):
    sorted1 = False
    while not sorted1:
        sorted1 = True
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                sorted1 = False
                list1[i], list1[i+1] = list1[i+1], list1[i]
    return list1

def insertion_sort(A):
    """
    Sort list A into order, in place.
    From Cormen/Leiserson/Rivest/Stein,
    Introduction to Algorithms (second edition), page 17,
    modified to adjust for fact that Python arrays use
    0-indexing.
    """
    for j in range(1, len(A)):
        print(A)
        # insert A[j] into sorted sequence A[0..j-1]
        i = j - 1
        while A[i] > A[j]:
            A[i + 1], A[i] = A[i], A[i + 1]
            if i == 0:
                break
            j -= 1
            i -= 1
    return A

def merging_sub_lists(left, right):
    result = []
    # result is sorted list
    i, j = 0, 0
    # i for left and j for right
    while i < len(left) and j < len(right):
        # move on 2 sub lists and compare
        if left[i] < right[j]:
            # put smallest in result and move step in its sub list
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge(l1, l2):
    l = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            l.append(l1[0])
            l1.remove(l1[0])
        else:
            l.append(l2[0])
            l2.remove(l2[0])
    if len(l1) != 0:
        l.extend(l1)
    else:
        l.extend(l2)
    return l

def merge_sort(list1):
    if len(list1) < 2:
        return list1[:]
    else:
        mid = len(list1) // 2
        l1 = merge_sort(list1[:mid])
        l2 = merge_sort(list1[mid:])
        return merge(l1, l2)


##
##def merge_sort(list1):
##    if len(list1) < 2:
##        return list1[:]
##    else:
##        mid = len(list1) // 2
##        left = merge_sort(list1[:mid])
##        right = merge_sort(list1[mid:])
##        return merging_sub_lists(left, right)


# function "13" to reverse list


def rev_list_(L):
    for i in range(len(L)//2):
        j = len(L) - i - 1
        L[i], L[j] = L[j], L[i]
    return L




# function "14" to get the abs value

def abs(x):
    if x >= 0:
        return x
    else:
        return -x


# function "15" an application on dynamic programming with knapsack problem 

def max_value(w, v, i, aw, memo):
    """
    its an application on dynamic programming its called knapsack problem in which we take items with values
    and weights and a maximum allowed weight we want to get a maximum value under the weight constrain 
    we use dictionary as a memorization element to save previously calculated pairs of available weight and
    level or index
    """
    # we use global counter to get number of calls must be global not to be reset every call
    global num_calls
    num_calls += 1
    try:
        # we try to get the value from stored 
        return memo[(i, aw)]
    except:
        # it is not stored which gives key error
        if i == 0:
            # basic case with last level we check if we can add first item if added we add its value unless we add zero
            # and every added will be stored as an index weight pair 
            if w[i] <= aw:
                memo[(i, aw)] = v[i]
                return v[i]
            else:
                memo[(i, aw)] = 0
                return 0    
        #   not basic case we go back to previous level and store value   
        without_i = max_value(w, v, i - 1, aw, memo)
        if w[i] > aw:
            # in this level if we can add the element we do and return the updated available weight 
            memo[(i, aw)] = without_i
            return without_i
        else:
            with_i = max_value(w, v, i - 1, aw - w[i], memo) + v[i]
            memo[(i, aw)] = max(without_i, with_i)
            # last step we return the winning value
            return max(without_i, with_i)
def max_value_test():
    memo = {}
    aw = 8
    w = [1, 1, 5, 5, 3, 3, 4, 4]
    v = [15, 15, 10, 10, 9, 9, 5, 5]
    i = len(v) - 1
    print(max_value(w, v, i, aw, memo))
    print(num_calls)
#num_calls = 0
#max_value_test()


def max_vaslue(w, v, vo, i, aw, av):
    
    if i == 0:
        
        if w[i] <= aw and vo[i] <= av:
            return v[i]
        else:
            return 0
    else:
        without_i = max_vaslue(w, v, vo, i - 1, aw, av)
        with_i = max_vaslue(w, v, vo, i - 1, aw - w[i], av-vo[i]) + v[i]
        if w[i] > aw or vo[i] > av:
            return without_i
        else:
            return max(with_i, without_i)


def max_vaslue_test():
    aw = 5
    w = [5, 3, 2]
    v = [9, 7, 8]
    vo = [10, 10, 10]
    av = 30
    i = len(v) - 1
    print(max_vaslue(w, v, vo, i, aw, av))   





# function "16" to generate subsets of a set

def gen_subsets(n):
    if len(n) == 0:
        return [[]]
    extra = n[-1:]
    smaller = gen_subsets(n[:-1])
    new = []
    for smsll in smaller:
        new.append(smsll + extra)
    return smaller + new



# function "17" iterative fibonicci

def fib_iter(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            fib_i, fib_ii = fib_ii, fib_ii + fib_i
        return fib_ii


# function "17" Sort Method
def sort(l1, l):
    #l1 = l2[:]
    if len(l1) < 2:
        return l + l1
    else:
        m = min(l1)
        l.append(m)
        l1.remove(m)
        return sort(l1, l)

  
l1 = list(range(100, 0, -1))
test = sort(l1, [])

