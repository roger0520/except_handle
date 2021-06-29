# learn how to hand exception or error handling
try:
    with open('f.txt', 'r') as f:
        for line in f:
            x = int(line.strip())
except FileNotFoundError as err:
    print('I caught an error:', err)
except ValueError:
    print('could not convert to int')
else:
    print('no exception caught')
finally:
    print('in finally')





# s = input('enter a number: ')
# try:
#     n = int(s)
# except ValueError: #這樣寫是捕捉特定的錯誤  如果只有寫except: 這樣就是全部都抓
#     print('!!!! ValueError !!!! told you to enter a number')
# # except ValueError, NameError: #捕捉多個錯誤寫法之一 比較少這樣用 通常會分開
# #     print('!!!! ValueError !!!! told you to enter a number')
# except NameError:
#     print('NameError')


# print(n)

# try:
#     while True:
#             s = input('please enter a number: ')
#             n = int(s)
# except:
#     print('you forget enter a number')


i = 0
err_cnt = 0
while True:
    try:
        s = input('please enter a number: ')
        n = int(s)
        print(f'good, you enter {n}')
    except ValueError:
        err_cnt += 1
        if err_cnt >= 3:
            print('已經三次錯誤了，不讓妳玩了。')
            break
        print('你沒有輸入數字?')
    except KeyboardInterrupt:
        print('\n遊戲結束')
        break
    finally:
        i += 1
        print(f'這是第 {i} 次遊玩')
