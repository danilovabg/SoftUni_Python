message, action = input(), input()

while action != 'Decode':
    action = action.split('|')
    if action[0] == 'ChangeAll':
        message = message.replace(action[1], action[2])
    elif action[0] == 'Insert':
        st = list(message)
        st.insert(int(action[1]), action[2])
        message = ''.join(st)
    elif action[0] =='Move':
        x = int(action[1])
        message = message[x:] + message[:x]
    action = input()
    if action == 'Decode':
        break
print(f'The decrypted message is: {message}')