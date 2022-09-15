def main(email, password):
    accounts = [
        ['t@t.com', '1234'],
        ['t2@t.com', '1234']
    ]

    selectedAccount = None
    for account in accounts:
        if account[0] == email:
            selectedAccount = account
            return

    if selectedAccount is None:
        print('Email incorrect')
        return

    if selectedAccount[1] != password:
        print('Password incorrect')
        return

    print('SignIn Ok!!')


if __name__ == '__main__':
    main('t@t.com', '1234')
    print('ryu')
